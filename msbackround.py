import subprocess
import hackthon
import time

networks=set(["AirBears.Berkeley"])

#import sys
#class nada():
	#def write(self, *args):
		#pass
#sys.stdout = nada()

def check_for_networks():
    process = subprocess.Popen(["ipconfig"],stdout= subprocess.PIPE)
    stdout,stderr = process.communicate()
    for network in networks:
        print("Checking if we're on %s" % network)
        if network in stdout:
            hackthon.connect()


if __name__ == "__main__":
	while 1:
		check_for_networks()
		time.sleep(1)

