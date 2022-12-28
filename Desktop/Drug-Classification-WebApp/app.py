import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))

st.title('Drug Classification WebApp')
st.sidebar.header('Drug Data')
image = Image.open('drug.jpg')
st.image(image, '')

# FUNCTION
def user_report():
  Age = st.sidebar.slider('Age of the patient', 0,100, 1 )
  Sex = st.sidebar.slider('Sex - F(0) M(1)', 0,1, 1 )
  BloodP = st.sidebar.slider('BP - High(0) Low(1) Normal(2)', 0,2, 1 )
  Cholesterol = st.sidebar.slider('Cholesterol High(0) Normal(1)', 0,1, 1 )
  Na_to_k = st.sidebar.number_input('Sodium to Potassium Ration')

  user_report_data = {
      'Age':Age,
      'Sex':Sex,
      'BP':BloodP,
      'Cholesterol':Cholesterol,
      'Na_to_k':Na_to_k,
  }
  report_data = pd.DataFrame(user_report_data, index=[0])
  return report_data

user_data = user_report()
st.header('Drug Data')
st.write(user_data)

Drug = model.predict(user_data)
dictionary_drug_type={
    0:"DrugY",
    1:"DrugA",
    2:"DrugB",
    3:"DrugC",
    4:"DrugX"
}
st.header('Probable Drug Type:')
for i in dictionary_drug_type:
    if Drug==i:
        st.subheader(str(dictionary_drug_type[i]))
