# # 최근 30일 Google·Naver 검색 관심도와 최근 업로드 YouTube 영상의 누적 성과 지표 분석

## 1. 프로젝트 개요

본 프로젝트는 수집일 기준 최근 30일 동안의 Google Trends와 Naver DataLab 검색 관심도 데이터를 기반으로, 검색 관심도가 높은 키워드가 YouTube 영상 성과 지표와 어떤 관계를 가지는지 분석한다.

YouTube 영상 성과 지표는 수집 시점 기준 누적 조회수, 좋아요 수, 댓글 수, 영상 개수, 100만 조회수 이상 여부, 업로드 후 경과일을 반영한 일평균 조회수 등을 사용한다.

본 프로젝트는 검색 관심도가 YouTube 조회수를 직접 발생시켰다는 인과관계를 주장하지 않고, 검색 관심도와 YouTube 영상 성과 지표 사이의 상관관계와 패턴을 탐색하는 것을 목표로 한다.

## 2. 문제 정의

사람들은 특정 이슈나 키워드에 관심이 생기면 Google이나 Naver에서 검색하고, 동시에 YouTube에서 관련 영상을 소비한다. 그러나 검색 관심도가 높은 키워드가 YouTube에서도 높은 조회수, 좋아요 수, 댓글 수로 나타나는지는 명확하지 않다.

따라서 본 프로젝트는 최근 30일 검색 관심도와 같은 기간에 업로드된 YouTube 영상의 성과 지표를 수집하여, 검색 기반 관심과 영상 소비 사이의 관계를 분석한다.

특히 YouTube 조회수는 시간이 지날수록 누적되는 값이기 때문에, 단순 누적 조회수뿐 아니라 업로드 후 경과일을 반영한 일평균 조회수도 함께 분석한다.

## 3. 분석 질문

1. Google Trends 검색 관심도가 높은 키워드일수록 관련 YouTube 영상의 평균 조회수가 높은가?
2. Naver DataLab 검색 관심도가 높은 키워드일수록 관련 YouTube 영상의 평균 조회수가 높은가?
3. Google/Naver 검색 관심도와 YouTube 좋아요 수, 댓글 수 사이에도 관계가 있는가?
4. 검색 관심도가 높은 키워드에서 100만 조회수 이상 영상 비율이 더 높게 나타나는가?
5. 누적 조회수보다 일평균 조회수를 사용할 때 검색 관심도와 YouTube 성과 지표의 관계가 더 명확하게 나타나는가?

## 4. 데이터 수집 계획

### Google Trends Data

- 대상 기간: 수집일 기준 최근 30일
- 대상 지역: 대한민국
- 수집 항목: 키워드별 검색 관심도
- 데이터 의미: 절대 검색량이 아닌 상대 검색 관심도
- 예상 파일 형식: CSV

### Naver DataLab Data

- 대상 기간: 수집일 기준 최근 30일
- 대상 지역: 대한민국
- 수집 항목: 키워드별 검색 관심도
- 데이터 의미: 절대 검색량이 아닌 상대 검색 지수
- 예상 파일 형식: JSON 또는 CSV

### YouTube Data

- 수집 방식: YouTube Data API
- 수집 기준: Google Trends 및 Naver DataLab에서 선정한 키워드와 관련된 YouTube 영상
- 영상 조건: 최근 30일 이내 업로드된 영상
- 수집 항목:
  - video_id
  - title
  - channel_title
  - published_at
  - view_count
  - like_count
  - comment_count
  - collected_at

YouTube Data API에서 제공하는 조회수는 특정 기간 동안 발생한 조회수가 아니라 수집 시점 기준 누적 조회수이다. 따라서 본 프로젝트에서는 업로드 후 경과일을 계산하여 일평균 조회수도 함께 사용한다.

## 5. 기술 스택

- 데이터 수집: Python, Google Trends CSV, Naver DataLab API, YouTube Data API
- 저장: HDFS
- 전처리: Apache Spark DataFrame
- 분석: Spark SQL, HiveQL
- 시각화: Matplotlib
- 버전 관리: GitHub

## 6. 데이터 파이프라인

Google Trends / Naver DataLab 검색 관심도 데이터 수집  
→ 검색 관심도 기반 키워드 선정  
→ YouTube Data API로 관련 영상 메타데이터 수집  
→ raw JSON/CSV 저장  
→ HDFS 업로드  
→ Spark 전처리  
→ Hive 테이블 생성  
→ 키워드별 YouTube 성과 지표 집계  
→ 검색 관심도와 YouTube 성과 지표의 상관관계 분석  
→ 결과 시각화 및 보고서 작성

## 7. 예상 분석 지표

### 검색 관심도 지표

- Google Trends 관심도
- Naver DataLab 관심도

### YouTube 성과 지표

- 키워드별 영상 개수
- 키워드별 평균 조회수
- 키워드별 중앙값 조회수
- 키워드별 평균 좋아요 수
- 키워드별 평균 댓글 수
- 100만 조회수 이상 영상 개수
- 100만 조회수 이상 영상 비율
- 업로드 후 경과일 기준 일평균 조회수

## 8. 예상 결과

Google Trends와 Naver DataLab의 검색 관심도 지표를 각각 YouTube 영상 성과 지표와 비교하여, 검색 관심도가 높은 키워드가 YouTube에서도 높은 영상 소비 지표로 나타나는지 분석한다.

또한 누적 조회수는 업로드 시점에 따라 차이가 발생할 수 있으므로, 일평균 조회수를 함께 계산하여 시간 차이에 따른 왜곡을 줄이고자 한다.

## 9. 한계

Google Trends와 Naver DataLab의 값은 절대 검색량이 아니라 상대적 검색 관심도이다. 따라서 본 프로젝트에서는 이를 실제 검색 횟수로 해석하지 않고, 검색 관심도와 검색 추이를 나타내는 지표로 사용한다.

또한 YouTube Data API에서 제공하는 조회수는 수집 시점 기준 누적 조회수이므로, 최근 30일 동안 발생한 조회수와는 다르다. 따라서 본 프로젝트는 검색 관심도가 YouTube 조회수를 직접 증가시켰다는 인과관계를 주장하지 않고, 두 지표 사이의 관계를 탐색하는 분석으로 제한한다.

## AI Tool Usage

- ChatGPT: 프로젝트 요구사항 이해, 주제 구체화, API 수집 절차 정리, Spark/Hadoop/Hive 오류 디버깅 지원, 보고서 목차 검토 및 문장 표현 다듬기에 활용하였다.
- ChatGPT의 제안은 그대로 제출하지 않고, 실제 API 수집 결과, HDFS/Spark/Hive 실행 결과, GitHub 산출물을 기준으로 검토·수정하였다.
- 최종 코드 실행, 데이터 수집, 결과 확인, 캡처 확보 및 제출 여부 판단은 작성자가 직접 수행하였다.

- ## 최종 산출물 요약

- 검색 키워드: 20개
- YouTube 검색 결과: 600개
- 고유 YouTube 영상: 581개
- 추가 YouTube 댓글 raw: 58,787개
- HDFS raw 전체 용량: 약 120.5MB
- Spark 결과:
  - results/spark_keyword_summary.csv
  - results/spark_category_summary.csv
  - results/spark_correlation.csv
  - results/spark_comment_keyword_summary.csv

대용량 댓글 raw 원본은 GitHub에 업로드하지 않고 HDFS에 저장하였다. GitHub에는 data/sample 경로에 1,000줄 샘플만 포함하였다.
