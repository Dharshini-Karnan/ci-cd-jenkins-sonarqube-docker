# CI/CD Pipeline with Jenkins, SonarQube & Docker

This project demonstrates an end-to-end CI/CD pipeline using **Jenkins**, **SonarQube**, and **Docker**, triggered automatically through **GitHub Webhooks**.  
The focus of this project is on **CI/CD automation and DevOps best practices**, not application complexity.

---

## 📌 Project Objective

- Automate build, test, code quality analysis, and containerization
- Integrate multiple DevOps tools into a single pipeline
- Implement a real-world CI/CD workflow using webhook triggers
- Automatically build and push Docker images to DockerHub

---

## 🛠️ Tech Stack

- **Version Control:** GitHub  
- **CI/CD Tool:** Jenkins  
- **Code Quality:** SonarQube  
- **Containerization:** Docker, DockerHub  
- **Programming Language:** Python  
- **Webhook Tunneling:** Ngrok  

---

## ✅ Prerequisites

### GitHub
- Repository created
- Webhook configured to Jenkins (via Ngrok)

### Jenkins
- Jenkins installed and running
- Required plugins installed:
  - Git
  - Pipeline
  - GitHub Integration
  - SonarQube Scanner
  - Credentials Binding

### SonarQube
- SonarQube server running locally
- Project created in SonarQube
- Authentication token added to Jenkins credentials

### Docker
- Docker Desktop installed and running
- Docker CLI accessible from Jenkins
- DockerHub account and repository created

### Ngrok
- Ngrok installed and authenticated
- Used to expose local Jenkins to GitHub for webhook triggering

### System
- Python 3.12 installed
- Internet access for pulling Docker base images

---

## 🔄 CI/CD Pipeline Flow

1. GitHub Commit  
2. GitHub Webhook (Ngrok)  
3. Jenkins Pipeline Trigger  
4. Automated Tests  
5. SonarQube Code Analysis  
6. Docker Image Build  
7. DockerHub Image Push  
8. Application Deployment using Docker  

---

## ⚙️ Pipeline Stages

- Source Code Checkout
- Run Python Unit Tests
- SonarQube Static Code Analysis
- Docker Image Build
- Push Image to DockerHub
- Run Application Container

---

🔗 Repository Links

GitHub Repository:
https://github.com/Dharshini-Karnan/ci-cd-jenkins-sonarqube-docker

DockerHub Repository:
https://hub.docker.com/r/dharshinikarnan/ci-cd-python-app

🎯 Outcome

Fully automated CI/CD pipeline

Real-time static code quality analysis

Dockerized application delivery

Hands-on experience with industry-standard DevOps tools

📝 Notes

Jenkins security was kept minimal for local development

Ngrok was used to enable webhook communication with GitHub

Quality Gate enforcement can be enabled or skipped as required

---

## 🚀 Deployment

The Docker image is deployed using Docker and can be run locally or on an EC2 instance.

```bash
docker run -d -p 5000:5000 dharshinikarnan/ci-cd-python-app:latest



