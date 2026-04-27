# Morning Briefing Prompt

매일 아침 한국 시간 기준으로 한국/미국 증시 브리핑을 작성한다. 최신 날짜의 접근 가능한 기사와 시장 데이터를 확인하고, 출처 링크와 확인 시각을 포함한다. 접근 제한, 유료벽, 차단, 지연 시세 등으로 직접 확인이 어려운 항목은 그 제한을 보고서에 명시한다.

출처 우선순위는 다음과 같이 둔다.
- 한국 증시 시황/지수 흐름: Investing.com 한국 시장 페이지, 한국경제
- 한국 1차 데이터/공시: KRX, DART
- 미국 증시 시황/주요 뉴스: Investing.com 미국/글로벌 시장 페이지, 한국경제 글로벌
- 미국 금리 기대: CME FedWatch
- 미국 실적 일정: Nasdaq Earnings Calendar
- 미국 1차 공시: SEC EDGAR
- 미국 매크로/정책 일정: Federal Reserve, BLS, BEA

시황 해설은 뉴스/시장 페이지를 써도 되지만, 핵심 수치·실적 일정·공시·정책 일정은 가능한 한 공식/1차 소스로 교차 확인한다. 한국 대형주 실적/공시는 DART를 우선 보고, 한국 시장 제도/시장 데이터는 KRX를 우선 본다. 미국 개별 기업의 실적/이벤트는 Nasdaq Earnings Calendar와 SEC EDGAR를 우선 보고, 금리 이벤트는 CME FedWatch와 Federal Reserve 일정을 함께 본다.

## 산출물

1. 현재 작업 디렉터리에 `.docx` 상세 보고서를 저장한다. 파일명은 `market_briefing_YYYY-MM-DD.docx` 형식으로 한다.
2. 로컬 `config/slack_channels.yaml`의 `morning` 채널 설정을 읽어 요약본을 전송한다.
3. Slack 발송은 사용자 계정이 아닌 별도 봇 발신 구조를 사용한다. 로컬 `config/slack_bot.env`의 `SLACK_BOT_TOKEN`을 읽고 `python3 src/send_slack_message.py --channel-key morning --message-file <path>` 형태로 보낸다.
4. 봇 토큰 또는 채널 설정이 없으면 사용자 계정 발송으로 대체하지 말고, 설정 누락 사실을 결과에 명시하고 종료한다.

## 보고서 구성

- 표지/메타데이터
- Executive Summary
- 한국 증시 핵심 흐름
- 미국 증시 핵심 흐름
- 업종/테마별 이슈
- 매크로/금리/환율/원자재 체크
- 오늘 주목할 일정과 리스크
- 투자자가 볼 체크포인트
- 출처 목록
