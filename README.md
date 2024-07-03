# FastAPI Application Tutorial

Welcome to the FastAPI Application Tutorial repository! This codebase is designed to accompany the "Learn how to create a FastAPI application in just 5 minutes!" YouTube video tutorial.

## Overview

In this tutorial, we'll build a FastAPI application from scratch in under 5 minutes. This repository contains the source code that demonstrates how to set up a FastAPI project, create API endpoints, run a local server, and explore automatic API documentation.

## Prerequisites

Before you get started, ensure you have the following:

> Basic knowledge of Python, 
> Python 3.7+ installed on your machine, 
> macOS (though the instructions are easily adaptable for other operating systems)

## Installation

Follow these steps to get the project up and running on your local machine:

### 1. Clone the repository:
```
git clone https://github.com/itstechelites/fastapi.git
cd fastapi-tutorial
```

### 2. Create and activate a virtual environment:
```
python3 -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### 3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Running the Application
To run the FastAPI application locally:

### 1. Start the FastAPI server:
```
uvicorn main:app --reload
```

### 2. Access the API:

Open your browser and navigate to http://127.0.0.1:8000 to see the running application.

### 3. Explore the automatic API documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Project Structure

## The repository structure is as follows:
```
fastapi-tutorial/
├── main.py             # The main application file
├── requirements.txt    # List of dependencies
└── README.md           # This file
```

## Useful Links

FastAPI Documentation
Uvicorn Documentation
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

