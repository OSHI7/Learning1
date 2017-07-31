from voipms import VoipMs
from datetime import datetime
import time
import matplotlib.pyplot as plt
import matplotlib
#dummy change; remove this

from Utils import  showModulePath

showModulePath(VoipMs)
#raise AssertionError("Unexpected value of 'distance'!", 11)
raise Exception('bad thing happened')


#Load the JSON file with pwrd
#client = VoipMs(, )
status=client.accounts.get.registration_status('136817_CELL3')
print(status)



from voipms import VoipMs
client = VoipMs('', '')
a=client.accounts.get.registration_status('136817_CELL3')
print('cell phone registered? ' + a['registered'])

'''
a=client.accounts.get.registration_status('136817_HOME')
print('home phone registered? ' + a['registered'])

a=client.accounts.get.registration_status('136817_CELL')
print('\defunct phone registered? ' + a['registered'])
'''

TIME_ARRAY=[]
REGISTRATION_ARRAY=[]

VOIPMS_LOGFILE='VoipMS_Logfile.csv'

with open(VOIPMS_LOGFILE, "a", newline="\r\n") as text_file:
    text_file.write('*'*10 + "\n")
    timeValue=datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    text_file.write('NEW LOG STARTED AT: ' + timeValue +'\n' )


i=-1
while 1:
    i=i+1
    timeValue=datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    TIME_ARRAY.append(timeValue) #Store the data

    # ref: https://stackoverflow.com/questions/26455616/how-can-i-create-basic-timestamps-or-dates-python-3-4
    x2 = [datetime.strptime(elem, '%Y-%m-%d, %H:%M:%S') for elem in TIME_ARRAY]
    dates=matplotlib.dates.date2num(x2)

    status=client.accounts.get.registration_status('136817_CELL3')
    #print('cell phone registered? ' + status['registered'])
    registerstatus= int(status['registered']=='yes')
    REGISTRATION_ARRAY.append(registerstatus)

    outstring=timeValue +  ", CellStatus , " + "{first}".format(first=registerstatus)
    print(outstring)

    #Append contents to file
    with open(VOIPMS_LOGFILE, "a", newline="\r\n") as text_file:
        text_file.write(outstring +'\n')

    #print(timeValue +  ", CellStatus= " + "{first}".format(first=registerstatus))

    #Update plot
    '''
    # ref https://stackoverflow.com/questions/11874767/real-time-plotting-in-while-loop-with-matplotlib
    plt.ion()
    matplotlib.pyplot.plot_date(dates, REGISTRATION_ARRAY)
    (fig, ax) = plt.subplots(1, 1)
    ax.plot(dates, REGISTRATION_ARRAY)
    fig.show()
    plt.pause(0.05)
    '''

    time.sleep(1)




