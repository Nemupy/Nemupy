import random
import schedule
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# ==== .env読み込み ====
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
POST_URL = 'https://api.twitter.com/2/tweets'

# ==== 投稿生成 ====
def generate_post():
    front = ''.join(random.choices(['ま', 'す', 'か', 'る', 'の', 'ゆ', 'あ'], k=7))
    back = ''.join(random.choices(['ふ', 'る'], k=5))
    return f"{front} {back}"

# ==== 投稿処理 ====
def post_to_x():
    tweet = generate_post()
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"text": tweet}
    response = requests.post(POST_URL, headers=headers, json=payload)
    if response.status_code == 201:
        print(f"[{datetime.utcnow()}] ✅ 投稿成功: {tweet}")
    else:
        print(f"[{datetime.utcnow()}] ⚠️ 投稿失敗: {response.status_code} - {response.text}")

# ==== スケジュール設定 ====
schedule.every(90).minutes.do(post_to_x)

# ==== 実行ループ ====
while True:
    schedule.run_pending()
    time.sleep(30)
