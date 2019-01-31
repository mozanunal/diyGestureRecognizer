
import serial
import numpy as np
import threading
from serReadline import serReadline


class Sensor(object):
    def __init__(self, comport, baudrate):
        # Serial
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = comport
        self.ser.open()
        self.serialReader = serReadline(self.ser)
        # Data and Plot
        self.x = np.arange(1000)
        self.data0 = []
        self.data1 = []
        self.data2 = []
        self.readThread = threading.Thread(target=self.readSampleThread)
        self.readThread.start()

    def __del__(self):
        self.ser.close()

    def readSamples(numberOfSample):
        pass

    def readSampleThread(self):
        counter = 0
        while True:
            try:
                sample = str(self.serialReader.readline(), 'ascii').replace('\r\n', '').split(" ")
                sample_Int = [int(i) for i in sample]
                self.data0.append(sample_Int[0])
                self.data1.append(sample_Int[1])
                self.data2.append(sample_Int[2])

                counter = counter+1
                print(counter)
                if counter % 500 == 0:
                    print("setttinggg")
            except Exception as e:
                print(e)
                time.sleep(1)
