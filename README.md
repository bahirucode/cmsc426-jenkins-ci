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

Jenkins checks GitHub for new commits every 2 minutes (Poll SCM, `H/2 * * * *`) and starts a build when it finds one. I tried a GitHub webhook with ngrok first, but my network blocked the ngrok connection, so I used polling instead.

## Setup steps (Mac)

1. `brew install openjdk@21 jenkins-lts`
2. `brew services start jenkins-lts` and open http://localhost:8080
3. Create a Pipeline job that uses this repo and the `Jenkinsfile` on the `main` branch
4. Under Triggers, turn on Poll SCM with `H/2 * * * *`
5. Click Build Now once, then push changes and Jenkins builds them automatically
