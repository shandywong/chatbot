README.txt — Graduate Employment Chatbot
Overview

The Graduate Employment Chatbot is a professional AI-powered assistant designed to provide text-based insights into employment trends, graduate job statistics, and career guidance for fresh graduates. This chatbot relies entirely on text input and output, making it lightweight and accessible via a web interface. It leverages OpenAI’s GPT API for natural language understanding and is integrated with custom datasets for accurate local employment information.

The primary goal of the chatbot is to assist graduates, career advisors, and HR professionals in understanding employment trends, career prospects, and industry-specific statistics in Malaysia.

How the Chatbot Was Created

Project Setup

The project is structured in Python using FastAPI for the backend API.

Frontend is built with HTML, CSS, and JavaScript (including AJAX calls for seamless interaction with the backend).

Python virtual environment (.venv) is used to manage dependencies.

Data Integration

Historical employment data and other relevant statistics are stored in Excel files (cleaned_chatbot_data.xlsx).

These datasets include metrics such as employment rate, job trends by qualification, and industry-specific data.

AI Integration

The chatbot uses OpenAI’s GPT API for natural language processing.

Custom Python scripts (llm.py) handle communication with the API and process user inputs to provide accurate responses.

Fallback responses are provided when user queries do not match the dataset or metrics.

Visualization Features

For questions involving trends or numbers, the chatbot can generate visualizations using Python plotting libraries (e.g., matplotlib, plotly).

These plots can be returned as images or embedded in the web interface.

Web Interface

Users interact with the chatbot through a simple web page (index.html) that connects to the FastAPI backend.

Real-time responses are handled via AJAX calls, ensuring smooth user experience.

How to Use the Chatbot

Running Locally

Activate your Python virtual environment:

.\.venv311\Scripts\Activate


Install required packages:

pip install -r requirements.txt


Run the FastAPI server:

uvicorn app.main:app --reload


Open the web interface in your browser at: http://127.0.0.1:8000/docs or your custom index.html.

Using the Chatbot

Type your question in the input box on the web interface.

The chatbot responds in text, providing information, statistics, and advice based on the query.

Example queries:

“Show employment rate trend for diploma graduates since 2016.”

“What are the top job sectors for fresh graduates in Malaysia?”

“Provide insights on IT and data science career opportunities.”

Advanced Features

The chatbot can generate trend plots if the question involves temporal or numeric data.

It supports fallback responses for unmatched queries, ensuring every user gets a response.

Capabilities of the Chatbot

Employment Data Insights

Provides historical trends in employment for diploma, degree, and other qualifications.

Supports industry-specific insights, e.g., technology, healthcare, or manufacturing.

Career Guidance

Recommends in-demand job sectors and roles.

Provides advice based on economic and labor trends.

Data Visualization

Generates plots for trends such as employment rates, graduate placement, or industry growth.

Can embed charts as images for easier interpretation.

Natural Language Understanding

Handles conversational queries intelligently using GPT API.

Interprets different ways of asking the same question and responds consistently.

Fallback and Error Handling

If a query does not match the dataset or metrics, the chatbot provides general employment guidance instead of failing.