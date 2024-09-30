import streamlit as st
import pickle

# Run code streamlit run streamlit_demo.py
# Be at ai-ml dir
# streamlit run .\src\main\python\com\bits\streamlit\streamlit_demo.py
# streamlit run .\src\main\python\com\bits\streamlit\streamlit_demo.py
# http://localhost:8501/

with open('models/random_for_streamlit_model.pkl', 'rb') as f :
    model = pickle.load(f);

st.title("My Streamlit Application")
number = st.slider("Pick a number", 0, 100)
sl = st.slider("Sepal Length(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
pl = st.slider("Petal Length(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
sw = st.slider("Sepal Width(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
pw = st.slider("Petal width(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)

if st.button('Predict'):
    input_data = [[sl,pl,sw,pw]]
    pridiction =  model.predict(input_data)
    #pridiction = 'Versicolur'

    st.write(f"The pridicted species is: {pridiction}")
