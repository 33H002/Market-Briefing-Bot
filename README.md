# Morning Market Briefing Bot

한국/미국 증시 관련 주요 이슈를 리서치해 상세 `.docx` 보고서를 만들고, Slack으로 요약본을 보내기 위한 Codex automation 프로젝트입니다.

## 구성

- `src/generate_market_briefing.py`: 샘플 보고서 레이아웃 생성 스크립트
- `docs/market_briefing_bot.md`: 자동화 실행 조건과 산출물 요약
- `docs/automation_prompt.md`: Codex automation에 등록한 프롬프트
- `docs/slack_summary_sample_2026-04-26.md`: Slack 발송 샘플
- `samples/market_briefing_2026-04-26.docx`: 2026-04-26 수동 실행 샘플 산출물
- `requirements.txt`: 로컬 실행에 필요한 Python 패키지

## 실행 방식

Codex automation은 매일 오전 8시 KST에 실행되도록 등록할 수 있습니다. 로컬 Mac이 켜져 있고 Codex/Slack 연결이 유지되어야 합니다.

수동으로 샘플 보고서를 다시 생성하려면 프로젝트 루트에서 아래 명령을 실행합니다.

```bash
python3 src/generate_market_briefing.py
```

실행하면 현재 경로에 `market_briefing_YYYY-MM-DD.docx` 형식의 샘플 보고서가 생성됩니다.

## 데이터 출처

기본 출처는 다음과 같습니다.

- 한국 증시: Investing.com, 한국경제
- 미국 증시: Investing.com, 한국경제 글로벌/월스트리트나우

실제 automation 실행 시에는 실행 당일 최신 웹 데이터를 확인하고, 접근 제한이나 지연 시세는 보고서에 명시합니다. `src/generate_market_briefing.py`는 레이아웃과 문서 포맷을 참고하기 위한 샘플 산출기이며, 실제 자동화 본문은 프롬프트에 따라 매일 새로 작성됩니다.

## Slack

기본 설정은 사용자가 지정한 Slack 채널로 요약본을 전송하는 것입니다. 공개 저장소에는 실제 채널명이나 채널 ID를 남기지 말고, 로컬 automation 설정에서만 관리하는 것을 권장합니다.

## 주의

이 프로젝트의 산출물은 시장 정보 브리핑이며 특정 종목 또는 자산의 매수/매도 권유가 아닙니다.
