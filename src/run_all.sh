#!/bin/bash

set -e

echo "1. HDFS 경로 생성"
hdfs dfs -mkdir -p /user/maria_dev/search_youtube/raw
hdfs dfs -mkdir -p /user/maria_dev/search_youtube/raw/comments
hdfs dfs -mkdir -p /user/maria_dev/search_youtube/processed
hdfs dfs -mkdir -p /user/maria_dev/search_youtube/results

echo "2. 기존 CSV 원본 데이터 업로드"
hdfs dfs -put -f data/*.csv /user/maria_dev/search_youtube/raw/ || true

echo "3. 댓글 raw 데이터 업로드"
hdfs dfs -put -f data/youtube_comments_raw.jsonl /user/maria_dev/search_youtube/raw/comments/ || true
hdfs dfs -put -f data/youtube_comments_summary.csv /user/maria_dev/search_youtube/raw/comments/ || true
hdfs dfs -put -f data/youtube_comments_error_log.csv /user/maria_dev/search_youtube/raw/comments/ || true

echo "4. HDFS raw 전체 용량 확인"
hdfs dfs -du -h -s /user/maria_dev/search_youtube/raw

echo "5. YouTube 영상 성과 Spark 분석 실행"
spark-submit --master 'local[2]' src/pipeline/spark_analyze_no_hive.py

echo "6. YouTube 댓글 raw Spark 분석 실행"
spark-submit --master 'local[2]' src/pipeline/spark_analyze_comments.py

echo "7. Spark 결과 확인"
hdfs dfs -ls -R /user/maria_dev/search_youtube/results

echo "Pipeline completed successfully."
