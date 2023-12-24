# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /usr/scr/app/
WORKDIR /usr/scr/app/

# Copy the current directory contents into the container at /usr/scr/app/
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the Django application
EXPOSE 8000

# Set execute permissions for entrypoint.sh
RUN chmod +x entrypoint.sh

# Run the entrypoint.sh script when the container starts
CMD ["./entrypoint.sh"]
