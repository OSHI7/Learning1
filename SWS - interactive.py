# -*- coding: utf-8 -*-
"""
Drawing Stokes vectors in the Poincare sphere
"""

import numpy as np
from numpy import linspace, outer, cos, sin, size, zeros_like, ones, mean
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

from py_pol import degrees
from py_pol.stokes import Stokes
from py_pol.mueller import Mueller
#from py_pol.drawings import draw_poincare_sphere, draw_on_poincare
from py_pol.drawings import draw_on_poincare

def set_aspect_equal_3d(ax):
    """Fix equal aspect bug for 3D plots."""
    xlim = (-1, 1)
    ylim = (-1, 1)
    zlim = (-1, 1)

    xmean = mean(xlim)
    ymean = mean(ylim)
    zmean = mean(zlim)

    plot_radius = max([
        abs(lim - mean_)
        for lims, mean_ in ((xlim, xmean), (ylim, ymean), (zlim, zmean))
        for lim in lims
    ])

    factor = 1
    ax.set_xlim3d([xmean - factor * plot_radius, xmean + factor * plot_radius])
    ax.set_ylim3d([ymean - factor * plot_radius, ymean + factor * plot_radius])
    ax.set_zlim3d([zmean - 1 * plot_radius, zmean + 1 * plot_radius])

def draw_poincare_sphere(ax,
                         stokes_points=None,
                         angle_view=[0.5, -1],
                         is_normalized=True,
                         kind='line',
                         color='r',
                         label='',
                         filename=''):
    """Function to draw the poincare sphere.
    It admits Stokes or a list with Stokes, or None

    Parameters:
        stokes_points (Stokes, list, None): list of Stokes points.
        angle_view (float, float): Elevation and azimuth for viewing.
        is_normalized (bool): normalize intensity to 1.
        kind (str): 'line' or 'scatter'.
        color (str): color of line or scatter.
        label (str): labels for drawing.
        filename (str): name of filename to save the figure.
    """

    elev, azim = angle_view
    max_size = 1

    #fig = plt.figure(figsize=(6, 6))
    #ax = fig.add_subplot(111, projection='3d', adjustable='box')
    # ax.set_aspect('equal')

    u = linspace(0, 360 * degrees, 90)
    v = linspace(0, 180 * degrees, 90)

    x = 1 * outer(cos(u), sin(v))
    y = 1 * outer(sin(u), sin(v))
    z = 1 * outer(ones(size(u)), cos(v))

    ax.plot_surface(
        x,
        y,
        z,
        rstride=4,
        cstride=4,
        color='b',
        edgecolor="k",
        linewidth=.0,
        alpha=0.1)
    ax.plot(sin(u), cos(u), 0, color='k', linestyle='dashed', linewidth=0.5)
    ax.plot(
        sin(u),
        zeros_like(u),
        cos(u),
        color='k',
        linestyle='dashed',
        linewidth=0.5)
    ax.plot(
        zeros_like(u),
        sin(u),
        cos(u),
        color='k',
        linestyle='dashed',
        linewidth=0.5)

    ax.plot([-1, 1], [0, 0], [0, 0], 'k-.', lw=1, alpha=0.5)
    ax.plot([0, 0], [-1, 1], [0, 0], 'k-.', lw=1, alpha=0.5)
    ax.plot([0, 0], [0, 0], [-1, 1], 'k-.', lw=1, alpha=0.5)

    ax.plot(
        xs=(1, ),
        ys=(0, ),
        zs=(0, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)

    ax.plot(
        xs=(-1, ),
        ys=(0, ),
        zs=(0, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)
    ax.plot(
        xs=(0, ),
        ys=(1, ),
        zs=(0, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)
    ax.plot(
        xs=(0, ),
        ys=(-1, ),
        zs=(0, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)
    ax.plot(
        xs=(0, ),
        ys=(0, ),
        zs=(1, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)
    ax.plot(
        xs=(0, ),
        ys=(0, ),
        zs=(-1, ),
        color='black',
        marker='o',
        markersize=4,
        alpha=0.5)
    distance = 1.2
    ax.text(distance, 0, 0, 'Q', fontsize=18)
    ax.text(0, distance, 0, 'U', fontsize=18)
    ax.text(0, 0, distance, 'V', fontsize=18)

    if stokes_points is not None:
        draw_on_poincare(
            ax,
            stokes_points,
            is_normalized=is_normalized,
            kind=kind,
            color=color,
            label=label)

    ax.view_init(elev=elev / degrees, azim=azim / degrees)

    ax.set_xlabel('$S_1$', fontsize=22)
    ax.set_ylabel('$S_2$', fontsize=22)
    ax.set_zlabel('$S_3$', fontsize=22)
    ax.grid(False)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    ax.set_xlim(-max_size, max_size)
    ax.set_ylim(-max_size, max_size)
    ax.set_zlim(-max_size, max_size)

    plt.tight_layout()
    set_aspect_equal_3d(ax)
    if filename not in (None, [], ''):
        plt.savefig(filename)
    #return ax, fig



#################### Stokes definitions

V=Stokes('V')
V.from_elements(1, -1, 0, 0)

H=Stokes('H')
H.linear_light(angle=0, intensity=1)

wavelength_center = 1550 # nm
wavelength = np.arange(1510, 1631, 20) #nm
alfa = wavelength_center*np.pi/(wavelength)
alfa_1510 = wavelength_center*np.pi/(1510)
alfa_1550 = wavelength_center*np.pi/(1550)
alfa_1630 = wavelength_center*np.pi/(1630)
angles = np.linspace(0, 180 * degrees, 90)

HWP = Mueller("HWP")
HWP.half_waveplate(np.pi/4)
HWP1 = Mueller("HWP")
HWP1.retarder_linear(alfa_1510, np.pi/4)
HWP2 = Mueller("HWP")
HWP2.retarder_linear(alfa_1550, np.pi/4)
HWP3 = Mueller("HWP")
HWP3.retarder_linear(alfa_1630, np.pi/4)

HWP45 = Mueller("HWP")
HWP45.half_waveplate(np.pi/8)
HWP451 = Mueller("HWP")
HWP451.retarder_linear(alfa_1510, np.pi/8)
HWP452 = Mueller("HWP")
HWP452.retarder_linear(alfa_1550, np.pi/8)
HWP453 = Mueller("HWP")
HWP453.retarder_linear(alfa_1630, np.pi/8)

QWP = Mueller("QWP")
QWP.quarter_waveplate(np.pi/4)
QWP1 = Mueller("QWP")
QWP1.retarder_linear(alfa_1510/2, np.pi/4)
QWP2 = Mueller("QWP")
QWP2.retarder_linear(alfa_1550/2, np.pi/4)
QWP3 = Mueller("QWP")
QWP3.retarder_linear(alfa_1630/2, np.pi/4)

MVac = Mueller('Vacuum')
MVac.vacuum()


def sim(retardance, angle_rotation, pdl, angle_artifact):
    ######## Variables
    
    retardance = retardance*np.pi
    angle_rotation = angle_rotation*np.pi
    angle_artifact = angle_artifact*np.pi
    
    MA = Mueller('Arbitrary')
    MA.retarder_linear(retardance, angle_rotation)
    
    MD = Mueller('Diattenuator')
    MD.diattenuator_linear(1, np.sqrt(10**(-pdl/10)), angle=angle_artifact)
    
    M = MD*MA
    
    ###################################################################
    #H1 = M*HWP1*V
    H2 = M*HWP2*V
    #H3 = M*HWP3*V
    
    #D1 = M*HWP451*V
    D2 = M*HWP452*V
    #D3 = M*HWP453*V
    
    #L1 = M*QWP1*V
    L2 = M*QWP2*V
    #L3 = M*QWP3*V
    
    TH = []
    TL = []
    TD = []
    
    H_points = []
    L_points = []
    D_points = []
    
    for a in alfa:
        HWP = Mueller("HWP")
        HWP.retarder_linear(a, np.pi/4)
    
        HWP45 = Mueller("HWP")
        HWP45.retarder_linear(a, np.pi/8)
        
        QWP = Mueller("HWP")
        QWP.retarder_linear(a/2, np.pi/4)
        
        H_a = HWP*V
        H_a = M*H_a
        
        L_a = QWP*V
        L_a = M*L_a
        
        D_a = HWP45*V
        D_a = M*D_a
    
        H_points.append(H_a)
        L_points.append(L_a)
        D_points.append(D_a)
        
        th = H_a.parameters.intensity()
        tl = L_a.parameters.intensity()
        td = D_a.parameters.intensity()
        
        TH.append(th)
        TL.append(tl)
        TD.append(td)
        
        H_points.append(H_a)
        L_points.append(L_a)
        D_points.append(D_a)
    
    TV = (M*V).parameters.intensity()
    TH = np.array(TH)
    TL = np.array(TL)
    TD = np.array(TD)
    
    beta = np.cos(wavelength_center*np.pi/(2.0*wavelength))	# wavelength first correction factor
    miu = np.sin(wavelength_center*np.pi/wavelength)		# wavelength second correction factor
    m00 = ((1 + beta*miu)*TV - miu*TL + TH)/(2.0 - (1 - beta)*miu)
    m01 = ((1 - miu)*TV + miu*TL - TH)/(2.0 - (1 - beta)*miu)
    m03 =	(2*TL - (1 + beta)*TV - (1 - beta)*TH)/(2.0 - miu*(1 - beta))
    m02 = TD - m00 - (miu/np.sqrt(2.0))*m03
    delta = np.sqrt(m01*m01 + m02*m02 + m03*m03)
    
    
    ILMin = 10*np.log10(m00 - delta)
    ILMax = 10*np.log10(m00 + delta)
    ILAVE = 10*np.log10(m00)
    PDL = 10*np.log10((m00 + delta)/(m00 - delta))
    
    
    ILAVE_Theo = 10*np.log10(M.parameters.mean_transmission())
    ILAVE_simple = 10*np.log10((TV + TH)/2)
    
    c = np.cos(wavelength_center*np.pi/(wavelength))
    s = np.sin(wavelength_center*np.pi/(wavelength))
    ILAVE_corrected2 = 10*np.log10((TH - TV*(c+s))/(1-c-s))
    
    return TL, TV, TH, TD, ILAVE_Theo, ILMax, ILMin, ILAVE, ILAVE_simple, \
           ILAVE_corrected2, H2, L2, D2, H_points, L_points, D_points, PDL, M
    ###################################################################


fig = plt.figure(figsize=(16,10))

retardance = 0*np.pi
angle_rotation = 0*np.pi
pdl = 0.1 # dB
angle_artifact = 0*np.pi

results = sim(retardance, angle_rotation, pdl, angle_artifact)
TL, TV, TH, TD, ILAVE_Theo, ILMax, ILMin, ILAVE, ILAVE_simple, ILAVE_corrected2, H2, L2, D2, H_points, L_points, D_points, PDL, M = results


ax1 = plt.subplot(231)
tlp, = plt.plot(wavelength, 10*np.log10(TL), label='S1 - L')
tvp, = plt.plot(wavelength, 10*np.log10(TV*np.ones(wavelength.size)), label='S2 - V')
thp, = plt.plot(wavelength, 10*np.log10(TH), label='S3 - H')
tdp, = plt.plot(wavelength, 10*np.log10(TD), label='S4 - D')
ILAVE_Theop1 = plt.axhline(ILAVE_Theo, ls='--', color='k')
plt.xlabel('Wavelength (nm)')
plt.ylabel('IL (dB)')
plt.legend(fontsize=8)


ax2 = plt.subplot(232)
ILMaxp, = plt.plot(wavelength, ILMax, label='ILMax')
ILMinp, = plt.plot(wavelength, ILMin, label='ILMin')
ILAVEp, = plt.plot(wavelength, ILAVE, label='ILAVE')
ILAVE_Theop2 = plt.axhline(ILAVE_Theo, ls='--', color='k')
plt.xlabel('Wavelength (nm)')
plt.ylabel('IL (dB)')
plt.legend(fontsize=8)


ax3 = plt.subplot(233)
ILAVEp2, = plt.plot(wavelength, ILAVE, '--', label='ILAVE Corrected S1S2S3 ')
ILAVE_simplep, = plt.plot(wavelength, ILAVE_simple, '--', label='Simple ILAVE S2S3')
ILAVE_corrected2p, = plt.plot(wavelength, ILAVE_corrected2, '--', label='ILAVE Corrected S2S3')
ILAVE_Theop3 = plt.axhline(ILAVE_Theo, ls='--', color='k')
plt.xlabel('Wavelength (nm)')
plt.ylabel('IL (dB)')
plt.legend(fontsize=8)



ax4 = fig.add_subplot(234, projection='3d', adjustable='box')
#ax, fig = draw_poincare_sphere(stokes_points=None)
draw_poincare_sphere(ax4, stokes_points=None)
draw_on_poincare(ax4,M*V, kind='scatter', color='DarkRed', label='V', is_normalized=False)
draw_on_poincare(ax4,H2, kind='scatter', color='g', label='H', is_normalized=False)
draw_on_poincare(ax4,L2, kind='scatter', color='b', label='L', is_normalized=False)
draw_on_poincare(ax4,D2, kind='scatter', color='y', label='D', is_normalized=False)
#draw_on_poincare(ax,[M*V, H_points[-1]], kind='line', color='DarkRed', label='', is_normalized=False)
#draw_on_poincare(ax,[M*V, H_points[0]], kind='line', color='DarkRed', label='', is_normalized=False)
draw_on_poincare(ax4,H_points, kind='line', color='g', label='H variation', is_normalized=False)
draw_on_poincare(ax4,L_points, kind='line', color='b', label='L variation', is_normalized=False)
draw_on_poincare(ax4,D_points, kind='line', color='y', label='D variation', is_normalized=False)
plt.legend(fontsize=8)
plt.tight_layout()




ax5 = plt.subplot(235)
ILAVE_errorp, = plt.plot(wavelength, ILAVE_Theo-ILAVE, '--', label='ILAVE Corrected S1S2S3 ')
ILAVE_simple_errorp, = plt.plot(wavelength, ILAVE_Theo-ILAVE_simple, '--', label='Simple ILAVE S2S3')
ILAVE_corrected2_errorp, = plt.plot(wavelength, ILAVE_Theo-ILAVE_corrected2, '--', label='ILAVE Corrected S2S3')
plt.axhline(0, ls='--', color='k')
plt.xlabel('Wavelength (nm)')
plt.ylabel('IL Error (dB)')
plt.legend(fontsize=8)


ax6 = plt.subplot(236)
PDLp, = plt.plot(wavelength, PDL, label='PDL')
pdlp = plt.axhline(pdl, ls='--', color='k')
plt.xlabel('Wavelength (nm)')
plt.ylabel('PDL (dB)')
plt.legend(fontsize=8)
plt.tight_layout()

#plt.subplot(234)
plt.subplots_adjust(bottom=0.28)
axcolor = 'lightgoldenrodyellow'
axretardance = plt.axes([0.25, 0.05, 0.65, 0.01], facecolor=axcolor)
axangle_rotation = plt.axes([0.25, 0.10, 0.65, 0.01], facecolor=axcolor)
axpdl = plt.axes([0.25, 0.15, 0.65, 0.01], facecolor=axcolor)
axangle_artifact = plt.axes([0.25, 0.20, 0.65, 0.01], facecolor=axcolor)

sretardance = Slider(axretardance, r'Retardance /$\pi$', 0, 2, valinit=retardance, valstep=0.05)
sangle_rotation = Slider(axangle_rotation, r'Angle /$\pi$',  0, 2, valinit=angle_rotation, valstep=0.05)
spdl = Slider(axpdl, 'DUT PDL /dB',  0, 5, valinit=pdl, valstep=0.1)
sangle_artifact = Slider(axangle_artifact, r'DUT Angle /$\pi$',  0, 2, valinit=angle_artifact, valstep=0.05)
 



def update(val):
    retardance = sretardance.val
    angle_rotation = sangle_rotation.val
    pdl = spdl.val
    angle_artifact = sangle_artifact.val
    
    results = sim(retardance, angle_rotation, pdl, angle_artifact)
    TL, TV, TH, TD, ILAVE_Theo, ILMax, ILMin, ILAVE, ILAVE_simple, ILAVE_corrected2, H2, L2, D2, H_points, L_points, D_points, PDL, M = results

    tlp.set_ydata(10*np.log10(TL))
    tvp.set_ydata(10*np.log10(TV*np.ones(wavelength.size)))
    thp.set_ydata(10*np.log10(TH))
    tdp.set_ydata(10*np.log10(TD))
    ILAVE_Theop1.set_data(([0, 1], [ILAVE_Theo, ILAVE_Theo]))
    ILMaxp.set_ydata(ILMax)
    ILMinp.set_ydata(ILMin)
    ILAVEp.set_ydata(ILAVE)
    ILAVE_Theop2.set_data(([0, 1], [ILAVE_Theo, ILAVE_Theo]))
    ILAVEp2.set_ydata(ILAVE)
    ILAVE_simplep.set_ydata(ILAVE_simple)
    ILAVE_corrected2p.set_ydata(ILAVE_corrected2)
    ILAVE_Theop3.set_data(([0, 1], [ILAVE_Theo, ILAVE_Theo]))
    
    ILAVE_errorp.set_ydata(ILAVE_Theo-ILAVE)
    ILAVE_simple_errorp.set_ydata(ILAVE_Theo-ILAVE_simple)
    ILAVE_corrected2_errorp.set_ydata(ILAVE_Theo-ILAVE_corrected2)
    PDLp.set_ydata(PDL)
    pdlp.set_data(([0, 1], [pdl, pdl]))

    #fig.delaxes(ax4)

    ax1.relim()        # Recalculate limits
    ax1.autoscale_view(True,True,True) #Autoscale
 
    ax2.relim()        # Recalculate limits
    ax2.autoscale_view(True,True,True) #Autoscale
    
    ax3.relim()        # Recalculate limits
    ax3.autoscale_view(True,True,True) #Autoscale
    
    # ax4.relim()        # Recalculate limits
    # ax4.autoscale_view(True,True,True) #Autoscale
    
    ax5.relim()        # Recalculate limits
    ax5.autoscale_view(True,True,True) #Autoscale

    ax6.relim()        # Recalculate limits
    ax6.autoscale_view(True,True,True) #Autoscale


    ax4.clear()
    #ax, fig = draw_poincare_sphere(stokes_points=None)
    draw_poincare_sphere(ax4, stokes_points=None)
    draw_on_poincare(ax4,M*V, kind='scatter', color='DarkRed', label='V', is_normalized=False)
    draw_on_poincare(ax4,H2, kind='scatter', color='g', label='H', is_normalized=False)
    draw_on_poincare(ax4,L2, kind='scatter', color='b', label='L', is_normalized=False)
    draw_on_poincare(ax4,D2, kind='scatter', color='y', label='D', is_normalized=False)
    #draw_on_poincare(ax,[M*V, H_points[-1]], kind='line', color='DarkRed', label='', is_normalized=False)
    #draw_on_poincare(ax,[M*V, H_points[0]], kind='line', color='DarkRed', label='', is_normalized=False)
    draw_on_poincare(ax4,H_points, kind='line', color='g', label='H variation', is_normalized=False)
    draw_on_poincare(ax4,L_points, kind='line', color='b', label='L variation', is_normalized=False)
    draw_on_poincare(ax4,D_points, kind='line', color='y', label='D variation', is_normalized=False)
    ax4.legend(fontsize=8)
    
    plt.subplots_adjust(bottom=0.28)

    fig.canvas.draw_idle()


sretardance.on_changed(update)
sangle_rotation.on_changed(update)
spdl.on_changed(update)
sangle_artifact.on_changed(update)

resetax = plt.axes([0.05, 0.1, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sretardance.reset()
    sangle_rotation.reset()
    spdl.reset()
    sangle_artifact.reset()
button.on_clicked(reset)

plt.subplots_adjust(bottom=0.28)

plt.show()


