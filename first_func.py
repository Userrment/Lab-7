import streamlit as st
import pandas as pd

def avg_price(choice: int, df: pd.DataFrame) -> float:
    return df.query(f'Survived == {choice}')['Fare'].mean()

def avg_price_output(df: pd.DataFrame) -> None:
    choice_list: list[str] = ["Не спасшиеся пассажиры", "Выжившие пассажиры"]
    is_alive = st.selectbox("Выберите категорию пассажиров", choice_list)

    text: str = "Средняя цена билета по категории — "
    choice: int
    
    if is_alive == "Не спасшиеся пассажиры":
        text += f"\"{choice_list[0]}\""
        choice = 0
    elif is_alive == "Выжившие пассажиры":
        text += f"\"{choice_list[1]}\""
        choice = 1
    
    st.write(f"{text}: {round(avg_price(choice, df), 4)}")
