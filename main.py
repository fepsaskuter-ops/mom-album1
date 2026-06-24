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
        font-size: 1.2em;
    }
    </style>
    """, unsafe_allow_html=True)

# Твои подписи
captions_list = {
    "childhood": ["Ваша первая дочка Викуська", "Я со своей любимой сестрой", "Пошел в садик,совсем недавно как будто было..", "Маленький невдупленыш",
                  "А тут я уже пошел в школу,это я помню..", "Мои первые рисунки, помнишь мама?", "Дурачимся с папой)", "Мои линейки в школу,помнишь мама?"],
    "travels": ["Ваше первое путешествие в мир бесконечной любви", "Гуляем с вами на новый год,мои любимые родители", "Папа со статуей,а где же мама?..", "Вы в бане,в каких то листьях..",
                "Мы в Питере,наше путешствие с вами)", "Мама со статуей,теперь понятно где она была.."],
    "adulthood": ["Ваша дочь заканчивает школу,помнишь мама?", "Годовщина свадьбы, 25 лет вместе!",]
}


def show_section(folder_name):
    path = os.path.join("photos", folder_name)
    # Сортируем по алфавиту
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


# --- МЕНЮ ---
menu = ["Главная", "Детство", "Путешествия", "Взрослая жизнь"]
page = st.sidebar.radio("Навигация:", menu)

if page == "Главная":
    st.markdown("<h1 class='main-title'>С днем рождения, Мама! ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>Добро пожаловать в наш альбом теплых воспоминаний</p>", unsafe_allow_html=True)
    st.write("---")
    st.info("Выбери раздел в меню слева, чтобы начать наше путешествие во времени!")
else:
    st.title(page)
    music_map = {"Детство": "childhood.mp3", "Путешествия": "travels.mp3", "Взрослая жизнь": "adulthood.mp3"}
    if page in music_map and os.path.exists(music_map[page]):
        st.audio(music_map[page])

    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])