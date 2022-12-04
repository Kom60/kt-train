# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time
import PyQt5

Time_value=1
Time_min=1
Time_max=999

Freq_min=25
Freq_max=65
Freq_value=25

Power_value=0

from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app=QtWidgets.QApplication([])
ui=uic.loadUi("design.ui")
ui.setWindowTitle("KT train")

serial = QSerialPort()
serial.setBaudRate(115200)
portList=[]
ports=QSerialPortInfo.availablePorts()
for port in ports:
    portList.append(port.portName())
print(portList)

def test():
    print("F")
    
def com_open():
    serial.setPortName(ui.com_select.currentText())
    print(ui.com_select.currentText())
    serial.open(QIODevice.ReadWrite)
    
def com_close():
    #serial.setPortName(ui.com_select.currentText())
    #print(ui.com_select.currentText())
    serial.close()
    
def onRead():
    rx=serial.readLine()
    rxs=str(rx,'utf-8').strip()
    print(rxs)
    data=rxs.split(',')
   # if()
    
def onClose():
    serial.close()
    
def serialSendData(data): #int list
    txs=""
    for val in data:
        txs+=str(val)
        txs+=','
    txs=txs[:-1]
    txs+=';'
    print(txs)
    serial.write(txs.encode())

def start_but_event():
    one="1"
    print("start")
    serial.write(one.encode())
    #serial.write(1)
    
def stop_but_event():
    zero="0"
    print("stop")
    serial.write(zero.encode())
    
def time_slider():
    global Time_value
    Time_value=ui.Time_set.value()
    ui.Time_LCD.display(Time_value)
    print(Time_value)
    
def freq_slider():
    global Freq_value
    Freq_value=ui.Freq_set.value()
    ui.Freq_LCD.display(Freq_value)
    print(Freq_value)

def minus_1_hz():
    #one="1"
    print("-1Hz")
    global Freq_value
    global Freq_min
    global Freq_max
    if(Freq_value-1>Freq_min):
        Freq_value=Freq_value-1
    ui.Freq_LCD.display(Freq_value)
   # serial.write(one.encode())
    #serial.write(1)
    
def plus_1_hz():
    #one="1"
    print("+1Hz")
    global Freq_value
    global Freq_min
    global Freq_max
    if(Freq_value+1<=Freq_max):
        Freq_value=Freq_value+1
    ui.Freq_LCD.display(Freq_value)
    # serial.write(one.encode())
    #serial.write(1)
    
def minus_1_min():
    #one="1"
    print("-1 min")
    global Time_value
    global Time_min
    global Time_max
    if(Time_value-1>Time_min):
        Time_value=Time_value-1
    ui.Time_LCD.display(Time_value)

   # serial.write(one.encode())
    #serial.write(1)
    
def plus_1_min():
    #one="1"
    print("+1 min")
    global Time_value
    global Time_min
    global Time_max
    if(Time_value+1<=Time_max):
        Time_value=Time_value+1
    ui.Time_LCD.display(Time_value)
    # serial.write(one.encode())
    #serial.write(1)

vals=[10,11,12]
serialSendData(vals)

ui.com_select.addItems(portList)
ui.com_select.currentIndexChanged.connect(test)
ui.com_apply.clicked.connect(com_open)
ui.com_close.clicked.connect(com_close)


ui.Time_set.valueChanged.connect(time_slider)
ui.Freq_set.valueChanged.connect(freq_slider)

ui.minus_1_min.clicked.connect(minus_1_min)
ui.plus_1_min.clicked.connect(plus_1_min)

ui.minus_1_Hz.clicked.connect(minus_1_hz)
ui.plus_1_Hz.clicked.connect(plus_1_hz)

ui.Power_LCD.display(Power_value)
ui.Time_LCD.display(Time_value)
ui.Freq_LCD.display(Freq_value)

serial.readyRead.connect(onRead) 


ui.show()
app.exec()
