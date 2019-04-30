# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 09:38:02 2019

@author: TOMATO
"""

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont,QIcon
import qrcode
import matplotlib.pyplot as plt
#from PIL import Image

class exp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        #鼠标停留添加提示信息
        self.setGeometry(600,200,800,600)#窗口位置和大小
        self.setWindowTitle('Hello!')
        #设置窗口图标
        self.setWindowIcon(QIcon('d:/python_projects/qrcode/tomato.ico'))
               
        QtWidgets.QToolTip.setFont(QFont('SansSerif',15))
        self.setToolTip('This is a <b>widget</b>')#html语法的加粗显示
        btn=QtWidgets.QPushButton('close',self)
        btn.setToolTip('Press and close the window')
        btn.resize(btn.sizeHint())#自动尺寸
        btn.clicked.connect(QtCore.QCoreApplication.quit)
#        btn.move(650,500)
        hbox=QtWidgets.QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn)
        
        vbox=QtWidgets.QVBoxLayout()
        vbox.addStretch()

        vbox.addLayout(hbox)
        
        self.setLayout(vbox)        

        self.show()
    def closeEvent(self,event):
        reply=QtWidgets.QMessageBox.question(self,'Ensure','Are you sure to quit?',
                                             QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                             QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #鼠标停留添加提示信息
        self.setGeometry(600,200,800,600)#窗口位置和大小
        self.setWindowTitle('Hello!')
        #设置窗口图标
        self.setWindowIcon(QIcon('d:/python_projects/qrcode/tomato.ico'))
        
        
        
        self.statusBar()#状态栏,显示悬停提示信息
        #设置带有图标的菜单命令Exit
        exitAction=QtWidgets.QAction(QIcon('d:/python_projects/qrcode/logo.ico'),'&Exit',self)
        exitAction.setShortcut('Ctrl+Q')#设置快捷键
        exitAction.setStatusTip('Exit the app')#添加鼠标悬停时的提示信息
        exitAction.triggered.connect(QtWidgets.qApp.quit)
        
        menubar=self.menuBar()#菜单栏
        fileMenue=menubar.addMenu('&file')#菜单栏里加file菜单
        fileMenue.addAction(exitAction)#file菜单里加exitAction
        
        self.toolbar=self.addToolBar('Exitoolbar')#创建名为Exittoolbar的工具栏
        self.toolbar.addAction(exitAction)#工具栏里添加exitAction

#        text=QtWidgets.QTextEdit()
#        self.setCentralWidget(text)
        
#        btn=QtWidgets.QPushButton('close',self)
#        btn.setToolTip('Press and close the window')
#        btn.resize(btn.sizeHint())#自动尺寸
#        btn.clicked.connect(QtCore.QCoreApplication.quit)
#        btn.move(650,500)        
        
#        hbox=QtWidgets.QHBoxLayout()
#        hbox.addStretch()
#        hbox.addWidget(btn)
#        
#        vbox=QtWidgets.QVBoxLayout()
#        vbox.addStretch()
#        vbox.addWidget(btn)
#        vbox.addLayout(hbox)
#        
#        self.setLayout(vbox)
        
        self.show()
        



if __name__=='__main__':
    
#    qr = qrcode.QRCode(version=1, 
#                       error_correction=qrcode.constants.ERROR_CORRECT_Q, 
#                       box_size=10,
#                       border=4)
#    
#    data="Trouble he will find you no matter where you go oh oh."
#    qr.add_data(data)
#    qr.make(fit=True)
#    qrimg = qr.make_image()
#    h,w=qrimg.size
#    
#    plt.figure("qrcode",figsize=(12,6))
#    plt.subplot(1,3,1)
#    title='qrcode without logo'
#    plt.imshow(qrimg)
    
#    qrimg.save("qrcode.png")
    
    
#    app=QtWidgets.QApplication(sys.argv)
#    widget=QtWidgets.QWidget()
#    widget.setWindowTitle('Hello')
#    widget.resize(500,500)
#    widget.move(700,200)
#    widget.setWindowIcon(QtGui.QIcon('logo.png'))  #设置应用图标
#    widget.show()
    
    app=QtWidgets.QApplication(sys.argv)
    ex=exp()
#    ex=mainwin()
    
    sys.exit(app.exec_())
    
    
    
    
    
    
    
    
    
    
    