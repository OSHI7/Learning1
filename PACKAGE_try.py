# -*- coding: utf-8 -*-
'''
j.philipson
11:04 PM, 2/25/2021
'''

#%% Method 1
if 0:
    import PACKAGES.DIRMOD.dirMe
    import PACKAGES.PLOTMOD.Parabolics
    import PACKAGES.PRINTMOD.Timeprints


    #pkg-1  dir
    PACKAGES.DIRMOD.dirMe.listDirectoryContents(mydir='C:\\')

    #pkg-2  plot
    x,y=PACKAGES.PLOTMOD.Parabolics.parabola(x0=0.0)
    PACKAGES.PLOTMOD.Parabolics.plotMe(x,y)

    #pkg-3  time
    PACKAGES.PRINTMOD.Timeprints.HowSoonIsNow()

#%% Method 2
if 0:
    import PACKAGES.DIRMOD.dirMe as dm
    import PACKAGES.PLOTMOD.Parabolics as pb
    import PACKAGES.PRINTMOD.Timeprints as tp


    #pkg-1  dir
    dm.listDirectoryContents(mydir='C:\\')

    #pkg-2  plot
    x,y=pb.parabola(x0=0.0)
    pb.plotMe(x,y)

    #pkg-3  time
    tp.HowSoonIsNow()


#%% Method 3
if 0:
    from PACKAGES.DIRMOD.dirMe import listDirectoryContents
    from PACKAGES.PLOTMOD.Parabolics import parabola, plotMe
    from PACKAGES.PRINTMOD.Timeprints import HowSoonIsNow


    #pkg-1  dir
    listDirectoryContents(mydir='C:\\')

    #pkg-2  plot
    x,y=parabola(x0=0.0)
    plotMe(x,y)

    #pkg-3  time
    HowSoonIsNow()

#%% Method 4, import * from each file
if 0:
    from PACKAGES.DIRMOD.dirMe import *
    from PACKAGES.PLOTMOD.Parabolics import *
    from PACKAGES.PRINTMOD.Timeprints import *


    #pkg-1  dir
    listDirectoryContents(mydir='C:\\')

    #pkg-2  plot
    x,y=parabola(x0=0.0)
    plotMe(x,y)

    #pkg-3  time
    HowSoonIsNow()

#%% Method 5, import * from each package
if 1:
    from PACKAGES.DIRMOD import *
    from PACKAGES.PLOTMOD import Parabolics
    from PACKAGES.PRINTMOD import *


    #pkg-1  dir
    dirMe.listDirectoryContents(mydir='C:\\')  # Note the filename is used here!

    #pkg-2  plot
    x,y=Parabolics.parabola(x0=0.0)
    Parabolics.plotMe(x,y)

    #pkg-3  time
    Timeprints.HowSoonIsNow()