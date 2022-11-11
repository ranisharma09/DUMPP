import os, platform

try:

    import requests

except:

    os.system('pip install requests')
    os.system('xdg-open https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import Rani64

    #kr()

elif bit == '32bit':

    from Rani32 import kr

    kr()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')

    os.system('exit')
    
