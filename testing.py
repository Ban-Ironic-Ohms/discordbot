"""
from datetime import datetime
import copy

now = datetime.now()
current_time = now.strftime("%Y:%m:%d:%H:%M:%S")
        
year = int(now.strftime("%Y"))
month = int(now.strftime("%m"))
day = int(now.strftime("%d"))
hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
second = int(now.strftime("%S"))

time = [["Y", year], ["m", month], ["d", day], ["H", hour], ["M", minute], ["S", second]]


pingtime = copy.deepcopy(time)
i = -1

passed_time = ["H", 10]
for unit in time:
    i += 1
    if unit[0] == passed_time[0]:
        pingtime[0][1] += passed_time[1]

print(datetime.utcnow().timestamp())
"""

entry = {"ping":"time"}

with open("timer.json", "r+") as file:
    data = json.load(file)
    data.update(entry)
