# OPENAI_API_KEYの環境変数を読み込む
from dotenv import load_dotenv
load_dotenv()

# 必要なライブラリをインポート
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.5
)

# streamlitを用いてアプリを作成
import streamlit as st

# Webアプリのタイトルと説明を表示
st.title("お家相談アプリ")
st.write("このアプリは、クライアントの建てたい家のイメージを具体化するための質問を生成したり、法律的な問題をお伝えします。")
st.write("以下のフォームにクライアントから聞き出した家のイメージを入力してください。")

# 画面に入力フォームを1つ用意
input_message = st.text_input("家のイメージを入力してください。", "例：2階建て、3LDK、庭付き、和風")

# ラジオボタンでLLMに振る舞わせる専門家の種類を選択
expertise = st.radio(
    "専門家を選択してください。",
    ("家のイメージ具体化", "法律相談")
)

# 各専門家ごとに、LLMに渡すシステムメッセージを変更
if expertise == "家のイメージ具体化":
    messages = [
        SystemMessage(content="あなたは優秀な建築コンサルタントです。ユーザーが建てたい家のイメージを聞いて、より具体的なイメージを持たせるための質問を生成ください。"),
        HumanMessage(content=input_message)
    ]
else:
    messages = [
        SystemMessage(content="あなたは優秀な建築関係の法律に詳しい弁護士です。ユーザーが建てたい家のイメージを聞いて、法律的な問題点を指摘してください。"),
        HumanMessage(content=input_message)
    ]

# ボタンが押されたら、LLMに質問を投げて、回答を表示
if st.button("実行"):
    result = llm(messages)
    st.write(result.content)
