# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set environment variables
ENV MODEL_FILE_PATH="models/"
ENV MODEL_NAME="Llama-3.2-3B-Instruct-Q4_K_M.gguf"
ENV REPO_NAME="unsloth/Llama-3.2-3B-Instruct-GGUF"

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "model_downloader.py"]
