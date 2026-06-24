import streamlit as st
import os

st.set_page_config(page_title="Подарок для мамы", page_icon="❤️")

# Твои подписи по порядку (как они лежат в папках)
captions_list = {
    "childhood": ["Маленький недупленныш", "Пошел в школу...", "Мои первые рисунки, помнишь мама?", "Дурачимся с папой",
                  "Помнишь мои линейки в школу?"],
    "travels": ["Ваше первое путешествие", "Гулляем с вами на новый год", "Папа со статуей", "Родители в бане",
                "Мы в Питере", "Мама со статуей"],
    "adulthood": ["Дочь заканчивает школу", "Годовщина свадьбы, 25 лет!", "Мы вместе"]
}


def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    # Берем файлы, сортируем их по алфавиту (как они обычно лежат в Windows)
    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not files:
        st.write("Фото пока нет.")
        return

    # Состояние индекса
    key_name = f'idx_{folder_name}'
    if key_name not in st.session_state: st.session_state[key_name] = 0
    idx = st.session_state[key_name]

    # Кнопки
    c1, c2 = st.columns(2)
    if c1.button("⬅ Назад", key=f"prev_{folder_name}"):
        if idx > 0: st.session_state[key_name] -= 1
        st.rerun()
    if c2.button("➡ Вперед", key=f"next_{folder_name}"):
        if idx < len(files) - 1: st.session_state[key_name] += 1
        st.rerun()

    # Вывод фото
    st.image(os.path.join(path, files[idx]), use_container_width=True)

    # Вывод подписи из списка (если она есть)
    if folder_name in captions_list and idx < len(captions_list[folder_name]):
        st.markdown(f"### {captions_list[folder_name][idx]}")


# Меню
st.sidebar.title("Меню альбома 📸")
page = st.sidebar.radio("Выберите раздел:", ["Главная", "Детство", "Путешествия", "Взрослая жизнь"])

if page == "Главная":
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>С днем рождения, Мама! ❤️</h1>",
                unsafe_allow_html=True)
else:
    st.title(page)
    # Музыка
    music_map = {"Детство": "childhood.mp3", "Путешествия": "travels.mp3", "Взрослая жизнь": "adulthood.mp3"}
    if page in music_map and os.path.exists(music_map[page]):
        st.audio(music_map[page])

    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])