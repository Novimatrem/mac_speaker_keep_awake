import subprocess
import time
import os 
dirname, filename = os.path.split(os.path.abspath(__file__))
print(dirname)
print(filename)
actualsoundname = dirname + "/warning-beep_distfix_FINAL.wav"
print(actualsoundname)
print("init"),
subprocess.Popen(["afplay", actualsoundname]),
    
while (True):
	{
    print("wokening"),
    subprocess.Popen(["afplay", actualsoundname]),
    time.sleep(9)
}

