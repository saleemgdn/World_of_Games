FROM python:3.7.16-slim
COPY MainScores.py MainScores.py
EXPOSE 8777
RUN pip install -r requirements.txt
CMD python MainScores.py
