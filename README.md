M-Tech AI Project – PA2312049010064
This repository contains the source code and configuration files for the M-Tech AI project associated with student ID PA2312049010064.

📁 Project Structure

.
├── app/                 # Main application code
├── DockerFile           # Docker configuration file
├── requirements.txt     # Python dependencies
├── setup.py             # Package setup script
└── .gitignore           # Files and directories to ignore in Git

🚀 Getting Started
To set up and run the project locally, follow these steps:

Clone the repository:
git clone https://github.com/RetheshnaPosina/M-tech-AI-PA2312049010064.git
cd M-tech-AI-PA2312049010064

Install the required dependencies:
pip install -r requirements.txt

Run the application:
Navigate to the app directory and execute the main script. (Replace main.py with the actual entry point if different.)
cd app
python main.py

🐳 Docker Deployment
To build and run the application using Docker:

Build the Docker image:
docker build -t mtech-ai-project .

Run the Docker container:
docker run -p 8000:8000 mtech-ai-project

Adjust the port numbers as needed based on your application's configuration.
