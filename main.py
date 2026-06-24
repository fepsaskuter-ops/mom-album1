import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Подарок для мамы", page_icon="❤️", layout="centered")

# --- КОНФИГУРАЦИЯ ---
# ЗАМЕНИ "1.jpg", "2.jpg" на РЕАЛЬНЫЕ имена файлов из твоих папок!
captions_data = {
    "childhood": {
        "1.jpg": "Маленький недупленныш",
        "2.jpg": "Пошел в школу...",
        "3.jpg": "Мои первые рисунки, помнишь мама?"
    },
    "travels": {
        "1.jpg": "Ваше первое путешествие",
        "2.jpg": "Гулляем с вами на новый год",
        "3.jpg": "Папа со статуей"
    },
    "adulthood": {
        "1.jpg": "Дочь заканчивает школу",
        "2.jpg": "Годовщина свадьбы, 25 лет!",
        "3.jpg": "Мы вместе"
    }
}

music_files = {
    "Детство": "childhood.mp3",
    "Путешествия": "travels.mp3",
    "Взрослая жизнь": "adulthood.mp3"
}


# --- ФУНКЦИИ ---
def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    # Берем файлы в том же порядке, что и в словаре
    if folder_name not in captions_data:
        st.write("Раздел в разработке...")
        return

    files = list(captions_data[folder_name].keys())

    if not files:
        st.write("Фото пока нет.")
        return

    # Состояние
    key_name = f'idx_{folder_name}'
    if key_name not in st.session_state: st.session_state[key_name] = 0
    idx = st.session_state[key_name]

    # Навигация
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ Назад", key=f"prev_{folder_name}"):
            if idx > 0: st.session_state[key_name] -= 1
            st.rerun()
    with col2:
        if st.button("➡ Вперед", key=f"next_{folder_name}"):
            if idx < len(files) - 1: st.session_state[key_name] += 1
            st.rerun()

    # Вывод фото
    filename = files[idx]
    st.image(os.path.join(path, filename), use_container_width=True)

    # Вывод подписи
    st.markdown(f"### {captions_data[folder_name].get(filename, '')}")


# --- ИНТЕРФЕЙС ---
st.sidebar.title("Меню альбома 📸")
page = st.sidebar.radio("Выберите раздел:", ["Главная", "Детство", "Путешествия", "Взрослая жизнь"])

if page == "Главная":
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>С днем рождения, Мама! ❤️</h1>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Добро пожаловать в наш цифровой альбом</h3>", unsafe_allow_html=True)
    st.write("---")
    st.image(
        "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJ4ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6ZzB6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/l41lTjJp8A6sD7D1m/giphy.gif",
        use_container_width=True)
    st.markdown("<div style='text-align: center;'>Выбирай раздел в меню слева и давай окунемся в воспоминания!</div>",
                unsafe_allow_html=True)
else:
    st.title(page)
    # Музыка
    if page in music_files and os.path.exists(music_files[page]):
        st.audio(music_files[page])

    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])