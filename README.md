# CMSC 426 Jenkins CI Project

A simple Python app for In-Class Activity #3. The app adds two numbers, and Jenkins runs the tests automatically when code is pushed to GitHub.

## Files

- `app.py` - the app (`add_numbers` function)
- `tests/test_app.py` - unit tests
- `Jenkinsfile` - the Jenkins pipeline

## Requirements

- Python 3
- Git
- Jenkins with the Git and GitHub plugins (for CI)

## Run the app

```
python3 app.py
```

## Run the tests

```
python3 -m unittest discover -s tests -v
```

## How Jenkins runs it

The Jenkins job `Student-CI-Project` gets the code from this repo and runs the Jenkinsfile. It checks the Python version, runs the app, and runs the tests. If a test fails, the build fails.

A GitHub webhook tells Jenkins when new code is pushed. Since Jenkins runs on my laptop, ngrok is used so GitHub can reach it.

## Setup steps (Mac)

1. `brew install openjdk@21 jenkins-lts`
2. `brew services start jenkins-lts` and open http://localhost:8080
3. Create a Pipeline job that uses this repo and the `Jenkinsfile` on the `main` branch
4. Click Build Now

Last trigger test: November 14, 2026
