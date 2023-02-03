FROM python:3.7.16-slim
COPY MainScores.py MainScores.py
EXPOSE 8777
RUN pip install flask
CMD python MainScores.py
