import os, platform
os.system('xdg-open https://www.facebook.com/100011755265711')
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from XAI64  import void
 
        void()
 
 
 
elif bit == "32bit":
 
        from ET32 import void
 
 
        void()
 
