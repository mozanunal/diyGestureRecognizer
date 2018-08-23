import time
import threading
from gestureControl import sensor

myGesSensor = sensor("COM3", 115200)

while True:
    # myGesSensor.plotsDataEvent.wait(2)
    # print("passsed")
    # myGesSensor.plotDataEvent.clear()
    input()
    time.sleep(1000)
