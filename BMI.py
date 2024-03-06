#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:55:36 2024

@author: r-ndz
"""

#Libraries importations
import streamlit as st
st.title('CREATION OF MY FIRST FORM')
st.write('This tool is a first form to calculate the body mass index based on informations filled')



#Dhe begining of the form
with st.form(key='key_BMI'):
    height=st.number_input('type your height ')
    weight=st.number_input('type your weight ')
    BMI=(height**2)/weight
    #create the button submit
    submit=st.form_submit_button('Submit')
    if submit:
        st.write('your body mass index is: '+str(BMI))
        