import streamlit as st
import os

# Настройка страницы
st.set_page_config(page_title="Подарок для мамы", page_icon="❤️")

# Словарь: Название раздела -> Имя файла музыки
music_files = {
    "Детство": "childhood.mp3",
    "Путешествия": "travels.mp3",
    "Взрослая жизнь": "adulthood.mp3"
}


# Функция для отображения фото
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

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ Назад", key=f'prev_{folder_name}'):
            if idx > 0: st.session_state[f'index_{folder_name}'] -= 1
            st.rerun()
    with col2:
        if st.button("➡ Вперед", key=f'next_{folder_name}'):
            if idx < len(files) - 1: st.session_state[f'index_{folder_name}'] += 1
            st.rerun()

    st.image(os.path.join(path, files[idx]), use_column_width=True)


# --- ГЛАВНАЯ ЛОГИКА ---
st.sidebar.title("Меню альбома")
page = st.sidebar.radio("Выберите раздел:", ["Главная", "Детство", "Путешествия", "Взрослая жизнь"])

if page == "Главная":
    st.title("С днем рождения, Мама! ❤️")
    st.subheader("Этот альбом — частичка моей любви к тебе")
    st.write("Используй меню слева, чтобы окунуться в наши воспоминания.")
else:
    st.title(page)

    # Плеер
    if page in music_files:
        song = music_files[page]
        if os.path.exists(song):
            st.audio(song, format='audio/mp3')
        else:
            st.warning(f"Файл {song} не найден. Проверь, лежит ли он в корне проекта!")

    # Карта разделов
    folder_map = {"Детство": "childhood", "Путешествия": "travels", "Взрослая жизнь": "adulthood"}
    show_section(folder_map[page])