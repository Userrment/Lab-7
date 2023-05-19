import streamlit as st
import pandas as pd
import first_func
import second_func
import third_func

df = pd.read_csv('titanic.csv')

st.title("Лабораторная работа 7\nКоманда: Дударев А., Петров Д., Ережепов О.")

choice_list: list[int] = [1, 2, 3]
choice: int = st.selectbox("Выберите номер задания: ", choice_list)
choice = 1

if choice == 1: first_func.avg_price_output(df)
if choice == 2: second_func.avg_age_output(df)
if choice == 3: third_func.gender_count_output(df)

