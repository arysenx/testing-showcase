# Testing Showcase Framework

[![CI/CD Status](https://github.com/arysenx/testing-showcase/actions/workflows/automated-testing.yaml/badge.svg)](https://github.com/username/testing-showcase/actions)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://python.org)
[![Pytest](https://img.shields.io/badge/Pytest-8.0+-green?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.16-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 🎯 Project Objective

This framework was engineered to demonstrate a **modern, scalable approach to Test Automation** that bridges the gap between fast API validation and user-centric UI testing. It addresses common challenges such as flaky tests, maintenance overhead, and fragmented reporting.

### Key Architectural Decisions
- **Page Object Model (POM)**: Strict encapsulation of UI elements and interactions to decouple test logic from DOM implementation details.
- **Config-Driven**: Environment-agnostic design using `config.yml` helps easily switch between Dev, Staging, and Prod environments.
- **CI/CD First**: Native integration with GitHub Actions including **headless execution** and artifact management.

---

## 🛠️ Technology Stack

| Category | Technology | Justification |
| :--- | :--- | :--- |
| **Core Framework** | **Pytest 8.x** |
| **API Engine** | **Requests** |
| **UI Engine** | **Selenium 4** |
| **Driver Mgmt** | **WebDriver Manager** |
| **Validation** | **JSONSchema** |
| **Reporting** | **Pytest-HTML** |
| **CI/CD** | **GitHub Actions** |

---

## 📁 Architecture

```text
testing-showcase/
├── .github/
│   └── workflows/
│       └── automated-testing.yaml  # CI/CD Pipeline definition
├── reports/                        # Test artifacts (HTML reports)
├── tests/
│   ├── api/                        # API Test Suite
│   │   ├── conftest.py             # API-specific fixtures
│   │   └── test_pokemon.py         # API test implementation
│   ├── ui/                         # UI Test Suite
│   │   ├── conftest.py             # WebDriver & Page Loader fixtures
│   │   └── test_login.py           # UI test implementation
│   ├── pages/                      # Page Object Models (POM)
│   │   ├── base.py                 # BasePage with explicit waits
│   │   └── login.py                # LoginPage logic
│   ├── common/                     # Shared Utilities
│   │   ├── schemas/                # JSON Schemas
│   │   └── helpers.py              # Config parsers & tools
│   └── conftest.py                 # Global hooks & configuration
├── config.yml                      # Centralized Configuration
├── pytest.ini                      # Pytest runner configuration
└── requirements.txt                # Dependency definitions
```

### Implemented Patterns
- **Page Object Model**: `tests/pages/`
- **Fixture Injection**: Extensive use of `conftest.py` for DI.
- **Strategy Pattern**: `page_loader` fixture for dynamic page instantiation.
- **Data-Driven Testing**: Parametrization in tests.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Google Chrome (for UI tests)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/username/testing-showcase.git
cd testing-showcase

# 2. Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r tests/requirements.txt
```

### Execution

**Run All Tests:**
```bash
python -m pytest tests/ -v
```

**Run Only API Tests:**
```bash
python -m pytest tests/api -v
```

**Run UI Tests (Headless):**
```bash
python -m pytest tests/ui --headless -v
```

**Generate HTML Report:**
```bash
python -m pytest tests/ --html=reports/report.html
```

**Run Behave Tests:**
```bash
behave bdd/features
```

---

## ⭐ Key Features

### 🔄 Intelligent Headless Mode
The framework automatically supports headless execution for CI environments via custom CLI flags.
```python
# tests/ui/conftest.py
if request.config.getoption("--headless"):
    chrome_options.add_argument("--headless")
```

### 🔐 Multi-Environment Configuration
Uses `config.yml` to separate test data from code, allowing secure and flexible configuration.
```yaml
# config.yml
environments:
  staging:
    base_url: https://staging.example.com
```

### 📉 Robust Reporting
Generates detailed HTML reports including error traces, duration, and status.
![Report Example]()

---

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration.

- **Trigger**: Pushes and Pull Requests to `main`.
- **Environment**: Ubuntu Latest + Python 3.11.
- **Steps**:
    1. Checkout Code.
    2. Install Dependencies (`pip install`).
    3. Run Tests in **Headless Mode**.
    4. Upload HTML Report as Artifact.

---

## 📈 Project Metrics

| Metric | Value |
| :--- | :--- |
| **Test Coverage** | API + UI |
| **Execution Time** | ~15s (local) |
| **Stability** | 100% Pass Rate |
| **Maintainability** | High (Modular Design) |

---

## 🤝 Contact

**Portfolio Candidate** - QA Automation Engineer | SDET
[LinkedIn](https://www.linkedin.com/in/angel-ramiro-jimenez/) | [Email](mailto:arj96@outlook.es)

> **Open to opportunities for**: SDET, ADET, QA Automation Engineer.

---
