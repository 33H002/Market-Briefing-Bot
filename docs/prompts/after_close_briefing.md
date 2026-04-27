# After-Close Briefing Prompt

매 영업일 한국 장 마감 후 장후 브리핑을 작성한다. 당일 한국 증시 마감 결과를 중심으로 미국 선물, 환율, 원자재, 주요 공시와 뉴스 흐름을 요약한다. 당일 수급, 업종, 주도주, 급등락 종목, 공시 이벤트를 확인하고 왜 움직였는지 설명한다.

출처 우선순위는 다음과 같이 둔다.
- 한국 지수/업종/수급: Investing.com, KRX, 한국경제
- 한국 공시/실적: DART
- 미국 선물/글로벌 위험선호: Investing.com 미국 지수/선물
- 환율/원자재/금리: Investing.com, CME FedWatch
- 장마감 후 핵심 뉴스: 한국경제, SEC EDGAR

## 산출물

1. `outputs/after_close` 디렉터리에 `.docx` 또는 `.md` 형태의 상세 장후 브리핑을 저장한다. 파일명은 `after_close_briefing_YYYY-MM-DD` 형식으로 한다.
2. 로컬 `config/slack_channels.yaml`의 `after_close` 채널 설정을 읽어 요약본을 전송한다.
3. Slack 발송은 사용자 계정이 아닌 별도 봇 발신 구조를 사용한다. 로컬 `config/slack_bot.env`의 `SLACK_BOT_TOKEN`을 읽고 `python3 src/send_slack_message.py --channel-key after_close --message-file <path>` 형태로 보낸다.
4. 봇 토큰 또는 채널 설정이 없으면 사용자 계정 발송으로 대체하지 말고, 설정 누락 사실을 결과에 명시하고 종료한다.

## 보고서 구성

- 오늘 시장 한 줄 요약
- 지수/수급/환율/원자재 핵심 수치
- 업종 및 테마별 강약
- 주도주/급등락 종목 체크
- 장마감 후 공시 및 실적 포인트
- 내일 장 전 체크포인트
- 출처 목록
