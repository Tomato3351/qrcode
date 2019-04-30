# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:59:43 2019

@author: TOMATO
"""

import pyqrcode
import qrcode
from qrtools import qrtools
#import matplotlib.pyplot as plt
from PIL import Image

if __name__=='__main__':
    
    qrimg=Image.open("qrcode.png")
#    qr=QR("qrcode.png")
#    d=qrcode.QR(qrimg)
    qrtools.QR("qrcode.png")
#    print(d.data)
#    qr.decode("qrcode.png")
#    print(qr.data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    