import numpy as np 
import pickle 
import streamlit as st 
import warnings
warnings.filterwarnings("ignore")

# loading the saved model
loaded_model = pickle.load(open('trained_adb_model.sav', 'rb'))

# create function for prediction
def sleep_disorder_prediction(input_data):
    input_data_as_np_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction) 
    if (prediction[0] == 0):
        return 'the person is not at a risk of sleep disorder'
    else:
        return 'the person is at a risk of sleep disorder'
        
# function for risk calculation
def percentage_of_risk(input_data):
    input_data_as_np_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_np_array.reshape(1,-1)
    pred = loaded_model.predict_proba(input_data_reshaped)
    risk = pred[:,1]
    risk_percent = round(risk[0]*100, 2)
    print(risk_percent)
    return str(risk_percent)
    
    
    
# UI

def main():
    
    st.set_page_config(page_title='Sleep Disorder', page_icon=':zzz:', layout='wide')
    st.title(':sleeping: Sleep Disorder Prediction')
    gender = st.selectbox('gender', ['Male', 'Female'])
    age = st.text_input('age')
    occupation = st.selectbox('occupation', ['Other', 'Doctor', 'Teacher', 'Nurse', 'Engineer', 'Accountant', 'Lawyer', 'Salesperson'])
    sleepDuration = st.text_input('sleep duration')
    quality = st.text_input('quality of sleep')
    physical = st.text_input('physical activity level')
    stress = st.text_input('stress level')
    bmi = st.selectbox('bmi category', ['Overweight', 'Normal', 'Obese'])
    heartrate = st.text_input('heart rate')
    steps = st.text_input('daily step count')
    bp_lower = st.text_input('bp lower')
    bp_upper = st.text_input('bp upper')
    
    # label encoding gender feature 
    if (gender == 'Male'):
        gender_encoded = 1
    elif (gender == 'Female'):
        gender_encoded = 0
    
    # label encoding gender occupation
    if (occupation == 'Accountant'):
        occupation_encoded = 0
    elif (occupation == 'Doctor'):
        occupation_encoded = 1
    elif (occupation == 'Engineer'):
        occupation_encoded = 2
    elif (occupation == 'Lawyer'):
        occupation_encoded = 3
    elif (occupation == 'Nurse'):
        occupation_encoded = 4
    elif (occupation == 'Other'):
        occupation_encoded = 5
    elif (occupation == 'Salesperson'):
        occupation_encoded = 6
    elif (occupation == 'Teacher'):
        occupation_encoded = 7
        
    # label encoding gender occupation
    if (bmi == 'Overweight'):
        bmi_encoded = 2
    elif (bmi == 'Normal'):
        bmi_encoded = 0
    elif (bmi == 'Obese'):
        bmi_encoded = 1
        
        
    input_features = [gender_encoded, age, occupation_encoded, sleepDuration, quality, physical, stress, bmi_encoded, heartrate, steps, bp_upper, bp_lower]
    
    diagnosis = ''
    risk_calculation = ''
    
    if st.button('risk prediction'):
        diagnosis = sleep_disorder_prediction(input_features)
    st.write(diagnosis)
    
    if st.button('risk calculation'):
        risk_calculation = percentage_of_risk(input_features)
    st.write(risk_calculation)
    
    
    
if __name__ == '__main__':
    main()