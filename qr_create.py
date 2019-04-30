# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:17:26 2019

@author: TOMATO
"""

import cv2
import numpy as np
import qrcode
import matplotlib.pyplot as plt
from PIL import Image

if __name__=='__main__':
    

    #最简单的二维码生成
    #img = qrcode.make('Hello,baby!')
    
    #高级设置
    #version:1-40,尺寸大小，从21*21开始，每次加4个单位大小
    #error_correction：纠错能力 L:7%,M:15%,Q:25%,H:35%
    #box_size:每个格子的像素大小
    #border:边框的格子宽度，默认4
    qr = qrcode.QRCode(version=7, 
                       error_correction=qrcode.constants.ERROR_CORRECT_H, 
                       box_size=5,
                       border=4)
    data="向美华****2019****王强CNY"
    qr.add_data(data)
    qr.make(fit=True)
    qrimg = qr.make_image()
    h,w=qrimg.size

    #添加logo，根据纠错能力，logo尺寸占比最大为0.0049,0.0225,0.0625,0.1225
    logo_percent=0.25#不需平方
    decay=0.85#logo大小系数0-1
    logo_h=int(h*logo_percent*decay)
    logo_w=int(w*logo_percent*decay)
    logo_img=Image.open("logo.png")
    logo_img_resized=logo_img.resize((logo_w, logo_h), resample=Image.ANTIALIAS)

    new_qrimg = Image.new('RGB', (w, h), (255, 255, 255))
    new_qrimg.paste(qrimg, box=(0, 0))
    x=int(w/2-logo_w/2)
    y=int(h/2-logo_h/2)
    new_qrimg.paste(logo_img_resized, box=(x, y))


    new_qrimg.save("D:\projects\qrdecode_zbar\qrdecode_zbar\qrcode.png")
    
    #plt显示
    plt.figure("qrcode",figsize=(12,6))
    plt.subplot(1,3,1)
    title='qrcode without logo'
    plt.imshow(qrimg)
    plt.subplot(1,3,2)
    title='logo image'
    plt.imshow(logo_img_resized)
    plt.subplot(1,3,3)
    title='qrcode with logo'
    plt.imshow(new_qrimg)

    plt.show()
    
    
    
    
    #转成nparray实例，cv显示
    img_np=np.asarray(qrimg)
    img_np=(img_np*255).astype(np.uint8)
    cv2.namedWindow("qrcode_creat",0)
    cv2.imshow("qrcode_creat",img_np)
    cv2.waitKey(0)
    
    
    rotate_mat=cv2.getRotationMatrix2D((w/2,h/2),270,1)
    code_reversal=cv2.warpAffine(img_np,rotate_mat,(h,w))
    cv2.imwrite("D:\projects\qrdecode_zbar\qrdecode_zbar\qrcodenp.png",code_reversal)
    
   


    cv2.destroyAllWindows()



