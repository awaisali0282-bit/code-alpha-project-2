# code-alpha-project-2
**Secure Code Review Dashboard** — A Python and Flask-based cybersecurity tool that analyzes source code for common vulnerabilities such as hardcoded credentials, SQL injection patterns, `eval()`, command execution, weak hashing, and insecure HTTP usage.
# 🛡️ Secure Code Review Dashboard

A lightweight **cybersecurity-focused static code analysis tool** built with Python and Flask. It analyzes submitted source code for common security-related coding patterns and presents the results through a professional web dashboard.

## 📌 Overview

The Secure Code Review Dashboard helps identify potentially risky patterns in source code before deployment. The backend analyzes the submitted code using pattern matching and returns categorized security findings.

The frontend provides a clear interface for submitting code and viewing detected issues according to their severity.

## ✨ Features

- 🔍 Static source-code analysis
- 🔐 Hardcoded credential detection
- 💉 SQL injection pattern detection
- ⚠️ `eval()` detection
- 💻 Command execution pattern detection
- 🐞 Debug mode detection
- 🔑 Weak hashing detection
- 🌐 Insecure HTTP detection
- 📊 HIGH / MEDIUM / LOW severity classification
- 💡 Security recommendations for detected findings
- 🟢 Backend status monitoring
- 🔄 Frontend-backend API communication

## 🛠️ Technology Stack

- **Python**
- **Flask**
- **Flask-CORS**
- **Regular Expressions**
- **HTML5**
- **CSS3**
- **JavaScript**

## 📂 Project Structure

```text
Secure-Code-Review/
│
├── index.html
├── style.css
├── script.js
├── security_analyzer.py
└── requirements.txt
```

## ⚙️ Installation

### 1. Install the required packages

```bash
pip install -r requirements.txt
```

### 2. Start the backend

```bash
python security_analyzer.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

### 3. Launch the frontend

Open `index.html` using **VS Code Live Server**.

## 🔄 How It Works

```text
Source Code
     ↓
Frontend Interface
     ↓
Flask API
     ↓
Security Pattern Analysis
     ↓
Vulnerability Findings
     ↓
Severity Classification
     ↓
Security Recommendations
     ↓
Dashboard Results
```

## 🔌 API Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/api/analyze` | POST | Analyze submitted source code |
| `/api/status` | GET | Check backend status |

## 🔐 Security Checks

The analyzer currently checks for patterns associated with:

- Hardcoded credentials
- SQL injection
- Dynamic code execution
- Operating-system command execution
- Debug mode
- Weak hashing algorithms
- Insecure HTTP connections

> **Note:** This is a pattern-based static analyzer and is not a replacement for comprehensive security testing or professional code auditing.

## 🎯 Learning Objectives

This project demonstrates practical concepts in:

- Secure coding
- Static code analysis
- Vulnerability identification
- Python-based cybersecurity automation
- REST API development
- Frontend-backend integration
- Security severity classification

## 🚀 Future Enhancements

Potential improvements include:

- Support for additional programming languages
- Line-number detection for findings
- Code syntax highlighting
- Exportable security reports
- Larger vulnerability rule sets
- CVE/CWE-based classification
- Advanced static analysis techniques
- Security report generation

## ⚠️ Disclaimer

This project is developed for **educational and authorized security-analysis purposes**. Detection results are based on configured patterns and should be manually reviewed before making security decisions.

## 👨‍💻 Project

**Secure Code Review Dashboard**  
Developed as part of a hands-on **Cybersecurity Project Series**.
