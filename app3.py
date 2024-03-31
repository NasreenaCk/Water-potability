import streamlit as st
import pickle
from PIL import Image
def main():
    st.title(':rainbow[WATER POTABILITY]')
    image = Image.open('water_potability.jpg')
    st.image(image, width=600)
    A1 = st.text_input('ph', placeholder='type here')
    A2 = st.text_input('Hardness', placeholder='type here')
    A3 = st.text_input('Solids', placeholder='type here')
    A4 = st.text_input('Chloramines', placeholder='type here')
    A5 = st.text_input('Sulfate', placeholder='type here')
    A6 = st.text_input('Conductivity', placeholder='type here')
    A7 = st.text_input('Organic_carbon', placeholder='type here')
    A8 = st.text_input('Trihalomethanes', placeholder='type here')
    A9 = st.text_input('Turbidity', placeholder='type here')

    features = [A1, A2, A3, A4, A5, A6, A7, A8, A9]
    model = pickle.load(open('mode3.sav', 'rb'))
    scaler = pickle.load(open('scaler3.sav','rb'))
    pred = st.button('PREDICT')
    if pred:
        prediction = model.predict(scaler.transform([features]))
        if prediction == 0:
            st.write('unsafe water')
        else:
            st.write('safe water')
main()
