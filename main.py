import streamlit as st
import os

st.set_page_config(page_title="Подарок для мамы", page_icon="❤️", layout="centered")

# Стили для глубокого фона и кнопок
st.markdown("""
    <style>
    .stApp { background-color: #4c0519; }
    .stMarkdown, p, div, h1, h2, h3 { color: #fdf2f8 !important; }
    .centered-text { text-align: center; font-weight: bold; font-size: 24px; color: #ffcbd1; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #fda4af;'>❤️ Любимой мамочке ❤️</h1>", unsafe_allow_html=True)

captions_list = {
    "childhood": ["Ваша первая дочь)", "Я со своей сестренкой, когда только родился", "Я пошел в детский сад",
                  "Маленький невдупленыш", "Пошел в школу...", "Мои первые рисунки, помнишь мама?", "Дурачимся с папой",
                  "Помнишь мои линейки в школу?"],
    "travels": ["Ваше первое путешествие в мир вечной любви ❤", "Гуляем с вами на новый год",
                "Папа сидит со статуей, но где же мама??", "Мои любимые родители в бане, почему-то все в листьях..",
                "Мы в Питере, мама смотрит куда-то..", "А вот и мама сидит со статуей)"],
    "adulthood": ["Ваша дочь уже заканчивает школу", "Ваша годовщина свадьбы, уже целых 25 лет!!", "Мы вместе"]
}

sections = {"✨ Детство": "childhood", "✈️ Путешествия": "travels", "🏡 Взрослое время": "adulthood"}
tabs = st.tabs(list(sections.keys()))


def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    files = sorted([f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not files:
        st.write("Тут пока пусто...")
        return

    # Создаем уникальный ключ для памяти этой папки
    if f"index_{folder_name}" not in st.session_state:
        st.session_state[f"index_{folder_name}"] = 0

    idx = st.session_state[f"index_{folder_name}"]

    # Кнопки "Нырнуть в воспоминания"
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Нырнуть назад", key=f"prev_{folder_name}"):
            if idx > 0: st.session_state[f"index_{folder_name}"] -= 1
    with col2:
        if st.button("➡️ Нырнуть вперед", key=f"next_{folder_name}"):
            if idx < len(files) - 1: st.session_state[f"index_{folder_name}"] += 1

    # Фото
    st.image(os.path.join(path, files[idx]), width=500)

    # Скрытая подпись (появляется только под текущим фото)
    folder_captions = captions_list.get(folder_name, [])
    if idx < len(folder_captions):
        st.markdown(f'<div class="centered-text">{folder_captions[idx]}</div>', unsafe_allow_html=True)


for i, (name, folder) in enumerate(sections.items()):
    with tabs[i]:
        show_section(folder)