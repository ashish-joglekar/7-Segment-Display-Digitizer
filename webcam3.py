#MIT License

#Copyright (c) 2016 Ashish Joglekar, RBCCPS, IISc <https://github.com/ashish-joglekar>

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import cv2
from PIL import Image
import PIL.ImageOps 
import time
import os, shutil
j=1
k=1
sx=[0 for i in range(22)]
sy=[0 for i in range(22)]

def click_point(event, x, y, flags, param):
    global j,k,sx,sy
    if event == cv2.EVENT_LBUTTONDOWN:      
        sx[k]=x
        sy[k]=y
        cv2.circle(clone,(sx[k],sy[k]), 3, (255,255,255), -1)
        k=k+1
        print sx
        print sy

# Camera 0 is the integrated web cam on my netbook
camera_port = 0
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()
print("Taking image...")
camera_capture = get_image()
file = "test_image.png"
cv2.imwrite(file, camera_capture)
image = cv2.imread("test_image.png")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_point)
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
	#stop when 21 points (3 seven segments) are selected on the image
    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        break
    elif k==22:
        break

while True:
    try:
        camera_capture = get_image()
        file = "test_image.png"
        cv2.imwrite(file, camera_capture)
        print "img..."
        image = cv2.imread("test_image.png")
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        
        ss11=gray_image[sy[1],sx[1]]
        ss12=gray_image[sy[2],sx[2]]
        ss13=gray_image[sy[3],sx[3]]
        ss14=gray_image[sy[4],sx[4]]
        ss15=gray_image[sy[5],sx[5]]
        ss16=gray_image[sy[6],sx[6]]
        ss17=gray_image[sy[7],sx[7]]


        ss21=gray_image[sy[8],sx[8]]
        ss22=gray_image[sy[9],sx[9]]
        ss23=gray_image[sy[10],sx[10]]
        ss24=gray_image[sy[11],sx[11]]
        ss25=gray_image[sy[12],sx[12]]
        ss26=gray_image[sy[13],sx[13]]
        ss27=gray_image[sy[14],sx[14]]


        
        #print "ss26=%d" %ss26

        ss31=gray_image[sy[15],sx[15]]
        ss32=gray_image[sy[16],sx[16]]
        ss33=gray_image[sy[17],sx[17]]
        ss34=gray_image[sy[18],sx[18]]
        ss35=gray_image[sy[19],sx[19]]
        ss36=gray_image[sy[20],sx[20]]
        ss37=gray_image[sy[21],sx[21]]

        print "ss11=%d" %ss11
        print "ss12=%d" %ss12
        print "ss13=%d" %ss13
        print "ss14=%d" %ss14
        print "ss15=%d" %ss15
        print "ss16=%d" %ss16
        print "ss17=%d" %ss17
        print "ss21=%d" %ss21
        print "ss22=%d" %ss22
        print "ss23=%d" %ss23
        print "ss24=%d" %ss24
        print "ss25=%d" %ss25
        print "ss26=%d" %ss26
        print "ss27=%d" %ss27
        print "ss21=%d" %ss31
        print "ss22=%d" %ss32
        print "ss23=%d" %ss33
        print "ss24=%d" %ss34
        print "ss25=%d" %ss35
        print "ss26=%d" %ss36
        print "ss27=%d" %ss37

##
##        
##        print "ss12=%d" %ss12
##        print "ss31=%d" %ss31
##
        if ss11<90:
            cv2.circle(gray_image,(sx[1],sy[1]), 3, (255,255,255), -1)
            ss11=1
        else:
            cv2.circle(gray_image,(sx[1],sy[1]), 3, (0,0,0), -1)
            ss11=0
            
        if ss12<90:
            cv2.circle(gray_image,(sx[2],sy[2]), 3, (255,255,255), -1)
            ss12=1
        else:
            cv2.circle(gray_image,(sx[2],sy[2]), 3, (0,0,0), -1)
            ss12=0

        if ss13<90:
            cv2.circle(gray_image,(sx[3],sy[3]), 3, (255,255,255), -1)
            ss13=1
        else:
            cv2.circle(gray_image,(sx[3],sy[3]), 3, (0,0,0), -1)
            ss13=0

        if ss14<90:
            cv2.circle(gray_image,(sx[4],sy[4]), 3, (255,255,255), -1)
            ss14=1
        else:
            cv2.circle(gray_image,(sx[4],sy[4]), 3, (0,0,0), -1)
            ss14=0


        if ss15<90:
            cv2.circle(gray_image,(sx[5],sy[5]), 3, (255,255,255), -1)
            ss15=1
        else:
            cv2.circle(gray_image,(sx[5],sy[5]), 3, (0,0,0), -1)
            ss15=0

        if ss16<90:
            cv2.circle(gray_image,(sx[6],sy[6]), 3, (255,255,255), -1)
            ss16=1
        else:
            cv2.circle(gray_image,(sx[6],sy[6]), 3, (0,0,0), -1)
            ss16=0

        if ss17<90:
            cv2.circle(gray_image,(sx[7],sy[7]), 3, (255,255,255), -1)
            ss17=1
        else:
            cv2.circle(gray_image,(sx[7],sy[7]), 3, (0,0,0), -1)
            ss17=0


        if ss21<90:
            cv2.circle(gray_image,(sx[8],sy[8]), 3, (255,255,255), -1)
            ss21=1
        else:
            cv2.circle(gray_image,(sx[8],sy[8]), 3, (0,0,0), -1)
            ss21=0
        

        if ss22<90:
            cv2.circle(gray_image,(sx[9],sy[9]), 3, (255,255,255), -1)
            ss22=1
        else:
            cv2.circle(gray_image,(sx[9],sy[9]), 3, (0,0,0), -1)
            ss22=0


        if ss23<90:
            cv2.circle(gray_image,(sx[10],sy[10]), 3, (255,255,255), -1)
            ss23=1
        else:
            cv2.circle(gray_image,(sx[10],sy[10]), 3, (0,0,0), -1)
            ss23=0

        if ss24<90:
            cv2.circle(gray_image,(sx[11],sy[11]), 3, (255,255,255), -1)
            ss24=1
        else:
            cv2.circle(gray_image,(sx[11],sy[11]), 3, (0,0,0), -1)
            ss24=0


        if ss25<90:
            cv2.circle(gray_image,(sx[12],sy[12]), 3, (255,255,255), -1)
            ss25=1
        else:
            cv2.circle(gray_image,(sx[12],sy[12]), 3, (0,0,0), -1)
            ss25=0
            
        if ss26<90:
            cv2.circle(gray_image,(sx[13],sy[13]), 3, (255,255,255), -1)
            ss26=1
        else:
            cv2.circle(gray_image,(sx[13],sy[13]), 3, (0,0,0), -1)
            ss26=0

        if ss27<90:
            cv2.circle(gray_image,(sx[14],sy[14]), 3, (255,255,255), -1)
            ss27=1
        else:
            cv2.circle(gray_image,(sx[14],sy[14]), 3, (0,0,0), -1)
            ss27=0

        if ss31<90:
            cv2.circle(gray_image,(sx[15],sy[15]), 3, (255,255,255), -1)
            ss31=1
        else:
            cv2.circle(gray_image,(sx[15],sy[15]), 3, (0,0,0), -1)
            ss31=0

        if ss32<90:
            cv2.circle(gray_image,(sx[16],sy[16]), 3, (255,255,255), -1)
            ss32=1
        else:
            cv2.circle(gray_image,(sx[16],sy[16]), 3, (0,0,0), -1)
            ss32=0

        if ss33<90:
            cv2.circle(gray_image,(sx[17],sy[17]), 3, (255,255,255), -1)
            ss33=1
        else:
            cv2.circle(gray_image,(sx[17],sy[17]), 3, (0,0,0), -1)
            ss33=0

        if ss34<90:
            cv2.circle(gray_image,(sx[18],sy[18]), 3, (255,255,255), -1)
            ss34=1
        else:
            cv2.circle(gray_image,(sx[18],sy[18]), 3, (0,0,0), -1)
            ss34=0

        if ss35<90:
            cv2.circle(gray_image,(sx[19],sy[19]), 3, (255,255,255), -1)
            ss35=1
        else:
            cv2.circle(gray_image,(sx[19],sy[19]), 3, (0,0,0), -1)
            ss35=0

        if ss36<90:
            cv2.circle(gray_image,(sx[20],sy[20]), 3, (255,255,255), -1)
            ss36=1
        else:
            cv2.circle(gray_image,(sx[20],sy[20]), 3, (0,0,0), -1)
            ss36=0

        if ss37<90:
            cv2.circle(gray_image,(sx[21],sy[21]), 3, (255,255,255), -1)
            ss37=1
        else:
            cv2.circle(gray_image,(sx[21],sy[21]), 3, (0,0,0), -1)
            ss37=0

        
        ss1sum=ss11+ss12+ss13+ss14+ss15+ss16+ss17
        ss2sum=ss21+ss22+ss23+ss24+ss25+ss26+ss27
        ss3sum=ss31+ss32+ss33+ss34+ss35+ss36+ss37
        ss1val=0
        ss2val=0
        ss3val=0
        print "ss1sum=%d" %ss1sum
        if ss1sum==2:
            ss1val=1
        elif ss1sum==3:
            ss1val=7
        elif ss1sum==4:
            ss1val=4
        elif ss1sum==5:
            if ss11==1:
                ss1val=5
            elif ss17==1:
                ss1val=3
            else:
                ss1val=2
        elif ss1sum==6:
            if ss13==1:
                if ss14==1:
                    ss1val=9
                else:
                    ss1val=0
            else:
                ss1val=6
        elif ss1sum==7:
            ss1val=8


        if ss2sum==2:
            ss2val=1
        elif ss2sum==3:
            ss2val=7
        elif ss2sum==4:
            ss2val=4
        elif ss2sum==5:
            if ss21==1:
                ss2val=5
            elif ss27==1:
                ss2val=3
            else:
                ss2val=2
        elif ss2sum==6:
            if ss23==1:
                if ss24==1:
                    ss2val=9
                else:
                    ss2val=0
            else:
                ss2val=6
        elif ss2sum==7:
            ss2val=8

        if ss3sum==2:
            ss3val=1
        elif ss3sum==3:
            ss3val=7
        elif ss3sum==4:
            ss3val=4
        elif ss3sum==5:
            if ss31==1:
                ss3val=5
            elif ss37==1:
                ss3val=3
            else:
                ss3val=2
        elif ss3sum==6:
            if ss33==1:
                if ss34==1:
                    ss3val=9
                else:
                    ss3val=0
            else:
                ss3val=6
        elif ss3sum==7:
            ss3val=8


        #print ss1val
        #print ss2val
        #print ss3val
       
        ssval=ss1val*10+ss2val+ss3val*0.1

        fo2 = open("readings.csv", 'a')
        fo2.write("%f" %(ssval))
        
        fo2.close()
        
        cv2.imwrite("cropped_image.png",gray_image)
        print ssval
        time.sleep(8)
    except KeyboardInterrupt:
        break
        del(camera)
