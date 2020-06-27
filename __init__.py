import sys as _sys
import os  as _os

# Windows ADALM2000 Drivers
if _sys.platform in ['win32']:  
    try:    import libm2k as _m2k
    except: print('To use an ADALM2000 on Windows, you need to install the m2k/ADALM2000 drivers, libiio, and libm2k with python bindings.')

# OSX ADALM2000 Drivers
elif _sys.platform in ['darwin']: 
    print('No ADALM2000 on OSX yet.')
    _m2k = None

# Linux ADALM2000 Drivers
else:                         
    _sys.path.append(_os.path.join(__path__[0], 'libm2k', 'linux'))
    try: import libm2k as _m2k
    except: _m2k = None
        

# Test for VISA
try:    import visa as _v
except: 
    print('Visa driver and / or pyvisa not installed. On Windows, consider Rhode & Schwartz VISA or NI-VISA, then pip install pyvisa. On Linux, pip install pyvisa and pyvisa-py')
    _v = None
    
from . import visa_tools
from . import instruments
from . import data
from . import functions
from . import playground