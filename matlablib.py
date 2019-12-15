import time
import IPython


# ref: https://stackoverflow.com/questions/5849800/what-is-the-python-equivalent-of-matlabs-tic-and-toc-functions
def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time() # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti # returns the time difference

TicToc = TicTocGenerator() # create an instance of the TicTocGen generator

# This will be the main function through which we define both tic() and toc()

def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print( "Elapsed time: %f seconds.\n" %tempTimeInterval )

def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)

def closefigures(plt):
    a=[plt.close(x) for x in range(1,100)] #bit dumb..how can i cound total # of figures?



def cc():
    import matplotlib.pyplot
    from IPython.testing.globalipapp import get_ipython  # https://pmbaumgartner.github.io/blog/testing-ipython-magics/
    ip = get_ipython()

    matplotlib.pyplot.close("all")

    #IPython.get_ipython().run_line_magic('reset', " -f in") # ref: https://ipython.readthedocs.io/en/stable/interactive/magics.html
    ip.run_line_magic('reset', " -f in") # short form works


def keyboard():
    ## DROP TO KEYBOARD in the middle of a script. If you have iPYTHON SETUP can do this.
    # Ref: https://stackoverflow.com/questions/2158097/drop-into-python-interpreter-while-executing-function
    IPython.embed(header='WELCOME, keyboard() (exit to go back)')

def quit_early():
    raise Exception('Halt', 'drop to keyboard')

class StopExecution(Exception):
    import sys
    #sys.tracebacklimit = 0 # ref: https://stackoverflow.com/questions/28413104/stop-python-script-without-killing-the-python-process
    def __init(self):
        pass
    def __str__(self):
        return ''

    def _render_traceback_(self):
        pass

    import sys, traceback, os

def kill_background():
    # Kill python background tasks if gets hung up in pycharm
    import os
    os.system('tskill python')

def kill():
    kill_background()



