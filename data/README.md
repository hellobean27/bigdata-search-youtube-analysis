# Data Description

이 폴더는 프로젝트에서 사용하는 데이터의 출처, 수집 방법, 스키마, GitHub 업로드 정책을 설명한다.

## 1. Google Trends Data

- 출처: Google Trends
- 대상 기간: 수집일 기준 최근 30일
- 대상 지역: 대한민국
- 데이터 의미: 절대 검색량이 아닌 상대 검색 관심도
- 예상 파일 형식: CSV

예상 컬럼:

| 컬럼명 | 설명 |
|---|---|
| keyword | 검색 키워드 |
| google_interest | Google Trends 검색 관심도 |
| period | 수집 기준 기간 |
| region | 대상 지역 |

## 2. Naver DataLab Data

- 출처: Naver DataLab API
- 대상 기간: 수집일 기준 최근 30일
- 대상 지역: 대한민국
- 데이터 의미: 절대 검색량이 아닌 상대 검색 지수
- 예상 파일 형식: JSON 또는 CSV

예상 컬럼:

| 컬럼명 | 설명 |
|---|---|
| keyword | 검색 키워드 |
| naver_interest | Naver DataLab 검색 관심도 |
| period | 수집 기준 기간 |
| region | 대상 지역 |

## 3. YouTube Data

- 출처: YouTube Data API
- 수집 기준: Google Trends 및 Naver DataLab에서 선정한 키워드와 관련된 YouTube 영상
- 영상 조건: 최근 30일 이내 업로드된 영상
- 데이터 의미: 수집 시점 기준 누적 성과 지표

예상 컬럼:

| 컬럼명 | 설명 |
|---|---|
| keyword | 수집에 사용한 검색 키워드 |
| video_id | YouTube 영상 ID |
| title | 영상 제목 |
| channel_title | 채널명 |
| published_at | 영상 업로드 일시 |
| view_count | 수집 시점 기준 누적 조회수 |
| like_count | 수집 시점 기준 누적 좋아요 수 |
| comment_count | 수집 시점 기준 누적 댓글 수 |
| collected_at | 데이터 수집 일시 |
| days_since_upload | 업로드 후 경과일 |
| views_per_day | 일평균 조회수 |

## 4. 데이터 해석 주의사항

Google Trends와 Naver DataLab의 값은 실제 검색 횟수가 아니라 상대적 검색 관심도이다. 따라서 본 프로젝트에서는 검색량이라는 표현 대신 검색 관심도 또는 상대 검색 지수라는 표현을 사용한다.

YouTube 조회수는 특정 기간 동안 발생한 조회수가 아니라 수집 시점 기준 누적 조회수이다. 따라서 업로드 시점 차이를 보정하기 위해 일평균 조회수를 함께 계산한다.

## 5. GitHub 업로드 정책

대용량 raw 데이터는 GitHub에 업로드하지 않고, 샘플 데이터만 data/sample/ 폴더에 저장한다.

업로드 예정 파일:

- data/sample/google_trends_sample.csv
- data/sample/naver_datalab_sample.csv
- data/sample/youtube_video_sample.csv

대용량 원본 데이터와 처리 데이터는 .gitignore를 통해 GitHub 업로드 대상에서 제외한다.
