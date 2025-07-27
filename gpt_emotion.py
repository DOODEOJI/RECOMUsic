import os
import openai
from dotenv import load_dotenv

load_dotenv()  # .env 파일 불러오기

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_emotion_gpt(user_input):
    prompt = f"""
다음 문장에서 느껴지는 감정을 하나의 단어로 분석해줘.
가능한 감정: 행복, 슬픔, 외로움, 피곤, 설렘, 분노, 집중, 무기력

문장: "{user_input}"
감정:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": "너는 감정을 정확히 분석하는 감정 분석기야. 감정을 하나의 단어로 출력해."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,
        temperature=0.4
    )

    emotion = response["choices"][0]["message"]["content"].strip()
    return emotion
