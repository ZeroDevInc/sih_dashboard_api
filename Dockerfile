
FROM python:3.9-slim
# Using the python:3.9-slim base image

COPY requirements.txt .
# Copying the requirements.txt file from the current directory into the container

RUN pip install -r requirements.txt
# Installing the dependencies specified in requirements.txt

COPY . .
# Copying the entire current directory into the container

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]