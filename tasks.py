from invoke import task
from datetime import datetime

@task
def run(c, day):
  with c.cd(day):
    c.run(f"python3 main.py")

@task
def leaderboard(c):
  with c.cd('leaderboard'):
    c.run(f"python3 main.py")

@task
def init(c, day):
  c.run(f"mkdir -p {day}")
  c.run(f"cp template/* {day}/")
