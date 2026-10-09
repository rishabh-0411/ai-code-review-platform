# AI Code Review Platform

An AI-powered code review platform that analyzes GitHub repositories and generates structured code quality feedback using Google's Gemini API.

## Overview

The AI Code Review Platform automates the initial stages of code review by cloning a GitHub repository, analyzing its structure, identifying relevant source files, and using a generative AI model to produce actionable review feedback.

Built with **FastAPI, React, and Google's Gemini API**, the platform provides a web interface for submitting repositories and viewing their analysis results.

## Features

- **GitHub Repository Cloning:** Clone repositories for automated analysis.
- **Repository Scanning:** Identify files, directories, programming languages, frameworks, package managers, Docker configurations, and documentation.
- **Intelligent File Selection:** Select relevant source files for AI-powered review.
- **AI-Powered Code Review:** Generate structured feedback using Google's Gemini API.
- **Issue Classification:** Organize findings by category and severity.
- **File-Level Feedback:** Include affected file paths and line references when available in the generated review.
- **Actionable Recommendations:** Present suggestions to improve code quality.
- **Repository Quality Score:** Display an overall score alongside strengths, issues, and recommendations.
- **REST API:** Expose repository cloning, scanning, and review functionality through FastAPI endpoints.
- **Web Interface:** Interact with the review workflow through a React frontend.

## Tech Stack

| Component | Technologies |
|---|---|
| Backend | Python, FastAPI |
| Frontend | React, Vite, JavaScript |
| AI Integration | Google Gemini API |
| Repository Operations | GitPython |
| Data Validation | Pydantic |
| Frontend UI | Material UI |
| HTTP Client | Axios |

## Architecture

The application follows a frontend-backend architecture:

1. The user submits a GitHub repository URL through the React interface.
2. The backend clones the repository into a temporary workspace.
3. The repository scanner and indexer analyze the repository structure and technology stack.
4. The file selector identifies relevant files for review.
5. The prompt builder prepares the repository context for the Gemini model.
6. The AI review service obtains and parses the model's response into a structured format.
7. The frontend displays the overall score, strengths, issues, and recommendations.

## Project Structure

```text
ai-code-review-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── database.py
│   │   └── main.py
│   ├── tests/
│   ├── temp/
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   └── pages/
│   ├── package.json
│   └── vite.config.js
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.11 or compatible Python version
- Node.js and npm
- Git
- A Google Gemini API key

### 1. Clone the project

```bash
git clone https://github.com/rishabh-0411/ai-code-review-platform.git
cd ai-code-review-platform
```

### 2. Configure the backend

Open a terminal in the project directory:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create a `.env` file in the `backend` directory and configure your Gemini API key using the environment variable name expected by your application.

**Never commit your `.env` file or expose your API key.**

Start the FastAPI development server using the application's entry point:

```powershell
uvicorn app.main:app --reload
```

If your application uses a different configuration or entry point, follow the corresponding project settings.

### 3. Configure the frontend

Open a second terminal from the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite in your terminal.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/repositories/clone` | Clone a GitHub repository |
| POST | `/repositories/scan` | Scan and analyze a repository |
| POST | `/repositories/review