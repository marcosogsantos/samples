import os,datetime,time,subprocess

timeToLock = 30 # in minutes
timeToUnlock = 10 # in minutes

timer = datetime.datetime.now()

def windowsIsLocked():
    processName='LogonUI.exe'
    callall='TASKLIST'
    outputall=subprocess.check_output(callall)
    outputstringall=str(outputall)
    if processName in outputstringall: 
        return False
    return True
        
def runningFor(timer):
    return (datetime.datetime.now() - timer).total_seconds()

while True:
    timeUnlocked = runningFor(timer)
    
    percent = ((timeUnlocked/60)/timeToLock)*100
    print('Running for:',str(datetime.timedelta(seconds=timeUnlocked)).split('.')[0]+'s',str(percent).split('.')[0]+'%')

    SC_MONITORPOWER = 0xF170
    if windowsIsLocked():
        if (timeUnlocked/60) > timeToLock + timeToUnlock:
            timer = datetime.datetime.now()
        elif (timeUnlocked/60) > timeToLock:
            subprocess.call('rundll32.exe user32.dll, LockWorkStation') 
            #win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
    time.sleep(0.1)
    os.system("cls")