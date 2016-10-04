from opdracht3_w3 import stopwatch

size = 1000000
stopWatch = stopwatch()
sum = 0
for i in range(1, size + 1):
 sum += i
stopWatch.stop()

stopWatch.getElapsedTime()
