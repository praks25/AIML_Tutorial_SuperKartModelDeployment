# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy backend files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
