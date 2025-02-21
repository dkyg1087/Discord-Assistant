# Start from the NVIDIA CUDA runtime image
FROM nvidia/cuda:12.5.1-runtime-ubuntu22.04

# Set environment variables to prevent prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install Python 3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121 && \
    pip3 install fastapi[standard]

WORKDIR /app
COPY . /app

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app:app"]