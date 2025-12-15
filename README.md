# CI/CD Pipeline with Jenkins, SonarQube and Docker

This project demonstrates an end-to-end CI/CD pipeline built using Jenkins, GitHub Webhooks, SonarQube, and Docker.  
The primary goal is to showcase CI/CD automation and DevOps best practices rather than application complexity.

---

## 📌 Project Overview

The pipeline is designed to automatically trigger on every GitHub commit and perform the following actions:

- Pull source code from GitHub
- Run automated tests
- Perform static code analysis using SonarQube
- Enforce quality gates
- Build a Docker image
- Push the image to DockerHub
- Deploy the application using Docker

---

## 🛠️ Tech Stack

- **Version Control:** GitHub  
- **CI/CD Tool:** Jenkins  
- **Code Quality:** SonarQube  
- **Containerization:** Docker  
- **Language:** Python  
- **Webhook Tunneling:** Ngrok  

---

## 📂 Project Structure

ci-cd-jenkins-sonarqube-docker/
│
├── app/ # Application source code
├── tests/ # Test scripts
├── Jenkinsfile # Jenkins pipeline definition
├── Dockerfile # Docker image configuration
├── sonar-project.properties # SonarQube configuration
└── README.md

---

## 🔄 CI/CD Pipeline Flow

GitHub Commit
↓
GitHub Webhook
↓
Jenkins Pipeline
↓
Build & Test
↓
SonarQube Analysis (Quality Gate)
↓
Docker Image Build
↓
DockerHub Push
↓
Deployment


---

## 🎯 Purpose

This project is created as a hands-on assignment to strengthen practical knowledge of CI/CD pipelines, automation workflows, and DevOps tooling integration.

---