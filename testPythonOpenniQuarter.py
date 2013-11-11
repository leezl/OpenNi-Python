'''
Short test file, may get longer
'''
from primesense import openni2
from primesense import _openni2 as c_api
#numpy, for matrix manipulation fo the images
import numpy as np
#matplotlib, for temporary display to check the images
import matplotlib.pyplot as plt

#takes frame data, and the type it is and displays the image
#frame_data = frame.get_buffer_as_blah(); thisType = numpy.someType
def print_frame(frame_data, thisType):
    #need to know what format to get the buffer in:
    # if color pixel type is RGB888, then it must be uint8, 
    #otherwise it will split the pixels incorrectly
    img  = np.frombuffer(frame_data, dtype=thisType)
    whatisit = img.size
    #QVGA is what my camera defaulted to, so: 1 x 240 x 320
    #also order was weird (1, 240, 320) not (320, 240, 1)
    if whatisit == (320*240*1):#QVGA
        img.shape = (1, 240, 320)
        #This order? Really? ^
        #shape it accordingly
        img = np.concatenate((img, img, img), axis=0)
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 0, 1)
    elif whatisit == (320*240*3):
        img.shape = (240, 320, 3)
        #these are, what is it, normalizsed?
    elif whatisit == (640*480*1):
        img.shape = (1, 480, 640)
        #This order? Really? ^
        #shape it accordingly
        img = np.concatenate((img, img, img), axis=0)
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 0, 1)
    elif whatisit == (640*480*3):
        img.shape = (480,640,3)
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

openni2.initialize()     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
print dev.get_sensor_info(openni2.SENSOR_DEPTH)

print "testing depth "
depth_stream = dev.create_depth_stream()
#depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 320, resolutionY = 240, fps = 30))
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 640, resolutionY = 480, fps = 30))

print "Testing Color "
color_stream = dev.create_color_stream()
#color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 320, resolutionY = 240, fps = 30))
color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 640, resolutionY = 480, fps = 30))

print "Starting Streams"
depth_stream.start()
color_stream.start()
openni2.wait_for_any_stream([depth_stream])
openni2.wait_for_any_stream([color_stream])
print "Reading frames"
frame_depth = depth_stream.read_frame()
frame_color = color_stream.read_frame()
print "Getting Buffers"
frame_data_depth = frame_depth.get_buffer_as_uint16()
frame_data_color = frame_color.get_buffer_as_uint8()
print "Printing"
print_frame(frame_data_depth, np.uint16)
print_frame(frame_data_color, np.uint8)
depth_stream.stop()
color_stream.stop()

openni2.unload()