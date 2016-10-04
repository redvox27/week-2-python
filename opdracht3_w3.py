import time
class stopwatch:
    startTime = 0
    endTime = 0
    result = 0
    def __init__(self):
        self.startTime = time.time()


    def start(self):
        self.startTime = time.time()
        return self.startTime
        #print(self.startTime)

    def stop(self):
        self.endtime = time.time()
        return self.endtime

    def getElapsedTime(self):
        self.result = self.endtime - self.startTime
        print(self.result)

