# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import time
import PyQt5
Time_value=1
Freq_value=25

from PyQt5 import QtWidgets,uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice

app=QtWidgets.QApplication([])
ui=uic.loadUi("design.ui")
ui.setWindowTitle("KT train")

serial = QSerialPort()
serial.setBaudRate(9600)
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
    Time_value=ui.Time_set.value()
    ui.Time_LCD.display(Time_value)
    print(Time_value)
    
def freq_slider():
    Freq_value=ui.Freq_set.value()
    ui.Freq_LCD.display(Freq_value)
    print(Freq_value)

vals=[10,11,12]
serialSendData(vals)

ui.com_select.addItems(portList)
ui.com_select.currentIndexChanged.connect(test)
ui.com_apply.clicked.connect(com_open)
ui.com_close.clicked.connect(com_close)


ui.Time_set.valueChanged.connect(time_slider)
ui.Freq_set.valueChanged.connect(freq_slider)

ui.start_button.clicked.connect(start_but_event)
ui.stop_button.clicked.connect(stop_but_event)

ui.Power_LCD.display(28.2)
ui.Time_LCD.display(Time_value)
ui.Freq_LCD.display(Freq_value)

serial.readyRead.connect(onRead) 


ui.show()
app.exec()
