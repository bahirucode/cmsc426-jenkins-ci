# CMSC 426 – Jenkins CI Project

A small Python app used to practice continuous integration with Jenkins and GitHub.
Every push to this repository triggers a Jenkins pipeline that runs the app and its unit tests.

## What it does

`app.py` has one function, `add_numbers(a, b)`, which returns the sum of two numbers.
Running the file prints:

```
Application started
2 + 3 = 5
```

## Project structure

```
cmsc426-jenkins-ci/
├── app.py              # the application
├── tests/
│   ├── __init__.py
│   └── test_app.py     # unittest test cases for add_numbers()
├── Jenkinsfile         # declarative pipeline that Jenkins runs
├── README.md
└── .gitignore
```

## Requirements

- Python 3 (tested with 3.15 from Homebrew; no third-party packages needed)
- Git
- For CI: Jenkins LTS on Java 21, with the Git, GitHub and Pipeline plugins

## Run the app

```bash
python3 app.py
```

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

All four tests should report `ok`.

## How Jenkins runs the tests

The Jenkins job `Student-CI-Project` is a Pipeline job set to "Pipeline script from SCM".
It checks out this repo and runs the `Jenkinsfile`, which has four stages:

1. **Checkout** – pulls the latest commit.
2. **Environment verification** – prints the python3 and git versions Jenkins is using.
3. **Run app** – runs `python3 app.py`.
4. **Unit tests** – runs `python3 -m unittest discover -s tests -v`. If any test fails,
   the command exits non-zero and Jenkins marks the build as FAILURE.

The Jenkinsfile adds `/opt/homebrew/bin` to `PATH`, because Jenkins started by
`brew services` only sees the system paths.

## GitHub trigger

The job has "GitHub hook trigger for GITScm polling" turned on. A GitHub webhook sends
push events to `<public tunnel URL>/github-webhook/`, and Jenkins then starts a build.
Since Jenkins runs on my laptop (localhost), a temporary tunnel is used only during the
demo and is shut down afterward.

## Reproducing this setup (macOS)

1. `brew install openjdk@21 jenkins-lts`
2. `brew services start jenkins-lts`, then open http://localhost:8080 and finish the setup wizard
   (install suggested plugins, create an admin user).
3. Clone this repo and check that `python3 -m unittest discover -s tests -v` passes.
4. In Jenkins, create a Pipeline job: Pipeline script from SCM → Git → this repo's URL,
   branch `main`, Script Path `Jenkinsfile`.
5. Click **Build Now** and check the console output.
6. For automatic builds, expose Jenkins through a temporary HTTPS tunnel, add a GitHub
   webhook pointing to `/github-webhook/`, and enable the GitHub hook trigger in the job.
