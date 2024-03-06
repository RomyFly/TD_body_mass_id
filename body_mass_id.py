import streamlit as st
import pandas as pd
import sqlite3
with sqlite3.connect('bmi') as connection:
    cur = connection.cursor()
    
#define the function to insert data in sqlite
def insert_into(nom, age, taille, poids, imc):
  try:
    sql = "INSERT INTO Patients (patient_names, patient_ages, patient_height, patient_weight, patient_bmi ) VALUES (?, ?, ?, ?, ?)"
    value = (nom, age, taille, poids, imc)
    cur.execute(sql, value)
    connection.commit()
  except sqlite3.Error as error:
    st.write("Erreur lors de l'insertion dans la table person", error)


st.title('CREATION OF MY FIRST FORM')
st.write('This tool is a first form to calculate the body mass index based on informations filled')



#Dhe begining of the form
with st.form('body mass index form', clear_on_submit=True):
    name = st.text_input('insert your name')
    Age = st.number_input('type your age ')
    height = st.number_input('type your height ')
    weight = st.number_input('type your weight ')
    #create the button submit
    submit = st.form_submit_button()
if submit:
    BMI= weight/(height**2)
    insert_into(name, Age,height, weight, BMI)
df=pd.read_sql_query("SELECT * FROM Patients", connection)
st.dataframe(df)

