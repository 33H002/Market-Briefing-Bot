# Weekly Briefing Prompt

매주 1회 한국 시간 기준으로 주간 증시 브리핑을 작성한다. 지난주 한국/미국 시장의 핵심 변화, 수급, 업종, 거시 변수, 실적 이벤트를 요약하고 이번 주 주요 일정과 시나리오를 정리한다. 단순 주간 뉴스 모음이 아니라, 무엇이 시장을 움직였는지와 이번 주 무엇을 봐야 하는지를 구조적으로 설명한다.

출처 우선순위는 다음과 같이 둔다.
- 주간 지수/업종 흐름: Investing.com, KRX
- 한국 핵심 공시/실적: DART, 한국경제
- 미국 지수/섹터/실적 일정: Investing.com, Nasdaq Earnings Calendar, SEC EDGAR
- 금리/정책 일정: CME FedWatch, Federal Reserve, BLS, BEA
- 보조 해설: 한국경제 글로벌/월스트리트나우

## 산출물

1. 현재 작업 디렉터리에 주간 상세 보고서를 저장한다. 파일명은 `weekly_market_briefing_YYYY-MM-DD.docx` 형식으로 한다.
2. 로컬 `config/slack_channels.yaml`의 `weekly` 채널 설정을 읽어 주간 요약본을 직접 전송한다. 실제 전송에는 `channel_name`과 `channel_id`를 사용한다.

## 보고서 구성

- 지난주 한 줄 결론
- 지난주 한국 시장 리뷰
- 지난주 미국 시장 리뷰
- 업종/테마 성과 요약
- 금리/환율/유가/거시 변수 리뷰
- 이번 주 캘린더
- 이번 주 핵심 시나리오 3개
- 관심 섹터 및 리스크
- 출처 목록
