import streamlit as st
import os

st.set_page_config(page_title="Подарок для мамы", page_icon="❤️")

# Словари с данными
captions = {
    "childhood": ["Маленький недупленныш", "Пошел в школу...", "Мои первые рисунки, помнишь мама?", "Дурачимся с папой",
                  "Помнишь мои линейки в школу?"],
    "travels": ["Ваше первое путешествие", "Гулляем с вами на новый год", "Папа со статуей", "Родители в бане",
                "Мы в Питере", "Мама со статуей"],
    "adulthood": ["Дочь заканчивает школу", "Годовщина свадьбы, 25 лет!", "Мы вместе"]
}

music_files = {
    "Детство": "childhood.mp3",
    "Путешествия": "travels.mp3",
    "Взрослая жизнь": "adulthood.mp3"
}


def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    if not os.path.exists(path):
        st.error(f"Папка {path} не найдена!")
        return

    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not files:
        st.write("Фото пока нет.")
        return

    # Инициализация индекса
    key_name = f'idx_{folder_name}'
    if key_name not in st.session_state:
        st.session_state[key_name] = 0

    idx = st.session_state[key_name]

    # Кнопки
    c1, c2 = st.columns(2)
    if c1.button("⬅ Назад", key=f"prev_{folder_name}"):
        if idx > 0: st.session_state[key_name] -= 1
        st.rerun()
    if c2.button("➡ Вперед", key=f"next_{folder_name}"):
        if idx < len(files) - 1: st.session_state[key_name] += 1
        st.rerun()

    # Фото
    st.image(os.path.join(path, files[idx]), use_container_width=True)

    # Подпись - берем из словаря
    if folder_name in captions and idx < len(captions[folder_name]):
        st.markdown(f"### {captions[folder_name][idx]}")
    else:
        st.write("Фото без подписи")


# Меню
page = st.sidebar.radio("Выберите раздел:", ["Главная", "Детство", "Путешествия", "Взрослая жизнь"])

if page == "Главная":
    st.title("С днем рождения, Мама! ❤️")
else:
    st.title(page)
    # Музыка
    if page in music_files and os.path.exists(music_files[page]):
        st.audio(music_files[page])

    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])