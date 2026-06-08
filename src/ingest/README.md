# Ingest

이 폴더는 프로젝트에서 사용한 데이터 수집 코드와 수집 방법 설명을 저장한다.

## 포함 파일

- `collect_youtube_comments.py`
  - YouTube Data API `commentThreads.list`를 사용하여 영상 댓글 raw 데이터를 수집하는 코드
  - 수집 결과는 `youtube_comments_raw.jsonl`, `youtube_comments_summary.csv`, `youtube_comments_error_log.csv`로 저장됨
  - 실제 API Key는 보안상 코드에 포함하지 않으며, 실행 시 직접 입력하거나 환경변수로 관리함

## 수집 데이터

본 프로젝트에서는 Google Trends, Naver DataLab, YouTube Data API를 활용하여 검색 관심도와 YouTube 영상 성과 데이터를 수집하였다.  
추가로 누적 100MB 이상 raw 데이터 확보 및 사용자 반응 데이터 보강을 위해 YouTube 댓글 raw 데이터를 JSONL 형식으로 수집하였다.

- 댓글 raw 수집 규모: 58,787개
- 댓글 raw JSONL 용량: 약 120.11MB
- HDFS raw 전체 용량: 약 120.5MB
- GitHub에는 대용량 원본 파일 대신 `data/sample/`에 샘플 파일만 업로드하였다.
