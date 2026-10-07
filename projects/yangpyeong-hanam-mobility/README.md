# 양평군 → 하남시 광역 생활이동 분석

2026년 「AI와 함께하는 교통문제 해결을 위한 데이터 분석 공모전」 분석을 재현하기 위한 코드와 요약 입력자료입니다.

## 분석 목적

양평군 12개 읍·면에서 하남시로 이동하는 생활이동을 분석해

1. 출발 읍·면별 이동량 집중도
2. 핵심 OD(출발지-도착지) 축
3. 이동목적 구성
4. 차량 의존 및 이동부담
5. 대중교통 전환 5%·10%·20% 정책 시나리오

를 계산합니다.

## 핵심 결과

- 전체 생활이동: 398,524건
- 양서면·양평읍·서종면: 262,010건, 전체의 65.75%
- 확인된 핵심 8개 OD: 151,872건, 전체의 38.11%
- 차량 이동 비중: 98.76%
- 평균 차량 이동거리: 24.009km
- 평균 차량 이동시간: 67.47분
- 주간 차량 이동거리: 약 1,499,543 vehicle-km
- 차량 이동 5% 전환 시: 주간 약 74,977 vehicle-km 감소

## 폴더 구조

```
yangpyeong-hanam-mobility/
├─ README.md
├─ requirements.txt
├─ data/
│  ├─ README.md
│  ├─ origin_totals.csv
│  ├─ key_od.csv
│  ├─ purpose_totals.csv
│  └─ policy_inputs.csv
└─ src/
   └─ analyze_mobility.py
```

## 실행

```bash
cd projects/yangpyeong-hanam-mobility
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/analyze_mobility.py
```

실행 후 `outputs/` 아래에 재계산된 CSV와 PNG 그래프가 생성됩니다.

## 데이터 범위 주의

- 398,524건의 OD·목적 분석은 2026년 6월 기준 분석값
- 차량수단·거리·시간 효과 계산은 2026-08-24~2026-08-30 기간 분석값

서로 다른 기간의 데이터를 같은 개별 이동으로 직접 결합하지 않고, 생활이동 구조와 차량 의존 특성을 별도 지표로 사용합니다.

## 재현성

이 저장소에는 공모전 보고서에 사용한 **집계 입력값**을 포함합니다. 원 API 응답 JSON 및 원본 ZIP 데이터는 용량·배포 조건 때문에 포함하지 않았습니다. 원본을 보유한 경우 동일한 집계 기준으로 CSV를 갱신한 뒤 코드를 재실행할 수 있습니다.
