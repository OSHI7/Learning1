from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph import PlotWidget, plot
from pyqtgraph.opengl import GLViewWidget
import random
import sys  # We need sys so that we can pass argv to QApplication
import os

import numpy as np
from py_pol import degrees
from py_pol.stokes import Stokes
from py_pol.mueller import Mueller

# pg.setConfigOption('background', 'w')

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('sws_simulator.ui', self)

        #################### Stokes definitions

        self.V=Stokes('V')
        self.V.from_elements(1, -1, 0, 0)

        self.H=Stokes('H')
        self.H.linear_light(angle=0, intensity=1)

        self.wavelength_center = 1550 # nm
        self.wavelength = np.arange(1510, 1630, 5) #nm
        self.alfa = self.wavelength_center*np.pi/(self.wavelength)
        alfa_1510 = self.wavelength_center*np.pi/(1510)
        alfa_1550 = self.wavelength_center*np.pi/(1550)
        alfa_1630 = self.wavelength_center*np.pi/(1630)
        self.angles = np.linspace(0, 180 * degrees, 90)

        self.HWP = Mueller("HWP")
        self.HWP.half_waveplate(np.pi/4)
        self.HWP1 = Mueller("HWP")
        self.HWP1.retarder_linear(alfa_1510, np.pi/4)
        self.HWP2 = Mueller("HWP")
        self.HWP2.retarder_linear(alfa_1550, np.pi/4)
        self.HWP3 = Mueller("HWP")
        self.HWP3.retarder_linear(alfa_1630, np.pi/4)

        self.HWP45 = Mueller("HWP")
        self.HWP45.half_waveplate(np.pi/8)
        self.HWP451 = Mueller("HWP")
        self.HWP451.retarder_linear(alfa_1510, np.pi/8)
        self.HWP452 = Mueller("HWP")
        self.HWP452.retarder_linear(alfa_1550, np.pi/8)
        self.HWP453 = Mueller("HWP")
        self.HWP453.retarder_linear(alfa_1630, np.pi/8)

        self.QWP = Mueller("QWP")
        self.QWP.quarter_waveplate(np.pi/4)
        self.QWP1 = Mueller("QWP")
        self.QWP1.retarder_linear(alfa_1510/2, np.pi/4)
        self.QWP2 = Mueller("QWP")
        self.QWP2.retarder_linear(alfa_1550/2, np.pi/4)
        self.QWP3 = Mueller("QWP")
        self.QWP3.retarder_linear(alfa_1630/2, np.pi/4)

        self.MVac = Mueller('Vacuum')
        self.MVac.vacuum()

        self.sINRetardance_label.setText(u'Input Retardance')
        self.sINAngle_label.setText(u'Input Angle')
        self.sINRotAngle_label.setText(u'Input Rot. Angle',)

        self.sDUTRetardance_label.setText(u'DUT Retardance')
        self.sDUTAngle_label.setText(u'DUT Angle')
        self.sDUTPDL_label.setText(u'DUT PDL',)

        # self._label.setAlignment(Qt.AlignCenter)
        # self._value.setAlignment(Qt.AlignCenter)

        self.sDUTAngle.setMinimum(0)
        self.sDUTPDL.setMinimum(0)
        self.sDUTRetardance.setMinimum(0)
        self.sINAngle.setMinimum(0)
        self.sINRetardance.setMinimum(0)
        self.sINRotAngle.setMinimum(0)

        self.sDUTAngle.setMaximum(100)
        self.sDUTPDL.setMaximum(300)
        self.sDUTRetardance.setMaximum(100)
        self.sINAngle.setMaximum(100)
        self.sINRetardance.setMaximum(100)
        self.sINRotAngle.setMaximum(100)

        self.sDUTAngle.setSingleStep(1)
        self.sDUTPDL.setSingleStep(1)
        self.sDUTRetardance.setSingleStep(1)
        self.sINAngle.setSingleStep(1)
        self.sINRetardance.setSingleStep(1)
        self.sINRotAngle.setSingleStep(1)

        self.sDUTAngle.setValue(0)
        self.sDUTPDL.setValue(8)
        self.sDUTRetardance.setValue(0)
        self.sINAngle.setValue(0)
        self.sINRetardance.setValue(0)
        self.sINRotAngle.setValue(0)


        self.resetButton.clicked.connect(self.reset)
        self.playButton.clicked.connect(self.play)

        self.sDUTAngle.valueChanged.connect(self.update)
        self.sDUTPDL.valueChanged.connect(self.update)
        self.sDUTRetardance.valueChanged.connect(self.update)
        self.sINAngle.valueChanged.connect(self.update)
        self.sINRetardance.valueChanged.connect(self.update)
        self.sINRotAngle.valueChanged.connect(self.update)

        self.sim()


        ###################### GL 3D View
        self.radius_scale = 3.0

        ### Axes
        glaxesn = gl.GLAxisItem()
        glaxesn.setSize(x=-10, y=-10, z=-10, size=None)
        glaxesp = gl.GLAxisItem()
        glaxesp.setSize(x=10, y=10, z=10, size=None)
        self.ax4.addItem(glaxesn)
        self.ax4.addItem(glaxesp)

#        ## create three grids, add each to the view
#        xgrid = gl.GLGridItem()
#        ygrid = gl.GLGridItem()
#        zgrid = gl.GLGridItem()
#        self.ax4.addItem(xgrid)
#        self.ax4.addItem(ygrid)
#        self.ax4.addItem(zgrid)
#
#        ## rotate x and y grids to face the correct direction
#        xgrid.rotate(90, 0, 1, 0)
#        ygrid.rotate(90, 1, 0, 0)
#
#        ## scale each grid differently
#        xgrid.scale(0.32, 0.32, 0.32)
#        ygrid.scale(0.32, 0.32, 0.32)
#        zgrid.scale(0.32, 0.32, 0.32)
#        xgrid.translate(-self.radius_scale*1.1,0,0)
#        ygrid.translate(0,-self.radius_scale*1.1,0)
#        zgrid.translate(0,0,-self.radius_scale*1.1)

        ### Poincare Sphere
        md = gl.MeshData.sphere(rows=20, cols=20, radius=self.radius_scale)
        PoincareSphere = gl.GLMeshItem(meshdata=md, smooth=True, drawFaces=False, drawEdges=True, edgeColor=(0.2,0.2,0.2,0.1))
        self.ax4.addItem(PoincareSphere)

        ### Stokes points
        self.pos = np.empty((10, 3))
        size = np.ones((10))*0.2
        color = np.empty((10, 4))
        # name = np.empty((10, 1))

        a = (self.M*self.V).get()*self.radius_scale
        self.pos[0] = (float(a[1]),float(a[2]),float(a[3]))
        color[0] = (1.0, 0.0, 0.0, 1.0)
        # name[0]='V'

        a = self.H1.get()*self.radius_scale
        self.pos[1] = (float(a[1]),float(a[2]),float(a[3]))
        color[1] = (0.0, 0.0, 1.0, 1.0)
        size[1] = 0.1
        # name[1]='H1'

        a = self.H2.get()*self.radius_scale
        self.pos[2] = (float(a[1]),float(a[2]),float(a[3]))
        color[2] = (0.0, 0.0, 1.0, 1.0)
        # name[2]='H'

        a = self.H3.get()*self.radius_scale
        self.pos[3] = (float(a[1]),float(a[2]),float(a[3]))
        color[3] = (0.0, 0.0, 1.0, 1.0)
        size[3] = 0.1
        # name[3]='H3'
        
        ##### L
        a = self.L1.get()*self.radius_scale
        self.pos[4] = (float(a[1]),float(a[2]),float(a[3]))
        color[4] = (0.0, 1.0, 0.0, 1.0)
        size[4] = 0.1
        # name[4]='L1'

        a = self.L2.get()*self.radius_scale
        self.pos[5] = (float(a[1]),float(a[2]),float(a[3]))
        color[5] = (0.0, 1.0, 0.0, 1.0)
        # name[5]='L'
        
        a = self.L3.get()*self.radius_scale
        self.pos[6] = (float(a[1]),float(a[2]),float(a[3]))
        color[6] = (0.0, 1.0, 0.0, 1.0)
        size[6] = 0.1
        # name[6]='L3'

        ##### D
        a = self.D1.get()*self.radius_scale
        self.pos[7] = (float(a[1]),float(a[2]),float(a[3]))
        color[7] = (1.0, 1.0, 0.0, 1.0)
        size[7] = 0.1
        # name[7]='D1'

        a = self.D2.get()*self.radius_scale
        self.pos[8] = (float(a[1]),float(a[2]),float(a[3]))
        color[8] = (1.0, 1.0, 0.0, 1.0)
        # name[8]='D'

        a = self.D3.get()*self.radius_scale
        self.pos[9] = (float(a[1]),float(a[2]),float(a[3]))
        color[9] = (1.0, 1.0, 0.0, 1.0)
        size[9] = 0.1
        # name[9]='D3'

        self.Stokes = gl.GLScatterPlotItem(pos=self.pos, size=size, color=color, pxMode=False)
        self.ax4.addItem(self.Stokes)


        self.ax1.addLegend(offset=(10, -10))
        self.ax1.setTitle('SWS Traces')
        self.ax1.setRange(xRange=[1490/1e9,1630/1e9])
        self.ax1p1 = self.ax1.plot(self.wavelength/1e9, 10*np.log10(self.TL), name='S1:L', pen=pg.mkPen('g', width=3))
        self.ax1p2 = self.ax1.plot(self.wavelength/1e9, 10*np.log10(self.TV*np.ones(self.wavelength.size)), name='S2:V', pen=pg.mkPen('r', width=3))
        self.ax1p3 = self.ax1.plot(self.wavelength/1e9, 10*np.log10(self.TH), name='S3:H', pen=pg.mkPen('b', width=3))
        self.ax1p4 = self.ax1.plot(self.wavelength/1e9, 10*np.log10(self.TD), name='S4:D', pen=pg.mkPen('y', width=3))
        self.ax1p5 = self.ax1.plot(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo', pen=pg.mkPen('w', width=1))
        self.ax1.setLabel('bottom', 'Wavelength', 'm')
        self.ax1.setLabel('left', 'IL', 'dB')
        
        self.ax2.addLegend(offset=(10, -10))
        self.ax2.setTitle('SWS Process')
        self.ax2.setRange(xRange=[1490/1e9,1630/1e9])
        self.ax2p1 = self.ax2.plot(self.wavelength/1e9, self.ILMax, name='ILMax', pen=pg.mkPen('c', width=3))
        self.ax2p2 = self.ax2.plot(self.wavelength/1e9, self.ILMin, name='ILMin', pen=pg.mkPen('y', width=3))
        self.ax2p3 = self.ax2.plot(self.wavelength/1e9, self.ILAVE, name='ILAVE', pen=pg.mkPen('m', width=3))
        self.ax2p4 = self.ax2.plot(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo', pen=pg.mkPen('w', width=1))
        self.ax2.setLabel('bottom', 'Wavelength', 'm')
        self.ax2.setLabel('left', 'IL', 'dB')

        self.ax3.addLegend(offset=(10, -10))
        self.ax3.setTitle('SWS PDL')
        self.ax3p1 = self.ax3.plot(self.wavelength/1e9, self.PDL, name='PDL', pen=pg.mkPen('b', width=3))
        self.ax3p2 = self.ax3.plot(self.wavelength/1e9, self.sDUTPDL.value()/10.0*np.ones(self.wavelength.size), name='PDL Theo', pen=pg.mkPen('w', width=1))
        # self.ax3.addLine(x=None, y=self.sDUTpdl.value()/10.0)
        self.ax3.setLabel('bottom', 'Wavelength', 'm')
        self.ax3.setLabel('left', 'PDL', 'dB')
        # plt.ylim([pdl*0.99, pdl*1.001])

        self.ax5.addLegend()
        self.ax5.setTitle('IL Average Calculations')
        self.ax5.setRange(xRange=[1490/1e9,1630/1e9])
        self.ax5p1 = self.ax5.plot(self.wavelength/1e9, self.ILAVE, name='ILAVE S1S2S3', pen=pg.mkPen('g', width=3))
        self.ax5p2 = self.ax5.plot(self.wavelength/1e9, self.ILAVE_simple, name='ILAVE S2S3 Simp.', pen=pg.mkPen('r', width=3))
        self.ax5p3 = self.ax5.plot(self.wavelength/1e9, self.ILAVE_corrected2, name='ILAVE S2S3 Corr.', pen=pg.mkPen('y', width=3))
        self.ax5p4 = self.ax5.plot(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo', pen=pg.mkPen('w', width=1))
        # self.ax5.addLine(x=None, y=self.ILAVE_Theo)
        self.ax5.setLabel('bottom', 'Wavelength', 'm')
        self.ax5.setLabel('left', 'IL', 'dB')

        self.ax6.addLegend()
        self.ax6.setTitle('IL Average Calculations Error')
        self.ax6.setRange(xRange=[1490/1e9,1630/1e9])
        self.ax6p1 = self.ax6.plot(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE, name='ILAVE S1S2S3', pen=pg.mkPen('g', width=3))
        self.ax6p2 = self.ax6.plot(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE_simple, name='ILAVE S2S3 Simp.', pen=pg.mkPen('r', width=3))
        self.ax6p3 = self.ax6.plot(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE_corrected2, name='ILAVE S2S3 Corr.', pen=pg.mkPen('y', width=3))
        self.ax6.addLine(x=None, y=0)
        self.ax6.setLabel('bottom', 'Wavelength', 'm')
        self.ax6.setLabel('left', 'IL Error', 'dB')


    def reset(self):
        self.sDUTAngle.setValue(0)
        self.sDUTPDL.setValue(8)
        self.sDUTRetardance.setValue(0)
        self.sINAngle.setValue(0)
        self.sINRetardance.setValue(0)
        self.sINRotAngle.setValue(0)

    def play(self):
        self.playButton.setText('Stop')
        self.playButton.clicked.connect(self.stop)

        self.choice = 1
        self.direction = 1

        self.timer_rand = QTimer()
        self.timer_rand.timeout.connect(self.rand)
        self.timer_rand.start(1500)

        self.timer_play = QTimer()
        self.timer_play.timeout.connect(self.playSim)
        self.timer_play.start(100)


    def rand(self):
        self.choice = random.randint(0,5)
        self.direction = random.randint(-1,1)
        if self.direction == 0: self.direction = 1

    def stop(self):
        self.timer_play.stop()
        self.timer_rand.stop()
        self.playButton.setText('Play')
        self.playButton.clicked.connect(self.play)

    def playSim(self):

        if self.choice==0:
            self.sDUTAngle.setValue(self.sDUTAngle.value() + self.direction*1)
        elif self.choice==1:
            self.sDUTPDL.setValue(self.sDUTPDL.value() + self.direction*1)
        elif self.choice==2:
            self.sDUTRetardance.setValue(self.sDUTRetardance.value() + self.direction*1)
        elif self.choice==3:
            self.sINAngle.setValue(self.sINAngle.value() + self.direction*1)
        elif self.choice==4:
            self.sINRetardance.setValue(self.sINRetardance.value() + self.direction*1)
        elif self.choice==5:
            self.sINRotAngle.setValue(self.sINRotAngle.value() + self.direction*1)

    def update(self):
        self.sim()
        self.ax1p1.setData(self.wavelength/1e9, 10*np.log10(self.TL), name='S1 - L')
        self.ax1p2.setData(self.wavelength/1e9, 10*np.log10(self.TV*np.ones(self.wavelength.size)), name='S2 - V')
        self.ax1p3.setData(self.wavelength/1e9, 10*np.log10(self.TH), name='S3 - H')
        self.ax1p4.setData(self.wavelength/1e9, 10*np.log10(self.TD), name='S4 - D')
        self.ax1p5.setData(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo')

        self.ax2p1.setData(self.wavelength/1e9, self.ILMax, name='ILMax')
        self.ax2p2.setData(self.wavelength/1e9, self.ILMin, name='ILMin')
        self.ax2p3.setData(self.wavelength/1e9, self.ILAVE, name='ILAVE')
        self.ax2p4.setData(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo')

        self.ax3p1.setData(self.wavelength/1e9, self.PDL, name='PDL')
        self.ax3p2.setData(self.wavelength/1e9, self.sDUTPDL.value()/10.0*np.ones(self.wavelength.size), name='PDL Theo')

        self.ax5p1.setData(self.wavelength/1e9, self.ILAVE, name='ILAVE S1S2S3 ')
        self.ax5p2.setData(self.wavelength/1e9, self.ILAVE_simple, name='ILAVE S2S3 Simp.')
        self.ax5p3.setData(self.wavelength/1e9, self.ILAVE_corrected2, name='ILAVE S2S3 Corr.')
        self.ax5p4.setData(self.wavelength/1e9, self.ILAVE_Theo*np.ones(self.wavelength.size), name='ILAVE Theo')

        self.ax6p1.setData(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE, name='ILAVE S1S2S3 ')
        self.ax6p2.setData(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE_simple, name='ILAVE S2S3 Simp.')
        self.ax6p3.setData(self.wavelength/1e9, self.ILAVE_Theo-self.ILAVE_corrected2, name='ILAVE S2S3 Corr.')

        a = (self.M*self.V).get()*self.radius_scale
        self.pos[0] = (float(a[1]),float(a[2]),float(a[3]))

        a = self.H1.get()*self.radius_scale
        self.pos[1] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.H2.get()*self.radius_scale
        self.pos[2] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.H3.get()*self.radius_scale
        self.pos[3] = (float(a[1]),float(a[2]),float(a[3]))

        a = self.L1.get()*self.radius_scale
        self.pos[4] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.L2.get()*self.radius_scale
        self.pos[5] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.L3.get()*self.radius_scale
        self.pos[6] = (float(a[1]),float(a[2]),float(a[3]))

        a = self.D1.get()*self.radius_scale
        self.pos[7] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.D2.get()*self.radius_scale
        self.pos[8] = (float(a[1]),float(a[2]),float(a[3]))
        a = self.D3.get()*self.radius_scale
        self.pos[9] = (float(a[1]),float(a[2]),float(a[3]))

        self.Stokes.setData(pos=self.pos)


    def sim(self):

        vDUTAngle = self.sDUTAngle.value()/50.0*np.pi
        vDUTPDL = self.sDUTPDL.value()/10.0
        vDUTRetardance = self.sDUTRetardance.value()/50.0*np.pi
        
        vINAngle = self.sINAngle.value()/50.0*np.pi
        vINRetardance = self.sINRetardance.value()/50.0*np.pi
        vINRotAngle = self.sINRotAngle.value()/50.0*np.pi

        self.sDUTAngle_value.setText(f'{self.sDUTAngle.value()/50.0:0.2f}' + u' \u03C0')
        self.sDUTPDL_value.setText(f'{self.sDUTPDL.value()/10.0:0.1f}' + u' dB')
        self.sDUTRetardance_value.setText(f'{self.sDUTRetardance.value()/50.0:0.2f}' + u' \u03C0')
        self.sINAngle_value.setText(f'{self.sINAngle.value()/50.0:0.2f}' + u' \u03C0')
        self.sINRetardance_value.setText(f'{self.sINRetardance.value()/50.0:0.2f}' + u' \u03C0')
        self.sINRotAngle_value.setText(f'{self.sINRotAngle.value()/50.0:0.2f}' + u' \u03C0')

        self.V=Stokes('V')
        self.V.from_elements(1, -1, 0, 0)

        MIN_Retarder = Mueller('Arbitrary Input')
        MIN_Retarder.retarder_linear(vINRetardance, vINAngle)

        MDUT_R = Mueller('Retarder')
        MDUT_R.retarder_linear(vDUTRetardance, vDUTAngle)

        MDUT_PDL = Mueller('Diattenuator')
        MDUT_PDL.diattenuator_linear(1, np.sqrt(10**(-vDUTPDL/10)), angle=vDUTAngle)


        self.M = MDUT_PDL*MDUT_R*MIN_Retarder
        ###################################################################
        self.H1 = self.M*(self.HWP1*self.V).rotate(vINRotAngle)
        self.H2 = self.M*(self.HWP2*self.V).rotate(vINRotAngle)
        self.H3 = self.M*(self.HWP3*self.V).rotate(vINRotAngle)

        self.D1 = self.M*(self.HWP451*self.V).rotate(vINRotAngle)
        self.D2 = self.M*(self.HWP452*self.V).rotate(vINRotAngle)
        self.D3 = self.M*(self.HWP453*self.V).rotate(vINRotAngle)

        self.L1 = self.M*(self.QWP1*self.V).rotate(vINRotAngle)
        self.L2 = self.M*(self.QWP2*self.V).rotate(vINRotAngle)
        self.L3 = self.M*(self.QWP3*self.V).rotate(vINRotAngle)

        TH = []
        TL = []
        TD = []

        H_points = []
        L_points = []
        D_points = []

        for a in self.alfa:
            HWP = Mueller("HWP")
            HWP.retarder_linear(a, np.pi/4)

            HWP45 = Mueller("HWP")
            HWP45.retarder_linear(a, np.pi/8)

            QWP = Mueller("QWP")
            QWP.retarder_linear(a/2, np.pi/4)

            H_a = (HWP*self.V).rotate(vINRotAngle)
            H_a = self.M*H_a

            L_a = (QWP*self.V).rotate(vINRotAngle)
            L_a = self.M*L_a

            D_a = (HWP45*self.V).rotate(vINRotAngle)
            D_a = self.M*D_a

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

        self.V.rotate(vINRotAngle)

        self.TV = (self.M*self.V).parameters.intensity()
        self.TH = np.array(TH)
        self.TL = np.array(TL)
        self.TD = np.array(TD)

        beta = np.cos(self.wavelength_center*np.pi/(2.0*self.wavelength))	# wavelength first correction factor
        miu = np.sin(self.wavelength_center*np.pi/self.wavelength)		# wavelength second correction factor
        m00 = ((1 + beta*miu)*self.TV - miu*self.TL + self.TH)/(2.0 - (1 - beta)*miu)
        m01 = ((1 - miu)*self.TV + miu*self.TL - self.TH)/(2.0 - (1 - beta)*miu)
        m03 =	(2*self.TL - (1 + beta)*self.TV - (1 - beta)*self.TH)/(2.0 - miu*(1 - beta))
        m02 = self.TD - m00 - (miu/np.sqrt(2.0))*m03
        delta = np.sqrt(m01*m01 + m02*m02 + m03*m03)

        self.ILMin = 10*np.log10(m00 - delta)
        self.ILMax = 10*np.log10(m00 + delta)
        self.ILAVE = 10*np.log10(m00)
        self.PDL = 10*np.log10((m00 + delta)/(m00 - delta))

        self.ILAVE_Theo = 10*np.log10(self.M.parameters.mean_transmission())
        self.ILAVE_simple = 10*np.log10((self.TV + self.TH)/2)

        c = np.cos(self.wavelength_center*np.pi/(self.wavelength))
        s = np.sin(self.wavelength_center*np.pi/(self.wavelength))
        self.ILAVE_corrected2 = 10*np.log10((self.TH - self.TV*(c+s))/(1-c-s))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':      
    main() 
