# Google·Naver 검색 관심도와 YouTube 영상 성과 지표의 관계 분석

## 1. 프로젝트 개요

본 프로젝트는 2026년 4월 Google Trends와 Naver DataLab의 검색 관심도 데이터를 기반으로, 검색 관심도가 높은 키워드가 YouTube 영상 성과 지표와 어떤 관계를 가지는지 분석한다.

YouTube 영상 성과 지표는 수집 시점 기준 누적 조회수, 좋아요 수, 댓글 수, 영상 개수 등을 사용한다.

## 2. 문제 정의

사람들은 특정 이슈나 키워드에 관심이 생기면 Google이나 Naver에서 검색하고, 동시에 YouTube에서 관련 영상을 소비한다. 그러나 검색 관심도가 높은 키워드가 YouTube에서도 높은 조회수나 반응으로 이어지는지는 명확하지 않다.

따라서 본 프로젝트는 검색 관심도와 YouTube 영상 성과 지표 사이의 관계를 분석하여, 검색 기반 관심과 영상 소비 사이의 연관성을 탐색한다.

## 3. 분석 질문

1. Google Trends 검색 관심도가 높은 키워드일수록 관련 YouTube 영상의 조회수가 높은가?
2. Naver DataLab 검색 관심도가 높은 키워드일수록 관련 YouTube 영상의 조회수가 높은가?
3. 검색 관심도와 YouTube 좋아요 수, 댓글 수 사이에도 관계가 있는가?
4. 검색 관심도가 높은 키워드에서 100만 조회수 이상 영상 비율이 더 높게 나타나는가?

## 4. 데이터 수집 계획

### Google Trends
- 대상 기간: 2026년 4월
- 수집 항목: 키워드별 검색 관심도
- 해석: 절대 검색량이 아닌 상대 검색 관심도

### Naver DataLab
- 대상 기간: 2026년 4월
- 수집 항목: 키워드별 검색 관심도
- 해석: 절대 검색량이 아닌 상대 검색 지수

### YouTube Data API
- 수집 항목: 영상 제목, 채널명, 업로드일, 조회수, 좋아요 수, 댓글 수
- 주의: 조회수는 2026년 4월 한 달 조회수가 아니라 수집 시점 기준 누적 조회수

## 5. 기술 스택

- 데이터 수집: Python, Google Trends CSV, Naver DataLab API, YouTube Data API
- 저장: HDFS
- 전처리: Apache Spark
- 분석: Spark SQL, HiveQL
- 시각화: Matplotlib
- 버전 관리: GitHub

## 6. 데이터 파이프라인

Google Trends / Naver DataLab 데이터 수집  
→ YouTube 영상 메타데이터 수집  
→ raw JSON/CSV 저장  
→ HDFS 업로드  
→ Spark 전처리  
→ Hive 테이블 생성  
→ 상관관계 분석 및 시각화

## 7. 예상 결과

Google과 Naver의 검색 관심도 지표를 각각 YouTube 영상 성과 지표와 비교하여, 검색 관심도와 영상 소비 지표 사이의 관계를 분석한다.

## 8. 한계

Google Trends와 Naver DataLab의 값은 절대 검색량이 아니라 상대적 검색 관심도이다. 또한 YouTube API로 수집하는 조회수는 수집 시점 기준 누적 조회수이므로, 특정 기간 동안 발생한 조회수로 해석하지 않는다.

## 9. AI Tool Usage

- ChatGPT: 프로젝트 주제 구체화, README 구조 검토, 분석 질문 설계 보조
