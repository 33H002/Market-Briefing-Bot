# 시장 브리핑 플랫폼

## 운영 프로필

- 아침 브리핑: 평일 오전 8시 KST
- 장후 브리핑: 평일 오후 4시 30분 KST
- 주간 브리핑: 매주 월요일 오전 7시 30분 KST
- 관심종목 브리핑: 수동 실행 또는 별도 watchlist 기반 자동화
- 관심종목 이벤트 알림: 장중/장후 수시 실행 또는 별도 조건 기반 자동화

## 실행 환경

- 작업 경로: `<PROJECT_ROOT>`
- 실행 환경: local

## 리서치 범위

- 한국 증시 시황: Investing.com, 한국경제
- 한국 1차 데이터/공시: KRX, DART
- 미국 증시 시황: Investing.com, 한국경제 글로벌
- 미국 금리/실적 이벤트: CME FedWatch, Nasdaq Earnings Calendar
- 미국 1차 공시/매크로 일정: SEC EDGAR, Federal Reserve, BLS, BEA
- 실행 당일 최신 웹 자료를 확인하고, 접근 제한이나 지연 시세가 있으면 보고서에 명시

## 산출물

- 아침 보고서: `market_briefing_YYYY-MM-DD.docx`
- 장후 보고서: `after_close_briefing_YYYY-MM-DD.docx` 또는 `.md`
- 주간 보고서: `weekly_market_briefing_YYYY-MM-DD.docx`
- 관심종목 보고서: `watchlist_briefing_YYYY-MM-DD.docx`
- 관심종목 이벤트 알림: Slack 단문 알림
- 저장 위치: 현재 작업 경로
- Slack 요약 채널: 브리핑 유형별 분리

## 프롬프트 파일

- 아침 브리핑: `docs/prompts/morning_briefing.md`
- 장후 브리핑: `docs/prompts/after_close_briefing.md`
- 주간 브리핑: `docs/prompts/weekly_briefing.md`
- 관심종목 브리핑: `docs/prompts/watchlist_briefing.md`
- 관심종목 이벤트 알림: `docs/prompts/watchlist_event_alert.md`

## 로컬 설정 파일

- 관심종목/보유 포지션: `config/watchlist_positions.yaml`
- 공개용 예시: `config/watchlist_positions.example.yaml`
- Slack 채널 매핑: `config/slack_channels.yaml`
- 공개용 예시: `config/slack_channels.example.yaml`

## Slack 채널 키

- `morning`: 아침 브리핑
- `after_close`: 장후 브리핑
- `weekly`: 주간 브리핑
- `watchlist`: 관심종목 브리핑
- `watchlist_alert`: 관심종목 이벤트 알림, 없으면 `watchlist` 채널 fallback

## 공통 보고서 구성

- 표지 및 메타데이터
- Executive Summary
- 한국 증시 핵심 흐름
- 미국 증시 핵심 흐름
- 업종 및 테마별 이슈
- 매크로, 금리, 환율, 원자재 체크
- 오늘 주목할 일정과 리스크
- 투자자가 볼 체크포인트
- 출처 목록

## Slack 요약 형식

- 날짜
- 한 줄 결론 또는 한 주 결론
- 한국 및 미국 핵심 이슈 3-5개
- 오늘 볼 포인트
- 생성된 보고서 파일명
- 기본 전송 대상: 브리핑 유형별 로컬 `config/slack_channels.yaml`의 `channel_name` / `channel_id`
