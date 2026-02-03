# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the current directory contents into the container at /app
COPY . /app

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Make port 8000 available to the world outside this container
EXPOSE 8000

# 6. Define environment variable for GCP project
ENV GOOGLE_CLOUD_PROJECT="your-project-id"

# 7. Run the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]