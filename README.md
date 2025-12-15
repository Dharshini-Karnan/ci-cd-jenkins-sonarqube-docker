CI/CD Pipeline with Jenkins, SonarQube & Docker

This project demonstrates an end-to-end CI/CD pipeline using Jenkins, SonarQube, and Docker, triggered automatically via GitHub Webhooks.
The focus of this project is on CI/CD automation and DevOps best practices, not application complexity.

📌 Project Objective

Automate build, test, code quality analysis, and containerization

Integrate multiple DevOps tools in a single pipeline

Implement real-world CI/CD workflow with webhook triggering

Push Docker images automatically to DockerHub

🛠️ Tech Stack

Version Control: GitHub

CI/CD Tool: Jenkins

Code Quality: SonarQube

Containerization: Docker & DockerHub

Programming Language: Python

Webhook Tunneling: Ngrok

✅ Prerequisites

Before running this pipeline, ensure the following are configured:

GitHub

Repository created

Webhook configured to Jenkins (via Ngrok)

Jenkins

Jenkins installed and running

Required plugins:

Git

Pipeline

GitHub Integration

SonarQube Scanner

Credentials Binding

SonarQube

SonarQube server running locally

Project created

Authentication token added to Jenkins credentials

Docker

Docker Desktop installed and running

Docker CLI accessible from Jenkins

DockerHub account and repository created

Ngrok

Installed and authenticated

Used to expose local Jenkins to GitHub

System

Python 3.12 installed

Internet access for pulling Docker base images

🔄 CI/CD Pipeline Flow
GitHub Commit
      ↓
GitHub Webhook (Ngrok)
      ↓
Jenkins Pipeline Trigger
      ↓
Automated Tests
      ↓
SonarQube Code Analysis
      ↓
Docker Image Build
      ↓
DockerHub Image Push
      ↓
Application Deployment via Docker

⚙️ Pipeline Stages

Source Code Checkout

Run Python Unit Tests

SonarQube Static Code Analysis

Docker Image Build

Push Image to DockerHub

Run Application Container

🚀 Deployment

The Docker image is deployed using Docker and can be run locally or on an EC2 instance.

docker run -d -p 5000:5000 dharshinikarnan/ci-cd-python-app:latest

📂 Repository Links

GitHub Repository:
https://github.com/Dharshini-Karnan/ci-cd-jenkins-sonarqube-docker

DockerHub Repository:
https://hub.docker.com/r/dharshinikarnan/ci-cd-python-app

🎯 Outcome

Fully automated CI/CD pipeline

Real-time code quality checks

Dockerized application delivery

Hands-on experience with industry-standard DevOps tools

📝 Note

Jenkins security was kept minimal for local development.

Ngrok was used to enable webhook communication with GitHub.

Quality Gate enforcement can be optionally enabled or skipped.