import streamlit as st
import pandas as pd
import first_func
import second_func
import third_func

df = pd.read_csv('titanic.csv')

st.title("Лабораторная работа 7\nКоманда: Дударев А., Петров Д., Ережепов О.")

choice: int = int(st.selectbox("Выберите номер задания: ", [1, 2, 3]))

if choice != None:
    match choice:
        case 1:
            first_func.avg_price_output(df)
        case 2:
            second_func.avg_age_output(df)
        case 3:
            third_func.gender_count_output(df)
else:
    pass
