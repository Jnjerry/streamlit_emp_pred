import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import pickle


app_mode = st.sidebar.selectbox('Select Page',['Home','Predict_Churn'])

if app_mode=='Home':
    st.title('Employee Prediction')
    st.markdown('Dataset :')
    df=pd.read_csv('emp_analytics.csv')
    st.write(df.head())


elif app_mode == 'Predict_Churn':

    st.subheader('Fill in employee details to get prediction ')
    st.sidebar.header("Other details :")
    prop = {'salary_low': 1, 'salary_high': 2, 'salary_medium': 3}
    satisfaction_level = st.number_input("satisfaction_level", min_value=0.0, max_value=1.0)
    average_montly_hours = st.number_input("average_montly_hours")
    promotion_last_5year = st.number_input("promotion_last_5year")
    salary = st.sidebar.radio("Select Salary ",tuple(prop.keys()))

    salary_low,salary_medium,salary_high=0,0,0
    if salary == 'High':
        salary_high = 1
    elif salary == 'Low':
        salary_low = 1
    else :salary_medium = 1


    subdata={
        'satisfaction_level':satisfaction_level,
        'average_montly_hours ':average_montly_hours ,
        'promotion_last_5year':   promotion_last_5year,
        'salary':[salary_low,salary_medium,salary_high],
        }

    features = [satisfaction_level, average_montly_hours, promotion_last_5year, subdata['salary'][0],subdata['salary'][1], subdata['salary'][2]]

    results = np.array(features).reshape(1, -1)

    if st.button("Predict"):

        picklefile = open("emp-model.pkl", "rb")
        model = pickle.load(picklefile)

        prediction = model.predict(results)
        if prediction[0] == 0:
            st.success('Employee will not churn')
        elif prediction[0] == 1:
            st.error( 'Employee will churn')

