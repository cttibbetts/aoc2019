import json
import math
from datetime import timedelta, datetime
from tabulate import tabulate

DEBUG = False

teams = {
  'nma': [
    'Christopher Tibbetts',
    'Taybin Rutkin',
    'Matthew Doherty',
    'Khaled Asaad',
    'Phuongnhat Nguyen',
    'Judith Harrigan',
    'Shawn Whitney',
    'Elise Thorsen',
    'Jacob Coakwell',
  ],
  'boston': [
    'Matthew Doherty',
    'Douglas Bodkin',
    'Ben Goldin',
    'Nicholas Davis',
    'Philippe Mimms',
    'Taybin Rutkin',
    'Christopher Tibbetts',
    'Phuongnhat Nguyen',
    'Nicholas Chounlapane',
    'Adam Mantell',
    'Judith Harrigan',
    'David Dulczewski',
    'Michael Singleton',
    'Brendan Terrio',
    'Daniel St. George',
    'Melissa Blotner',
    'Nathaniel Bowditch',
    'Kraig Boates',
    'Steven Keith',
    'Geoffrey Sullivan',
    'Christopher Regan',
    'Steve Carlon',
  ]
}

whitelist = None
# whitelist = teams['nma']
# whitelist = teams['boston']

def to_relative_seconds(day_number, timestamp):
  day_number -= 1 # offset by one
  dec_1 = 1575176400
  day_delta = 86400
  return timestamp - (dec_1 + day_number * day_delta)

def print_ts(delta):
  return str(timedelta(seconds=delta))

def get_median_solve(user):
  score = 0
  try:
    half = math.floor(len(user['scores'])/2)

    if len(user['scores']) % 2 == 0:
      score = math.ceil((user['scores'][half-1] + user['scores'][half]) / 2)
    else:
      score = user['scores'][half]
  except:
    pass
  return score

def get_middle_scores(user):
  scores = user['scores']
  half = math.floor(len(scores)/2)
  return scores[half-1:half+2]

def sort_users(user):
  return user['stars'], -user['median_score']

def process_user(user):
  user['scores'] = sorted([
    to_relative_seconds(int(day), int(score['2']['get_star_ts']))
    for day, score in user['completion_day_level'].items()
    if '2' in score
  ])
  user['median_score'] = get_median_solve(user)
  if (user['name'] == 'Christopher Tibbetts' and DEBUG):
    print([print_ts(s) for s in user['scores']])
  return user

if __name__ == '__main__':
  with open('leaderboard.json') as input:
    scoreboard = json.loads(input.readline())
    users = scoreboard['members']

    users = sorted(
      [process_user(u) for u in users.values()],
      key=sort_users,
      reverse=True
    )

    table = [
      ([i+1, user['name'], user['stars'] * '*', print_ts(user['median_score']), *[print_ts(ts) for ts in get_middle_scores(user)]])
      for i, user in enumerate(users)
      if user['stars'] > 0 and (user['name'] in whitelist if whitelist is not None else True)
    ]
    print(tabulate(table, headers=["Place", "Name", "Stars", "Median Solve Time", "better", "current", "worse"]))
