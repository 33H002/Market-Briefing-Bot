# Market Briefing Platform

한국/미국 증시 관련 주요 이슈를 리서치해 상세 `.docx` 보고서를 만들고, Slack으로 요약본을 보내기 위한 Codex automation 플랫폼입니다. 아침 브리핑뿐 아니라 장후 브리핑, 주간 브리핑, 관심종목 브리핑까지 같은 구조에서 운영할 수 있도록 구성합니다.

## 구성

- `src/generate_market_briefing.py`: 샘플 보고서 레이아웃 생성 스크립트
- `docs/market_briefing_bot.md`: 전체 브리핑 플랫폼 운영 요약
- `docs/automation_prompt.md`: 아침 브리핑용 기본 프롬프트
- `docs/prompts/morning_briefing.md`: 아침 브리핑 프롬프트
- `docs/prompts/after_close_briefing.md`: 장후 브리핑 프롬프트
- `docs/prompts/weekly_briefing.md`: 주간 브리핑 프롬프트
- `docs/prompts/watchlist_briefing.md`: 관심종목 브리핑 프롬프트
- `docs/prompts/watchlist_event_alert.md`: 관심종목 이벤트 알림 프롬프트
- `docs/roadmap.md`: 추가 추천 자동화 아이디어
- `config/watchlist_positions.example.yaml`: 관심종목/보유 포지션 예시 파일
- `config/slack_channels.example.yaml`: 브리핑 유형별 Slack 채널 매핑 예시 파일
- `docs/slack_summary_sample_2026-04-26.md`: Slack 발송 샘플
- `samples/market_briefing_2026-04-26.docx`: 2026-04-26 수동 실행 샘플 산출물
- `requirements.txt`: 로컬 실행에 필요한 Python 패키지

## 지원 브리핑

- 아침 브리핑: 장 시작 전 핵심 시황, 금리, 실적, 리스크 정리
- 장후 브리핑: 당일 수급, 업종, 주도주, 이벤트 리뷰
- 주간 브리핑: 지난주 리뷰와 이번 주 캘린더, 핵심 시나리오
- 관심종목 브리핑: 지정 종목·ETF·테마에 대한 공시/실적/이벤트 중심 업데이트
- 관심종목 이벤트 알림: 보유/관심 종목의 공시, 실적, 급등락 발생 시 짧은 Slack 알림

## 실행 방식

Codex automation은 브리핑 유형별로 별도 등록해 운영할 수 있습니다. 로컬 Mac이 켜져 있고 Codex/Slack 연결이 유지되어야 합니다.

수동으로 샘플 보고서를 다시 생성하려면 프로젝트 루트에서 아래 명령을 실행합니다.

```bash
python3 src/generate_market_briefing.py
```

실행하면 현재 경로에 `market_briefing_YYYY-MM-DD.docx` 형식의 샘플 보고서가 생성됩니다.

## 데이터 출처

기본 출처는 다음과 같습니다.

- 한국 증시 시황: Investing.com, 한국경제
- 한국 1차 데이터/공시: KRX, DART
- 미국 증시 시황: Investing.com, 한국경제 글로벌/월스트리트나우
- 미국 이벤트/금리 기대: CME FedWatch, Nasdaq Earnings Calendar
- 미국 1차 공시/매크로 일정: SEC EDGAR, Federal Reserve, BLS, BEA

실제 automation 실행 시에는 실행 당일 최신 웹 데이터를 확인하고, 접근 제한이나 지연 시세는 보고서에 명시합니다. 시황 해설은 Investing.com/한국경제를, 공시와 공식 수치 확인은 KRX·DART·SEC EDGAR·미국 공식 발표기관을 우선 사용합니다. `src/generate_market_briefing.py`는 레이아웃과 문서 포맷을 참고하기 위한 샘플 산출기이며, 실제 자동화 본문은 프롬프트에 따라 매일 새로 작성됩니다.

## Slack

브리핑 유형별로 Slack 채널을 분리해 운영하는 것을 기본으로 합니다. 각 automation은 자신의 브리핑 유형에 맞는 채널 키를 선택해야 하며, 실제 채널명과 채널 ID는 로컬 `config/slack_channels.yaml`에서만 관리하는 것을 권장합니다.

## 추천 운영 방식

- 아침 브리핑: 평일 오전 8시 KST
- 장후 브리핑: 평일 오후 4시 30분 KST
- 주간 브리핑: 매주 월요일 오전 7시 30분 KST
- 관심종목 브리핑: 수동 실행 또는 별도 watchlist 조건 기반 자동화
- 관심종목 이벤트 알림: 장중/장후 수시 실행 또는 조건 기반 자동화

권장 채널 분리 예시는 다음과 같습니다.

- `morning`: 아침 브리핑 전용 채널
- `after_close`: 장후 브리핑 전용 채널
- `weekly`: 주간 브리핑 전용 채널
- `watchlist`: 관심종목 브리핑 전용 채널
- `watchlist_alert`: 관심종목 이벤트 알림 전용 채널, 없으면 `watchlist` 채널 사용

## 관심종목 설정

관심종목 브리핑은 로컬 `config/watchlist_positions.yaml` 파일을 읽어 보유 종목, 평균단가, 주수, 메모를 함께 반영할 수 있게 설계합니다. 공개 저장소에는 예시 파일만 두고 실제 보유 수량/평단가는 커밋하지 않는 것을 권장합니다.

Slack 채널도 같은 방식으로 로컬 `config/slack_channels.yaml` 파일을 사용합니다. 저장소에는 `config/slack_channels.example.yaml`만 유지하고 실제 채널 정보는 커밋하지 않는 것을 권장합니다.

## 주의

이 프로젝트의 산출물은 시장 정보 브리핑이며 특정 종목 또는 자산의 매수/매도 권유가 아닙니다.
