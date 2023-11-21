## Test Automation Project for [Practice.ExpandTesting.com](https://practice.expandtesting.com/)

---

[![Website](https://img.shields.io/website.svg?url=https://prog420.github.io/AutomationPractice)]()
[![Python](https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11-blue)]()
[![CodeStyle](https://img.shields.io/badge/code%20style-black-000000.svg)]()

---

It's a playground project for automated UI testing using Python, Pytest and Selenium.

**Test Reports:** [Allure](https://allurereport.org/)

**CI:** [Github Actions](https://github.com/features/actions/)

### 🛠️ Prerequisites

[![Pytest](https://img.shields.io/badge/pytest-7.4.0-blue)](https://pypi.python.org/pypi/pytest)
[![pytest-xdist](https://img.shields.io/badge/pytest--xdist-3.3.1-blue)](https://pypi.org/project/pytest-xdist/)
[![Selenium](https://img.shields.io/badge/selenium-4.10.0-blue)](https://pypi.org/project/selenium/)
[![Allure Pytest](https://img.shields.io/badge/allure--pytest-2.13.2-blue)](https://pypi.python.org/pypi/allure-pytest)
[![webdriver-manager](https://img.shields.io/badge/webdriver--manager-4.0.0-blue)](https://pypi.org/project/webdriver-manager/)

### 🛠️ Running Tests

---

#### a) Github Actions CI

Check Latest Test Run Report: [Allure Report Page](https://prog420.github.io/AutomationPractice)

Launch New Test Run:

1. Navigate to `Actions` tab.
2. Select `Allure Report CI`.
3. Click `Run Workflow`.
4. Select `Use Workflow From:`: `Branch: main`.
5. Click `Run Workflow`.
6. Wait until the job is complete.
7. Navigate to [Allure Report Page](https://prog420.github.io/AutomationPractice).

---

#### b) Local Machine:

1. Clone repository, install dependencies:
```bash
# Clone repository
git clone ...

# Install virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

3) Start new test run:

```bash
pytest -vs --alluredir=allure-reports
```

4) Check allure report:

```bash
allure serve allure-reports
```

---

#### CLI Arguments:
1. `--headless` - run tests without loading the browser's UI.