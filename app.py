import streamlit as st
from emotion_classifier import classify_emotion
from utils import get_music_list, make_youtube_link

st.set_page_config(page_title="감정 음악 추천 챗봇", page_icon="🎧")
st.title("🎧 감정 기반 음악 추천 챗봇")

user_input = st.text_input("지금 기분이나 상황을 말해보세요:")

if user_input:
    emotion = classify_emotion(user_input)
    st.success(f"분석된 감정: **{emotion}**")

    song_list = get_music_list(emotion)

    if song_list:
        st.markdown("🎵 이런 음악은 어때요?")
        for song in song_list:
            st.markdown(f"- [{song}]({make_youtube_link(song)})")
    else:
        st.warning("해당 감정에 맞는 음악이 아직 준비되지 않았어요 😢")
