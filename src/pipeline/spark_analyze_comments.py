from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, count, countDistinct, avg, length, coalesce, lit
)

spark = SparkSession.builder \
    .appName("SearchYouTubeCommentAnalysis") \
    .getOrCreate()

comments_path = "/user/maria_dev/search_youtube/raw/comments/youtube_comments_raw.jsonl"
merged_path = "/user/maria_dev/search_youtube/raw/youtube_trends_merged_20keywords.csv"
out_path = "/user/maria_dev/search_youtube/results/spark_comment_keyword_summary"

# 1.  raw JSONL 
comments = spark.read.json(comments_path)

# 2.  YouTube  CSV video_id, keyword, category  
video_map = spark.read.option("header", "true").csv(merged_path) \
    .select("video_id", "keyword", "category") \
    .dropDuplicates(["video_id", "keyword", "category"])

# 3.      
comment_clean = comments.select(
    col("video_id"),
    col("video_title"),
    col("channel_title"),
    col("comment_id"),
    col("comment_text"),
    col("comment_like_count").cast("double").alias("comment_like_count"),
    col("reply_count").cast("double").alias("reply_count")
).dropna(subset=["video_id", "comment_id"])

# 4. video_id   /  
joined = comment_clean.join(video_map, on="video_id", how="left")

# 5. /   
summary = joined.groupBy("keyword", "category").agg(
    count("*").alias("collected_comment_count"),
    countDistinct("video_id").alias("commented_video_count"),
    avg("comment_like_count").alias("avg_comment_like_count"),
    avg("reply_count").alias("avg_reply_count"),
    avg(length(coalesce(col("comment_text"), lit("")))).alias("avg_comment_text_length")
).orderBy(col("collected_comment_count").desc())

summary.coalesce(1).write.mode("overwrite").option("header", "true").csv(out_path)

print("Comment analysis completed successfully.")
spark.stop()
