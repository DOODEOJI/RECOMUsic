from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 모델 불러오기 (최초 1회 다운로드, 이후 캐시됨)
tokenizer = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")
model = AutoModelForSequenceClassification.from_pretrained("beomi/KcELECTRA-base", num_labels=3)

# label 맵핑 (이건 사전 실험 기반, 실제 프로젝트에선 조정 가능)
label_map = {
    0: "부정",
    1: "중립",
    2: "긍정"
}

def classify_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    label = label_map[predicted_class]

    # 감정 → 음악 감정으로 변환 예시
    if label == "긍정":
        return "행복"
    elif label == "부정":
        return "슬픔"
    else:
        return "집중"
