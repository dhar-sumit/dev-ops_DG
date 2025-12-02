# DevOps CI/CD Pipeline - Calculator App

## Overview
This project demonstrates a complete **CI/CD pipeline** for a Python-based Calculator Application using **Jenkins** and **Docker**. The pipeline automates the process of code integration, building, testing, packaging, and reporting build status.  

The pipeline ensures consistency, reliability, and faster delivery by using isolated Docker environments and structured Jenkins pipelines.

---

## Features
- Automated **build, test, and packaging** using Jenkins.
- **Docker-based isolated environment** for consistent builds.
- **Webhook integration** with GitHub for automatic triggers.
- Detailed **build status reporting** (Success / Failure).
- Python packaging of application artifacts (`.whl` and `.tar.gz`).
- **AWS CloudFormation** integration using **SAM** template.

---

## Architecture

```text
          ┌───────────────────────────┐
          │     GitHub Repository     │
          │   (Source Code + Tests)   │
          └─────────────┬─────────────┘
                        │
                [Webhook Trigger]
                        │
                        v
          ┌───────────────────────────┐
          │      Jenkins Server       │
          │ (Pipeline Orchestrator)   │
          └─────────────┬─────────────┘
                        │
                        v
          ┌────────────────────────────┐
          │      Jenkins Pipeline      │
          │  (Defined in Jenkinsfile)  │
          └─────────────┬──────────────┘
                        │
                        v
   ┌───────────────────────────────────────────────────┐
   │   Checkout   |    Build    |   Test   |  Package  │
   ├──────────────┼─────────────┼──────────┼───────────┤
   │ Pull latest  │ Build Docker│ Run Unit │ Create    │
   │ code from    │ image of    │ Tests in │ Python    │
   │ GitHub       │ app         │ container│ Packages  │
   │              │             │          │ (.whl,    │
   │              │             │          │ .tar.gz)  │
   └───────────────────────────────────────────────────┘
                        │
                        v
          ┌───────────────────────────┐
          │       Docker Engine       │
          │ (Isolated Runtime Env)    │
          └─────────────┬─────────────┘
                        │
                        v
          ┌─────────────────────────────┐
          │      Build Status Report    │
          │  (SUCCESS ✅ / FAILURE ❌) │
          └─────────────────────────────┘
````

---

## Prerequisites

1. **Windows OS**
2. **Java (JDK 17+)**
3. **Docker Desktop**
4. **Jenkins**
5. **Git**
6. **Python 3.13+**
7. **ngrok** (optional, for exposing Jenkins externally)
8. **AWS (Basics)**

---

## Steps to Run

1. **Push Code to GitHub Repository**

   * Any commit triggers the Jenkins pipeline via webhook.

2. **Jenkins Pipeline Execution**

   * Checkout code
   * Build Docker image for `calculator-app`
   * Run unit tests inside Docker container
   * Package Python artifacts (`.whl`, `.tar.gz`)

3. **View Build Status**

   * Check the Jenkins **Dashboard** for SUCCESS or FAILURE.
   * Use **Console Output** to debug errors if build fails.

4. **Docker Environment**

   * Ensures isolated and consistent builds across different systems.

---

## Notes

* Docker ensures **environment consistency**.
* Python packaging allows **reusable artifacts** for future deployment.
* Pipeline is modular and can be extended for additional stages like **Deployment**, **Code Quality**, or **Notifications**.

---

## Author

**Sumit Dhar**
DataGrokr Software Development Intern
[GitHub](https://github.com/dhar-sumit) | [Email](mailto:sumiths.0015@example.com)
