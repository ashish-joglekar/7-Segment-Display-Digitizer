# 7-Segment-Display-Digitizer 
(Ashish Joglekar RBCCPS, IISc)
Digitize Instrument's display by recording data using a Webcam
This code was written to record data measured by a digital multimeter and store the readings in a csv file.  

1. When you first run this program you will see the image your webcam captured. Select the seven segment display segments you wish to digitize in clockwise order as shown below:
                                          2 _        9 _         16 _
                                          1|_| 3     8|_| 10     15|_| 17
                                            4         11           18
                                          5|_|7     12|_|14      19|_|21
                                            6          13           20
Once 21 points are selected the digitization will begin. You can see the output image "cropped_image". An 'ON' segment is indicated by a white circle while an 'OFF' segment is shown by a black circle.
You may need to adjust individual sement thresholds if your lighting is non uniform.

2. Current sampling time is 8 seconds. You may change it to your requirement

3. Result is printed and also saved in a file called readings.csv

4. Choose camera port correctly
