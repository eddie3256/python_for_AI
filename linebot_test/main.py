from flask import Flask, request, abort
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import google.generativeai as genai
import os
load_dotenv()

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ["CHANNEL_SECRET"])
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])

@app.route("/")
def index():
    return "<h1>LineBot的webhook的程式</h1>"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    genai.configure(api_key=os.environ["Gemini_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(event.message.text)
    message = TextSendMessage(text=response.txt)
    line_bot_api.reply_message(event.reply_token, message)