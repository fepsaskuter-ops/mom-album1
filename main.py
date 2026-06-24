import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Подарок для мамы", page_icon="❤️", layout="centered")

# --- СТИЛИ (КРАСИВЫЙ ФОН) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }
    .main-title {
        color: #D63384;
        text-align: center;
        font-size: 3em;
        font-family: 'Arial', sans-serif;
    }
    .sub-title {
        color: #555;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Твои подписи
captions_list = {
    "childhood": ["Маленький недупленныш", "Пошел в школу...", "Мои первые рисунки, помнишь мама?", "Дурачимся с папой",
                  "Помнишь мои линейки в школу?"],
    "travels": ["Ваше первое путешествие", "Гулляем с вами на новый год", "Папа со статуей", "Родители в бане",
                "Мы в Питере", "Мама со статуей"],
    "adulthood": ["Дочь заканчивает школу", "Годовщина свадьбы, 25 лет!", "Мы вместе"]
}


def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not files:
        st.write("Фото скоро будут здесь!")
        return

    if f'idx_{folder_name}' not in st.session_state: st.session_state[f'idx_{folder_name}'] = 0
    idx = st.session_state[f'idx_{folder_name}']

    col1, col2 = st.columns([1, 1])
    if col1.button("⬅ Назад", key=f"prev_{folder_name}"):
        if idx > 0: st.session_state[f'idx_{folder_name}'] -= 1
        st.rerun()
    if col2.button("➡ Вперед", key=f"next_{folder_name}"):
        if idx < len(files) - 1: st.session_state[f'idx_{folder_name}'] += 1
        st.rerun()

    st.image(os.path.join(path, files[idx]), use_container_width=True)

    if folder_name in captions_list and idx < len(captions_list[folder_name]):
        st.markdown(f"<h3 style='text-align: center; color: #333;'>{captions_list[folder_name][idx]}</h3>",
                    unsafe_allow_html=True)


# --- МЕНЮ И ЛОГИКА ---
menu = ["Главная", "Детство", "Путешествия", "Взрослая жизнь"]
page = st.sidebar.radio("Навигация:", menu)

if page == "Главная":
    st.markdown("<h1 class='main-title'>С днем рождения, Мама! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Добро пожаловать в наш альбом теплых воспоминаний</p>", unsafe_allow_html=True)
    st.write("---")
    # Добавляем еще больше радости
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTjJp8A6sD7D1m/giphy.gif")
    st.info("Выбери раздел в меню слева, чтобы начать наше путешествие во времени!")
else:
    st.title(page)
    music_map = {"Детство": "childhood.mp3", "Путешествия": "travels.mp3", "Взрослая жизнь": "adulthood.mp3"}
    if page in music_map and os.path.exists(music_map[page]):
        st.audio(music_map[page])

    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])