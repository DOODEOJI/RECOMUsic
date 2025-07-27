def classify_emotion(text):
    text = text.lower()
    if "우울" in text or "지쳐" in text or "힘들" in text:
        return "슬픔"
    elif "신나" in text or "기뻐" in text or "좋아" in text:
        return "행복"
    elif "집중" in text or "공부" in text or "몰입" in text:
        return "집중"
    elif "외로" in text or "혼자" in text:
        return "외로움"
    else:
        return "행복"  # 기본값
