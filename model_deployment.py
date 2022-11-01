# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/rusba/ML_Rainfall_Prediction/trained_LR_RF_final_model.sav', 'rb'))


# creating a function for Prediction

def rainfall_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'It will not rain tommorrow'
    else:
      return 'It will rain tommorrow'
  
    
  
def main():
    
    
    # giving a title
    st.title('Rainfall Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Location = st.text_input('Enter Location')
    Rainfall = st.text_input('Rainfall')
    Evaporation= st.text_input('Evaporation')
    Sunshine	 = st.text_input('Sunshine')
    WindGustDir = st.text_input('Enter Wind gust direction')
    WindGustSpeed = st.text_input(' Enter WindGustSpeed')
    WindDir9am = st.text_input('Enter Wind Direction at 9 am')
    WindDir3pm = st.text_input(' Enter Wind Direction at 3 pm')
    WindSpeed9am=st.text_input('Enter Wind speed at 9 am')
    WindSpeed3pm=st.text_input('Wind speed at 3 pm')
    Humidity3pm = st.text_input('Enter Humidity at 3pm')
    Humidity9am = st.text_input(' Enter Humidity at 9am')
    Pressure9am = st.text_input(' Enter Pressure at 9am')
    Pressure3pm	= st.text_input(' Enter Pressure at 3pm')
    Cloud9am	 = st.text_input('Enter Cloud at 9am')
    Cloud3pm =st.text_input('Cloud at 3pm')
    RainToday=st.text_input('Rain Today')
    
    loc=st.sidebar.selectbox("Encoded location value",['Adelaide : 1', 'Albany : 2', 'Albury : 3', 'AliceSprings : 4', 'BadgerysCreek : 5',	'Ballarat : 6', 	
            'Bendigo : 7', 'Brisbane : 8', 'Cairns : 9','Canberra : 10',	'Cobar : 11',	'CoffsHarbour : 12',	'Dartmoor : 13',	
            'Darwin : 14', 'GoldCoast : 15', 'Hobart : 16', 'Katherine : 17',	'Launceston : 18',	'Melbourne : 19',	'MelbourneAirport : 20',
            'Mildura : 21', 'Moree : 22',	'MountGambier : 23',	'MountGinini : 24',	'Newcastle : 25', 'Nhil : 26', 'NorahHead : 27', 	'NorfolkIsland : 28',	'Nuriootpa : 29',	
            'PearceRAAF : 30', 'Penrith : 31', 'Perth : 32', 'PerthAirport : 33', 'Portland : 34', 'Richmond : 35', 'Sale : 36', 'SalmonGums : 37',	'Sydney : 38', 
            'SydneyAirport : 39', 'Townsville : 40', 'Tuggeranong : 41',	'Uluru : 42', 'WaggaWagga : 43', 'Walpole : 44', 'Watsonia : 45', 
            'Williamtown : 46', 'Witchcliffe : 47', 'Wollongong : 48',	'Woomera : 49'])
    windgustdir=st.sidebar.selectbox("encoded windgusdirection  value",['NNW:0', 'NW:1', 'WNW:2', 'N:3', 'W:4', 'WSW:5', 'NNE:6', 'S:7', 'SSW:8', 'SW:9', 'SSE:10',
       'NE:11', 'SE:12', 'ESE:13', 'ENE:14', 'E:15'])
    winddir9am =st.sidebar.selectbox("encoded winddirection at 9 am",['NNW : 0', 'N : 1', 'NW : 2', 'NNE : 3', 'WNW : 4', 'W : 5', 'WSW : 6', 'SW : 7', 'SSW : 8', 'NE : 9', 'S : 10',
       'SSE : 11', 'ENE : 12', 'SE : 13', 'ESE : 14', 'E : 15'])
    winddir3pm =st.sidebar.selectbox("encoded winddirection at 3pm",['NW : 0', 'NNW : 1', 'N : 2', 'WNW : 3', 'W : 4', 'NNE : 5', 'WSW : 6', 'SSW : 7', 'S : 8', 'SW : 9', 'SE : 10',
       'NE : 11', 'SSE : 12', 'ENE : 13', 'E : 14', 'ESE : 15'])
    



    # code for Prediction
    Rain_prediction= ''
    
    # creating a button for Prediction
    
    if st.button('rainfall prediction Result'):
        Rain_prediction = rainfall_prediction([Location,Rainfall,Evaporation,Sunshine,WindGustDir,WindGustSpeed,WindDir9am,WindDir3pm,WindSpeed9am,WindSpeed3pm,Humidity3pm,Humidity9am,Pressure9am,Pressure3pm,Cloud9am,Cloud3pm,RainToday])
        
        
    st.success(Rain_prediction)
    
    
    
    
    
if __name__ == '__main__':
    main()


