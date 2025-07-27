import openai

openai.api_key = ""  # 여기에 API 키 입력하거나 .env로 따로 관리 가능

def classify_emotion_gpt(user_input):
    prompt = f"""
다음 문장에서 느껴지는 감정을 '하나의 단어'로 출력해줘. 예시는 이래:

예:
"오늘 날씨 진짜 좋고 기분 좋아!" → 행복
"하루 종일 너무 피곤하고 힘들어" → 피곤
"외롭고 쓸쓸해" → 외로움

문장: "{user_input}"
감정:
    """.strip()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "너는 감정을 분석하는 챗봇이야."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10,
        temperature=0.3
    )

    emotion = response['choices'][0]['message']['content'].strip()
    return emotion
