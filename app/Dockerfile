# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port (FastAPI runs on 8000)
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]