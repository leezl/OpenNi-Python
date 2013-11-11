OpenNI Python tests
====================
This is a small test section for playing with the python bindings for OpenNI.

Currently on my system:
Ubuntu 12.04
OpenNI 2.2
NiTE 2.2
Python Bindings (primsense) 2.2
Carmine 1.08 Camera

My computer is an old HP Pavilion dv6. I could not get the Camera working on a Lenovo Y500: After fixing the permissions errors (had to be root), I had timeout issues which may still be usb setting problems.

Strange Issues:
=====================
OpenNI and Python:
    *Color Streams appear strange it they are stopped, and then restarted.   
    *Color and Depth Syncing is cannot be activated   
        -> the function takes no parameters, but complains in the OpenNI code that a aparameter is wrong   
    *Color and Depth can be read at the same time in Quarter size, (320,240, :), or if depth is (640, 480, 1), but not if color is (640, 480, 3), regardless of what depth is. Note: Color can be read at this size by itself.   