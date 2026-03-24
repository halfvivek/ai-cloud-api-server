# AI Cloud Server (EC2 + Nginx + Python)

This project is a simple AI-like API server hosted on AWS EC2.

## Features
- Handles user requests via HTTP
- Routes requests based on input
- Integrates external APIs (jokes API)
- Runs behind Nginx reverse proxy

## Tech Stack
- AWS EC2
- Nginx
- Python (http.server)
- REST API

## Example Endpoints

/ask?question=tell me a joke  
/ask?question=what is the time  

## Architecture

User → Internet → EC2 → Nginx → Python API → Response

## Learning Outcome
- Cloud deployment
- API building
- Reverse proxy setup
- External API integration
