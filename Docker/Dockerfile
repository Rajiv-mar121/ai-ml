FROM python:3.9-slim
WORKDIR /app
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY ../com/bits/random-forest.py .
#COPY best_model.pkl .
CMD ["python", "random-forest.py"]