# 아침 증시 브리핑 봇

## 실행 일정

- 매일 오전 8시 KST에 Codex automation으로 실행
- 작업 경로: `<PROJECT_ROOT>`
- 실행 환경: local

## 리서치 범위

- 한국 증시: Investing.com, 한국경제
- 미국 증시: Investing.com, 한국경제 글로벌
- 실행 당일 최신 웹 자료를 확인하고, 접근 제한이나 지연 시세가 있으면 보고서에 명시

## 산출물

- 상세 보고서: `market_briefing_YYYY-MM-DD.docx`
- 저장 위치: 현재 작업 경로
- Slack 요약: `<SLACK_CHANNEL_NAME>` 채널

## 보고서 구성

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
- 한 줄 결론
- 한국 및 미국 핵심 이슈 3-5개
- 오늘 볼 포인트
- 생성된 DOCX 파일명
- 기본 전송 대상: 로컬 automation 설정의 `<SLACK_CHANNEL_NAME>` / `<SLACK_CHANNEL_ID>`
