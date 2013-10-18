'''
Short test file, may get longer
'''
from primesense import openni2
from primesense import _openni2 as c_api
#numpy, for matrix manipulation fo the images
import numpy as np
#matplotlib, for temporary display to check the images
import matplotlib.pyplot as plt

'''
Starter test program
'''

from primesense import openni2
from primesense import _openni2 as c_api
import numpy as np
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
        #shape it accordingly, that is, 1048576=1024*1024
        img.shape = (1, 240, 320)#small chance these may be reversed in certain apis...This order? Really?
        #filling rgb channels with duplicates so matplotlib can draw it (expects rgb)
        img = np.concatenate((img, img, img), axis=0)
        #because the order is so weird, rearrange it (third dimension must be 3 or 4)
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 0, 1)
    elif whatisit == (320*240*3):
        #color is miraculously in this order
        img.shape = (240, 320, 3)
    else:
        print "Frames are of size: ",img.size

    #images still appear to be reflected, but I don't need them to be correct in that way
    print img.shape
    #need both of follwoing: plt.imShow adds image to plot
    plt.imshow(img)
    #plt.show shows all the currently added figures
    plt.show()

openni2.initialize()     # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
print dev.get_sensor_info(openni2.SENSOR_DEPTH)

depth_stream = dev.create_depth_stream()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM, resolutionX = 320, resolutionY = 240, fps = 30))
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
print_frame(frame_data, np.uint16)
depth_stream.stop()

depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM, resolutionX = 320, resolutionY = 240, fps = 30))
depth_stream.start()
frame = depth_stream.read_frame()
frame_data = frame.get_buffer_as_uint16()
print_frame(frame_data, np.uint16)
depth_stream.stop()

print "Testing Color "
color_stream = dev.create_color_stream()
color_stream.set_video_mode(c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888, resolutionX = 320, resolutionY = 240, fps = 30))
color_stream.start()
frame = color_stream.read_frame()
frame_data1 = frame.get_buffer_as_uint8()
print_frame(frame_data1, np.uint8)
color_stream.stop()

openni2.unload()
