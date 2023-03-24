
# Use the official Python base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install the dependencies with --no-cache-dir so it wont download the flask app here  ~/.cache/pip
RUN pip install --no-cache-dir flask

# Copy the Flask app and the Utils.py file into the container
COPY Scores/MainScores.py .
COPY Utils.py .

# Copy the name.txt and Scores.txt files into the container
COPY ../name.txt .
COPY Scores/Scores.txt .
COPY Scores/Last_scores.txt .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "MainScores.py"]