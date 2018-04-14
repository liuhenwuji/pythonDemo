#! python3
import time

print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')
input()
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input();
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
