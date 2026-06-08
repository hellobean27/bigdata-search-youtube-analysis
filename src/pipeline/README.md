# Pipeline

이 폴더는 HDFS에 저장된 데이터를 Spark로 처리하는 분석 코드를 포함한다.

- spark_analyze_no_hive.py
  - YouTube 영상 성과 데이터와 검색 관심도 병합 데이터를 Spark로 집계
  - keyword/category summary 및 correlation 결과 생성

- spark_analyze_comments.py
  - YouTube 댓글 raw JSONL 데이터를 Spark로 읽기
  - video_id 기준으로 기존 영상 데이터와 연결
  - 키워드/분야별 댓글 수, 댓글 좋아요, 답글 수, 댓글 길이 집계
