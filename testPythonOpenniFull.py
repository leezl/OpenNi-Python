'''
Short test file, may get longer
'''
from primesense import openni2
from primesense import _openni2 as c_api
#numpy, for matrix manipulation fo the images
import numpy as np
#matplotlib, for temporary display to check the images
import matplotlib.pyplot as plt
#alternate: 
#import cv2 #can display uint16 images (correctly load and store depth)

#takes frame data, and the type it is and displays the image
#frame_data = frame.get_buffer_as_blah(); thisType = numpy.someType
def print_frame(frame_data, thisType):
    #need to know what format to get the buffer in:
    # if color pixel type is RGB888, then it must be uint8, 
    #otherwise it will split the pixels incorrectly
    img  = np.frombuffer(frame_data, dtype=thisType)
    whatisit = img.size
    #QVGA is what my camera defaulted to, so: 1 x 480 x 640
    #also order was weird (1, 480, 640) not (640, 480, 1)
    if whatisit == (640*480*1):#QVGA
        img.shape = (1, 480, 640)
        #This order? Really? ^
        #shape it accordingly
        img = np.concatenate((img, img, img), axis=0)
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 0, 1)
    elif whatisit == (640*480*3):
        img.shape = (480, 640, 3)
        #these are, what is it, normalizsed?
    else:
        print "Frames are of size: ",img.size
    #images still appear to be reflected, but I don't need them to be correct in that way
    print img.shape
    #need both of follwoing: plt.imShow adds image to plot
    plt.imshow(img)
    #plt.show shows all the currently added figures
    #plt.show()
    plt.pause(0.1)
    plt.draw()
    plt.close()
    
def print_frames(frame_data, frame_data2, thisType, thisType2):
    img  = np.frombuffer(frame_data, dtype=thisType)
    whatisit = img.size
    print "Image size 1 ",whatisit
    if whatisit == (640*480*1): #QVGA, default
        img.shape = (1, 480, 640)
        #This order? Really? ^
        #shape it accordingly
        img = np.concatenate((img, img, img), axis=0)
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 0, 1)
    elif whatisit == (640*480*3):
        img.shape = (480, 640, 3)
        #these are, what is it, normalizsed?
    else:
        print "Frames are of size: ",img.size
    print img.shape
    plt.imshow(img)
    plt.show()
    
    img1  = np.frombuffer(frame_data2, dtype=thisType2)
    whatisit = img1.size
    print "Image size 2 ",whatisit
    if whatisit == (640*480*1): #QVGA, default
        img1.shape = (1, 480, 640)
        #This order? Really? ^
        #shape it accordingly
        img1 = np.concatenate((img1, img1, img1), axis=0)
        img1 = np.swapaxes(img1, 0, 2)
        img1 = np.swapaxes(img1, 0, 1)
    elif whatisit == (640*480*3):
        img1.shape = (480, 640, 3)
        img1 = np.swapaxes(img1, 0, 2)
        #these are, what is it, normalizsed?
    else:
        print "Frames are of size: ",img1.size
    print img1.shape
    plt.imshow(img1)
    
    plt.show()

openni2.initialize()     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
print dev.get_sensor_info(openni2.SENSOR_DEPTH)

print "testing depth "
depth_stream = dev.create_depth_stream()
'''depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 640, resolutionY = 480, fps = 30))
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
print_frame(frame_data, np.uint16)
depth_stream.stop()'''

'''print "Testing depth 2 "
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
print_frame(frame_data, np.uint16)
depth_stream.stop()'''

print "Testing Color "
color_stream = dev.create_color_stream()
'''color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30))
color_stream.start()
frame = color_stream.read_frame()
frame_data1 = frame.get_buffer_as_uint8()
print_frame(frame_data1, np.uint8)
color_stream.stop()'''

print "what?"
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 640, resolutionY = 480, fps = 30))
color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30))
print "Starting Streams"
depth_stream.start()
color_stream.start()
print "Read frames"
frame = depth_stream.read_frame()
frame1 = color_stream.read_frame()
print "Getting Buffer"
frame_data = frame.get_buffer_as_uint16()
frame_data1 = frame1.get_buffer_as_uint8()
print "Printing"
print_frames(frame_data, frame_data1, np.uint16, np.uint8)
depth_stream.stop()
color_stream.stop()

openni2.unload()
