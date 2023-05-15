FROM python:3.10

COPY github_team_check.py /github_team_check.py

RUN pip install PyGithub

ENTRYPOINT ["python", "github_team_check.py"]
