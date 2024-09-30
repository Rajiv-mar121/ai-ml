import streamlit as st

# Run code streamlit run streamlit_demo.py
# http://localhost:8501/
st.title("My Streamlit Application")
number = st.slider("Pick a number", 0, 100)
sl = st.slider("Sepal Length(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
pl = st.slider("Petal Length(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
sw = st.slider("Sepal Width(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)
pw = st.slider("Petal width(cm)", min_value=4.0, max_value=8.0, value=5.0, step=0.1)

if st.button('Predict'):
    input_data = [[sl,pl,sw,pw]]
    #pridict = model.
    pridiction = 'Versicolur'

    st.write(f"The pridicted species is: {pridiction}")
