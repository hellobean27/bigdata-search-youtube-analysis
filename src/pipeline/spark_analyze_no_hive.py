# -*- coding: utf-8 -*-
from __future__ import print_function

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, avg, countDistinct, sum as spark_sum,
    when, expr, desc
)

spark = SparkSession.builder \
    .appName("SearchYouTubeTrendAnalysisNoHive") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

raw_path = "/user/maria_dev/search_youtube/raw"
processed_path = "/user/maria_dev/search_youtube/processed"
results_path = "/user/maria_dev/search_youtube/results"

youtube = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("multiLine", "true") \
    .option("escape", "\"") \
    .csv(raw_path + "/youtube_trends_merged_20keywords.csv")

print("===== Raw row count =====")
print(youtube.count())

youtube_clean = youtube.select(
    col("category"),
    col("keyword"),
    col("video_id"),
    col("title"),
    col("channel_title"),
    col("published_at"),
    col("view_count").cast("double").alias("view_count"),
    col("like_count").cast("double").alias("like_count"),
    col("comment_count").cast("double").alias("comment_count"),
    col("google_interest").cast("double").alias("google_interest"),
    col("naver_interest").cast("double").alias("naver_interest"),
    col("days_since_upload").cast("double").alias("days_since_upload"),
    col("views_per_day").cast("double").alias("views_per_day")
).dropDuplicates(["keyword", "video_id"])

youtube_clean = youtube_clean.withColumn(
    "is_million_view",
    when(col("view_count") >= 1000000, 1).otherwise(0)
)

print("===== Clean row count =====")
print(youtube_clean.count())

youtube_clean.coalesce(1).write.mode("overwrite") \
    .option("header", "true") \
    .csv(processed_path + "/youtube_clean_csv")

keyword_summary = youtube_clean.groupBy("category", "keyword").agg(
    avg("google_interest").alias("google_interest"),
    avg("naver_interest").alias("naver_interest"),
    countDistinct("video_id").alias("video_count"),
    avg("view_count").alias("avg_view_count"),
    expr("percentile_approx(view_count, 0.5)").alias("median_view_count"),
    avg("like_count").alias("avg_like_count"),
    avg("comment_count").alias("avg_comment_count"),
    spark_sum("is_million_view").alias("million_view_count"),
    avg("views_per_day").alias("avg_views_per_day"),
    expr("percentile_approx(views_per_day, 0.5)").alias("median_views_per_day")
)

keyword_summary = keyword_summary.withColumn(
    "million_view_ratio",
    col("million_view_count") / col("video_count")
)

keyword_summary.coalesce(1).write.mode("overwrite") \
    .option("header", "true") \
    .csv(results_path + "/spark_keyword_summary")

category_summary = youtube_clean.groupBy("category").agg(
    countDistinct("keyword").alias("keyword_count"),
    countDistinct("video_id").alias("video_count"),
    avg("view_count").alias("avg_view_count"),
    expr("percentile_approx(view_count, 0.5)").alias("median_view_count"),
    avg("like_count").alias("avg_like_count"),
    avg("comment_count").alias("avg_comment_count"),
    spark_sum("is_million_view").alias("million_view_count"),
    avg("views_per_day").alias("avg_views_per_day"),
    expr("percentile_approx(views_per_day, 0.5)").alias("median_views_per_day")
)

category_summary = category_summary.withColumn(
    "million_view_ratio",
    col("million_view_count") / col("video_count")
)

category_summary.coalesce(1).write.mode("overwrite") \
    .option("header", "true") \
    .csv(results_path + "/spark_category_summary")

metrics = [
    "avg_view_count",
    "avg_views_per_day",
    "million_view_ratio",
    "avg_like_count",
    "avg_comment_count"
]

corr_rows = []

for metric in metrics:
    google_corr = keyword_summary.stat.corr("google_interest", metric)
    naver_corr = keyword_summary.stat.corr("naver_interest", metric)
    corr_rows.append((metric, google_corr, naver_corr))

corr_df = spark.createDataFrame(
    corr_rows,
    ["metric", "google_corr", "naver_corr"]
)

corr_df.coalesce(1).write.mode("overwrite") \
    .option("header", "true") \
    .csv(results_path + "/spark_correlation")

print("===== Spark Keyword Summary TOP 20 =====")
keyword_summary.orderBy(desc("avg_views_per_day")).show(20, False)

print("===== Spark Category Summary =====")
category_summary.orderBy(desc("avg_views_per_day")).show(10, False)

print("===== Spark Correlation Result =====")
corr_df.show(20, False)

print("Spark analysis completed successfully.")

spark.stop()
