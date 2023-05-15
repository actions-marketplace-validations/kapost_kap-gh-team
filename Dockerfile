FROM python:3.10

WORKDIR /app
COPY github_team_check.py .

RUN pip install PyGithub

ENTRYPOINT ["python", "github_team_check.py"]
