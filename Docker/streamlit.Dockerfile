FROM python:3.11-slim
WORKDIR /app
COPY ../requirements.txt .
COPY ../models/random_for_streamlit_model.pkl .
COPY ../src/main/python/com/bits/streamlit/streamlit_demo.py .

RUN pip install -r requirements.txt
#Streamlit port
EXPOSE 8501
CMD ["streamlit","run","streamlit_demo.py"]

# Be at below location
#C:\Users\USER\git\python\AIML-Code\ai-ml>
#docker build -f Docker/streamlit.Dockerfile -t streamlit .
# RUN container by
# docker run -p 8501:8501 streamlit