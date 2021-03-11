# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:06:23 2021

@author: HRITHIK
"""
import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
from scipy import interpolate
import tkinter as tk
#from tkinter import filedialog
from tkinter import *
#from PIL import ImageTk, Image

top=tk.Tk()
top.geometry('900x1000')
top.title('Filter Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',25,'bold'))

#to open file path where image is stored
def uploadImg():
    ImagePath=easygui.fileopenbox()
    
    
    emboss(ImagePath)
    sepia(ImagePath)
    caartoonify(ImagePath)
    warmImage(ImagePath)
    coldImage(ImagePath)
    bW(ImagePath)

def sepia(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()
    
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepiaFiltered=cv2.filter2D(originalImage, -1, kernel)
    
    Resized7=cv2.resize(sepiaFiltered,(800,800))
    
    save1=Button(top,text="Save sepia filtered image",command=lambda: save(Resized7,ImagePath,"sepia_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30)


def emboss(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()
    
    kernel = np.array([[0,-1,-1],
                            [1,0,-1],
                            [1,1,0]])
    embossFiltered=cv2.filter2D(originalImage, -1, kernel)
    
    Resized7=cv2.resize(embossFiltered,(800,800))
    
    save1=Button(top,text="emboss filtered image",command=lambda: save(Resized7,ImagePath,"emboss_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30)
    
def spreadLookupTable(x, y):
    
      spline = interpolate.UnivariateSpline(x, y)
      return spline(range(256))

def warmImage(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(originalImage)
    red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
    filtered=cv2.merge((red_channel, green_channel, blue_channel))
    
    resized=cv2.resize(filtered,(800,800))
    
    save1=Button(top,text="warm filtered image",command=lambda: save(resized,ImagePath,"emboss_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30)

def coldImage(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()
    
    increaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 80, 160, 256])
    decreaseLookupTable = spreadLookupTable([0, 64, 128, 256], [0, 50, 100, 256])
    red_channel, green_channel, blue_channel = cv2.split(originalImage)
    red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
    blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
    filt=cv2.merge((red_channel, green_channel, blue_channel))
    
    resized=cv2.resize(filt,(800,800))
    
    save1=Button(top,text="cold filtered image",command=lambda: save(resized,ImagePath,"emboss_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30)

def caartoonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()

      
    #resizing numberred formed image
    ReSized1 = cv2.resize(originalImage, (800, 800))
    #plt.imshow(ReSized1, cmap='gray')
    
    #converting resized image to gray form
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (800, 800))
    #plt.imshow(ReSized2, cmap='gray')
    
    #smoothing an image
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (800, 800))
    #plt.imshow(ReSized3, cmap='gray')
    
    #edging the image
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (800, 800))
    #plt.imshow(ReSized4, cmap='gray')
    
    #beautifying image
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (800, 800))
    #plt.imshow(ReSized5,cmap="gray")
   
    
    #masking image
    cartoonImg=cv2.bitwise_and(colorImage,colorImage,mask=getEdge)
    
    ReSized6=cv2.resize(cartoonImg,(800,800)) 
    
    #plt.imshow(ReSized6,cmap="gray")
    
    #plotting the transition
    images=[ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
    fig, axes = plt.subplots(3,2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
        
    plt.show()
    
    
    
    save1=Button(top,text="Save cartoon image",command=lambda: save(ReSized6,ImagePath,"cartoon_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30) 
    
def bW(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    
    #checking if image is selected properly
    if originalImage is None:
        print("Sorry! Image not found choose appropriate file.")
        sys.exit()
    
    grayScaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleImage, (800, 800))
    
    
    save1=Button(top,text="Save black&white image",command=lambda: save(ReSized2,ImagePath,"B&W_img"),padx=30,pady=5)
    save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
    save1.pack(side=TOP,pady=30)
    

def save(ReSized6,ImagePath,newName):
    #saving an image using imwrite()
    
    path1 = os.path.dirname(ImagePath)
    extension=os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName+extension)
    
    cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName +" at "+ path
    
    tk.messagebox.showinfo(title=None, message=I)
    
    


upload=Button(top,text="Select img file",command=uploadImg,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=30) 



top.mainloop()

    
