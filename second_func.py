import streamlit as st
import pandas as pd

def avg_age(choice: int, df: pd.DataFrame) -> float:
    return df.query(f'Pclass == {choice}')['Age'].mean()

def avg_age_output(df: pd.DataFrame) -> None:
    choice_list: list[str] = ["Класс 1", "Класс 2", "Класс 3"]
    pass_class = st.selectbox("Выберите категорию пассажиров", choice_list)

    text: str = "Средний возраст по классам пассажиров — "
    choice: int

    match pass_class:
        case "Класс 1":
            text += f"\"{choice_list[0]}\""
            choice = 1
        case "Класс 2":
            text += f"\"{choice_list[1]}\""
            choice = 2
        case "Класс 3":
            text += f"\"{choice_list[2]}\""
            choice = 3
    
    st.write(f"{text}: {round(avg_age(choice, df), 4)}")