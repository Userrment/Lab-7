import streamlit as st
import pandas as pd
import first_func
import second_func
import third_func

df = pd.read_csv('titanic.csv')

st.title("Лабораторная работа 7\nКоманда: Дударев А., Петров Д., Ережепов О.")

choice: int = int(st.selectbox("Выберите номер задания: ", [1, 2, 3]))
