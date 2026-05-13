# Data Description

이 폴더는 프로젝트에서 사용하는 데이터의 출처, 수집 방법, 스키마를 설명한다.

## 1. Google Trends Data

- 출처: Google Trends
- 대상 기간: 2026년 4월
- 데이터 의미: 절대 검색량이 아닌 상대 검색 관심도
- 예상 파일 형식: CSV

## 2. Naver DataLab Data

- 출처: Naver DataLab API
- 대상 기간: 2026년 4월
- 데이터 의미: 절대 검색량이 아닌 상대 검색 지수
- 예상 파일 형식: JSON 또는 CSV

## 3. YouTube Data

- 출처: YouTube Data API
- 수집 항목: video_id, title, channel_title, published_at, view_count, like_count, comment_count
- 주의: view_count는 수집 시점 기준 누적 조회수이다.

## 4. GitHub 업로드 정책

대용량 raw 데이터는 GitHub에 업로드하지 않고, 샘플 데이터만 data/sample/ 폴더에 저장한다.
