import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction'],
        icons=['house','book'],
        styles={
            "container":{"background-color":"#e2ac3f"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#924f1b",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#e2ac3f"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#DE3163;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE MINE DETECTION SYSTEM </p>',unsafe_allow_html=True)
    st.markdown(' <p class="paragraph"> This system about predicting SONAR rocks against Mines with the help of Machine Learning. SONAR is an abbreviated form of Sound Navigation and Ranging. It uses sound waves to detect objects underwater. Machine learning-based tactics, and deep learning-based approaches have applications in detecting sonar signals and hence targets.Fourier transform, wavelet transform, limit cycle, etc. are signal processing methods applicable for an underwater acoustic signal. Machine Learning enables the processing of sonar signals and target detection. It is a subfield of artificial intelligence which tells machines how to manipulate data more proficiently.  </p>',
    unsafe_allow_html=True)

    

if selected=='Prediction':

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('rockmine.sav','rb'))

    def rockmine_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'Mine is Detected'
        else:
            return 'Detection of Rock'
    def main(): 


        st.markdown("<h1 style='text-align: center; color: #D80000   ;'>MINE DETECTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,=st.columns(2)


        with co1:
            freq1=st.number_input('Enter Frequency Value for Frequency 1',format='%f')
            freq2=st.number_input('Enter Frequency Value for Frequency 2',format='%f')
            freq3=st.number_input('Enter Frequency Value for Frequency 3',format='%f')
            freq4=st.number_input('Enter Frequency Value for Frequency 4',format='%f')

        with col2:
            freq5=st.number_input('Enter Frequency Value for Frequency 5',format='%f')
            freq6=st.number_input('Enter Frequency Value for Frequency 6',format='%f')
            freq7=st.number_input('Enter Frequency Value for Frequency 7',format='%f')
            freq8=st.number_input('Enter Frequency Value for Frequency 8',format='%f')

            

        #code for the prediction 
        diagnosis=''
        #creating a button for prediction 
        if st.button('Prediction Result'):
            diagnosis = rockmine_prediction([freq1,freq2,freq3,freq4,freq5,freq6,freq7,freq8])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()










