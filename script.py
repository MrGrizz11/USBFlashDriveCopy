from time import sleep
import win32api
import win32file
import copyusb


def target():
    drives = win32api.GetLogicalDriveStrings().split('\x00')[: -1]
    for device in drives:
        type = win32file.GetDriveType(device)
        if (type == 2):
            return 1


def search_target():
    global location
    while target() == None:
        print("TARGET NOT FOUND")
        sleep(3)
        print("SEARCHING TARGET..")
        sleep(10)
        target()
    else:
        sleep(2)
        print("TARGET FOUNDED")
        sleep(1)
        print(" -- START COPYING -- ")
        sleep(2)
        
        copyusb.copy()
        if (target() == None):
            search_target()


search_target()

print(location)
sleep(5)
