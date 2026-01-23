# Use standard Python
FROM python:3.10-slim

# Install system dependenceies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Upgrade pip tooling
RUN python -m pip install -U pip setuptools wheel

# Install PaddlePaddle CPU (Linux) from the official Paddle index (stable CPU)
RUN python -m pip install paddlepaddle==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# Install PaddleOCR with the PP-StructureV3 dependency group ("doc-parser")
RUN python -m pip install -U "paddleocr[doc-parser]"

# Optional but commonly helpful:
RUN python -m pip install -U opencv-python-headless