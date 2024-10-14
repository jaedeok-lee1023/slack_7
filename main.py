import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』*\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n건강하고 안전한 클러스터를 위한 몇가지 협조사항 안내드립니다.\n\n"
            f"\n"
            f"\n"
            f":k체크: 클러스터 내 모든 도로의 경우 :자동차:*제한속도 30Km 미만* :no_entry_sign: \n"
            f":k체크: 심야 시간대에는 화물차량 운행이 빈번하여 *꼭! 안전운행 필수* :k느낌표: \n"
            f":k체크: 1층 출차로 램프 :화살표1: 흡연실 or 직원식당 *무단횡단 금지* :no_entry: \n"
            f":k체크: 각 층 입출차로 *램프 역주행 금지* :man-gesturing-no: \n"
            f":k체크: 입차 차단기 (1층 / 2층~7층) 주행 차로 임의 변경 금지 (사각지대로 사고 위험) :arrow_up: \n"
            f"\n"
            f"구성원 여러분들의 안전한 근무환경을 위한 협조사항 이니 꼭!! 실천 부탁드립니다.\n"
            f"\n"
            f"\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
