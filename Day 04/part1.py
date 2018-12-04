from collections import defaultdict
from datetime import datetime

file=open("input.in","r")
content = file.readlines()

guardsShift = defaultdict(list)
guardTimes = defaultdict(int)

for line in sorted(content):
    time, action = line.split('] ') 
    time = datetime.strptime(time[1:], '%Y-%m-%d %H:%M')
    
    if action.startswith('Guard'):
        idGuard= int(action.split()[1][1:])
    elif 'falls asleep' in action:
        start_time = time
    elif 'wakes up' in action:
        end_time = time
        guardsShift[idGuard].append((start_time.minute,end_time.minute))
        guardTimes[idGuard] += (end_time.minute - start_time.minute)
    
(idSleepyGuard, highestTime) = max(guardTimes.items(), key=lambda par: par[1])

countTimes = [0 for x in range(60)]
for sleep in guardsShift[idSleepyGuard]:
    for i in range(sleep[0],sleep[1] + 1):
        countTimes[i] += 1

bestMinute = countTimes.index(max(countTimes))

print(idSleepyGuard)
print(bestMinute)
print(idSleepyGuard * bestMinute)