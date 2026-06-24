import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Подарок для мамы", page_icon="❤️", layout="centered")

# 1. СЛОВАРЬ ПОДПИСЕЙ И МУЗЫКИ
# Просто отредактируй тексты внутри кавычек, если нужно
captions = {
    "childhood": [
        "Маленький недупленныш",
        "Пошел в школу...",
        "Мои первые рисунки, помнишь мама?",
        "Дурачимся с папой",
        "Помнишь мои линейки в школу?"
    ],
    "travels": [
        "Ваше первое путешествие в мир вечной любви ❤️",
        "Гулляем с вами на новый год",
        "Папа сидит со статуей, но где же мама??",
        "Мои любимые родители в бане, почему-то все в листьях...",
        "Мы в Питере, мама смотрит куда-то...",
        "А вот и мама сидит со статуей"
    ],
    "adulthood": [
        "Ваша дочь уже заканчивает школу",
        "Ваша годовщина свадьбы, уже целых 25 лет!!",
        "Мы вместе"
    ]
}

music_files = {
    "Детство": "childhood.mp3",
    "Путешествия": "travels.mp3",
    "Взрослая жизнь": "adulthood.mp3"
}


# 2. ФУНКЦИЯ ОТОБРАЖЕНИЯ ФОТО И ПОДПИСЕЙ
def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    if not os.path.exists(path):
        st.write("Фотографии скоро появятся!")
        return

    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    if not files:
        st.write("Фото пока нет.")
        return

    # Состояние для переключения фото
    if f'index_{folder_name}' not in st.session_state:
        st.session_state[f'index_{folder_name}'] = 0

    idx = st.session_state[f'index_{folder_name}']

    # Кнопки навигации
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ Назад", key=f'prev_{folder_name}'):
            if idx > 0: st.session_state[f'index_{folder_name}'] -= 1
            st.rerun()
    with col2:
        if st.button("➡ Вперед", key=f'next_{folder_name}'):
            if idx < len(files) - 1: st.session_state[f'index_{folder_name}'] += 1
            st.rerun()

    # Вывод фото
    st.image(os.path.join(path, files[idx]), use_column_width=True)

    # Вывод подписи
    if folder_name in captions and idx < len(captions[folder_name]):
        st.markdown(f"### {captions[folder_name][idx]}")


# 3. ОСНОВНОЕ МЕНЮ
st.sidebar.title("Меню альбома")
page = st.sidebar.radio("Выберите раздел:", ["Главная", "Детство", "Путешествия", "Взрослая жизнь"])

if page == "Главная":
    st.title("С днем рождения, Мама! ❤️")
    st.write("---")
    st.write(
        "Этот альбом — частичка моей любви к тебе. Выбери раздел в меню слева, чтобы посмотреть наши общие воспоминания.")
else:
    st.title(page)

    # Плеер (автоматически выбирает песню из music_files)
    if page in music_files:
        song = music_files[page]
        if os.path.exists(song):
            st.audio(song, format='audio/mp3')

    # Карта разделов
    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])