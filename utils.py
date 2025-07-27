import json

def get_music_list(emotion):
    with open("music_db.json", "r", encoding="utf-8") as f:
        db = json.load(f)
    return db.get(emotion, [])

def make_youtube_link(song_title):
    return f"https://www.youtube.com/results?search_query={song_title.replace(' ', '+')}"
