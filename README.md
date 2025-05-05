# M-Tech AI Project – PA2312049010064

This repository contains the source code and configuration files for the M-Tech AI project associated with student ID **PA2312049010064**.

## 📁 Project Structure

```
.
├── app/                 # Main application code
├── DockerFile           # Docker configuration file
├── requirements.txt     # Python dependencies
├── setup.py             # Package setup script
└── .gitignore           # Files and directories to ignore in Git
```

## 🚀 Getting Started

To set up and run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/RetheshnaPosina/M-tech-AI-PA2312049010064.git
   cd M-tech-AI-PA2312049010064
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   Navigate to the `app` directory and execute the main script. (Replace `main.py` with the actual entry point if different.)

   ```bash
   cd app
   python main.py
   ```

## 🐳 Docker Deployment

To build and run the application using Docker:

1. **Build the Docker image:**

   ```bash
   docker build -t mtech-ai-project .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 8000:8000 mtech-ai-project
   ```

   Adjust the port numbers as needed based on your application's configuration.


