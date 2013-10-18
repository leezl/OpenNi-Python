README: OpenNI with Python Bindings
===================================

I have installed OpenNI 2.2 x64, NiTE2.2 x64, and primesense 2.2.0.30 (the python bindings) on an Ubuntu 12.10 system with an AMD Athlon(tm) X2 Dual-Core QL-64 × 2. This is an old computer.   
   
The current version of OpenNI (2.0 on) does not work with the Kinect. Liscencing Issues. They support their own cameras, and others, but if you want to use the Kinect (or PCL, or ROS) chance are you will be using earlier versions. These may not have supprot for the python bindings. I haven't checked.
   
NiTe does not work. It gives the error: Invalid Instruction for the samples, which seems to be a problem with older computers that do not support SSE 3 commands, which NiTE uses. *As seen [here](http://answers.ros.org/question/51211/openni_tracker-illegal-instruction/)*   
   
OpenNI seems to work. The python bindings seem to work. It is likely that some of them (those which rely on NiTE) will fail.    
   
If you have a newer/better computer this should not be an issue for you.   
   
I downloaded OpenNI, NiTE and primesense from the following links respectively:    
   
[OpenNI](http://www.openni.org/openni-sdk/)    
   
[NiTE](http://www.openni.org/files/nite/)   
   
[primesense](http://www.openni.org/files/python-bindings/)   

Once you have them in a directory (unpacked) install as instructed on the site, ie:

   > cd OpenNI-Linux-x64-2.2   
   > sudo ./install.sh   
   
The same for NiTE. For the python bidnings, after installing both OpenNI and NiTE:
   
   > cd primesense-2.2.0.30   
   > python setup.py install   
   
Make sure you have python installed.   
    
In order to run any of the code, chances are you will need to copy the contents of the OpenNi Redist/ folder into your project directory. I tried to get around this by adding that directory to the PATH and LD_LIBRARY_DIR variables, but it seems that the python bindings expect the OpenNI .so files to be right next to your code. This is probably fixable, I am not working on it now, so copy-paste.   
    
I included the primesense python code in this project so that I could add my own comments to it. These may or may not be helpful.   
