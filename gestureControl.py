
import serial
import pyqtgraph as pg
import numpy as np
import threading
import time

from serReadline import serReadline


class sensor(object):
    def __init__(self, comport, baudrate):
        # Serial
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = comport
        self.ser.open()
        self.serialReader = serReadline(self.ser)
        # Data and Plot
        self.plotWidget = pg.plot(title="Gesture Graphing")
        self.x = np.arange(1000)
        self.data0 = []
        self.data1 = []
        self.data2 = []

        # Threads
        self.plotDataEvent = threading.Event()
        self.readThread = threading.Thread(target=self.readSampleThread)
        self.readThread.start()
        self.plotThread = threading.Thread(target=self.plotDataThread)
        # plotWidget.plot(x, y[1], pen=(1,3))
        # plotWidget.plot(x, y[2], pen=(2,3))

    def __del__(self):
        self.ser.close()

    def resetData(self):
        pass

    def readSampleThread(self):
        counter = 0
        while True:
            try:
                sample = str(self.serialReader.readline(),'ascii').replace('\r\n', '').split(" ")
                sample_Int = [int(i) for i in sample]
                self.data0.append(sample_Int[0])
                self.data1.append(sample_Int[1])
                self.data2.append(sample_Int[2])

                counter = counter+1
                print(counter)
                if counter % 10 == 0:
                    print("setttinggg")
                    self.plotWidget.plot( self.data0 )
                    self.plotWidget.plot( self.data1 )
                    self.plotWidget.plot( self.data2 )
                    #self.plotDataEvent.set()
                # print(sample_Int)
            except Exception as e:
                print(e)
                time.sleep(1)

    def plotDataThread(self):
        # while True:
        #     self.plotDataEvent.wait()
        #     self.plotWidget.plot(self.data0)
        #     self.plotWidget.plot(self.data1)
        #     self.plotWidget.plot(self.data2)
        #     self.plotDataEvent.clear()
        # self.plotWidget.plot( self.x, self.data1, pen=(2,3) )
        # self.plotWidget.plot( self.x, self.data2, pen=(3,3) )
