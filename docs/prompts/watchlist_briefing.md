# Watchlist Briefing Prompt

지정한 관심종목, ETF, 테마에 대한 브리핑을 작성한다. 종목별 공시, 실적, 수급, 밸류에이션 논점, 컨센서스 변화, 관련 뉴스, 섹터 맥락을 함께 정리한다. 단순 뉴스 나열이 아니라 종목별 투자자가 다음으로 확인해야 할 포인트를 분명히 적는다.

가능하면 작업 디렉터리의 `config/watchlist_positions.yaml` 파일을 읽어 관심종목 목록과 보유 포지션 정보를 함께 반영한다. 파일에 평균단가(`avg_cost`), 보유 주수(`shares`), 통화(`currency`), 메모(`notes`)가 있으면 현재 가격과 비교해 대략적인 손익 구간, 포지션 크기, 다음 확인 포인트를 서술한다. 파일이 없거나 값이 비어 있으면 그 사실을 보고서에 짧게 명시하고, 일반 watchlist 브리핑으로 계속 진행한다.

입력값으로 다음을 받을 수 있다고 가정한다.
- 관심종목 티커/종목명 목록
- 관련 ETF 또는 비교 종목
- 집중 테마(예: HBM, 조선, 원전, AI 인프라)
- 평균단가와 보유 주수 같은 로컬 포지션 정보

출처 우선순위는 다음과 같이 둔다.
- 한국 종목 공시/실적: DART, KRX
- 미국 종목 공시/실적: SEC EDGAR, Nasdaq Earnings Calendar
- 시황 및 보조 해설: Investing.com, 한국경제
- 거시 보강: CME FedWatch, Federal Reserve

## 산출물

1. `outputs/watchlist` 디렉터리에 관심종목 브리핑을 저장한다. 파일명은 `watchlist_briefing_YYYY-MM-DD.docx` 형식으로 한다.
2. 로컬 `config/slack_channels.yaml`의 `watchlist` 채널 설정을 읽어 핵심 요약을 전송한다.
3. Slack 발송은 사용자 계정이 아닌 별도 봇 발신 구조를 사용한다. 로컬 `config/slack_bot.env`의 `SLACK_BOT_TOKEN`을 읽고 `python3 src/send_slack_message.py --channel-key watchlist --message-file <path>` 형태로 보낸다.
4. 봇 토큰 또는 채널 설정이 없으면 사용자 계정 발송으로 대체하지 말고, 설정 누락 사실을 결과에 명시하고 종료한다.

## 보고서 구성

- 종목별 핵심 이슈 요약
- 보유 포지션 맥락(평균단가, 주수, 손익 구간)
- 실적/공시/가이던스 변화
- 수급과 가격 반응
- 동종업계 비교 포인트
- 다음 확인 이벤트
- 종목별 리스크와 관전 포인트
- 출처 목록
