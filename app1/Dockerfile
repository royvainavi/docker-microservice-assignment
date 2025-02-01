FROM python:3.8-slim
WORKDIR /app
COPY app1.py .
RUN pip install flask requests
EXPOSE 6000
CMD ["python", "app1.py"]
