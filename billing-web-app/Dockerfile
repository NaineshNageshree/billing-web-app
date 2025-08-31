FROM python:3.11-slim

# Install system dependencies required for ReportLab + Cairo
RUN apt-get update && apt-get install -y \
    build-essential \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    pkg-config \
    libcairo2-dev \
    cmake \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements
COPY app/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY app/ /app/

EXPOSE 5000

CMD ["python", "app.py"]
