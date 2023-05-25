import streamlit as st
import pandas as pd


def gender_count(choice: int, df: pd.DataFrame):
    return df.query(f'Pclass == {choice}').groupby('Sex')['Sex'].count()


def gender_count_output(df: pd.DataFrame) -> None:
    choice_list: list[str] = ["Класс 1", "Класс 2", "Класс 3"]
    pass_class = st.selectbox("Выберите категорию пассажиров", choice_list)

    text: str = "Количество пассажиров по классам — "
    choice: int

    if pass_class == "Класс 1":
        text += f"\"{choice_list[0]}\""
        choice = 1
    elif pass_class == "Класс 2":
        text += f"\"{choice_list[1]}\""
        choice = 2
    elif pass_class == "Класс 3":
        text += f"\"{choice_list[2]}\""
        choice = 3

    df_slice = gender_count(choice, df)

    st.write(f"{text}:")

    for col_name, item in df_slice.items():
        gender: str

        if col_name == "female":
            gender = "Женщины"
        elif col_name == "male":
            gender = "Мужчины"

        st.write(f"{gender} — {item}")
