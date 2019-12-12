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


def keyboard():
    ## DROP TO KEYBOARD in the middle of a script. If you have iPYTHON SETUP can do this.
    # Ref: https://stackoverflow.com/questions/2158097/drop-into-python-interpreter-while-executing-function
    IPython.embed(header='WELCOME, keyboard() (exit to go back)')
