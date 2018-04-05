import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

# For convenience, we import all the classes in PyQt4's QtCore and QtGui modules rather than listing only those we need. The only disadvantage to this is that the program's namespace will contain all the classes from those modules.

# Creating a Window

# The application's window will be an instance of the Window custom widget class, derived from QWidget, which we will use as a container for other widgets.

class Window(QtWidgets):
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)

        self.text = self.tr("Text Effects")
        self.number = 6
        self.font = QFont()


        self.view = QGraphicsView()

        textLabel = QLabel(self.tr("&Text:"))
        numberLabel = QLabel(self.tr("&Number:"))
        fontLabel = QLabel(self.tr("&Font:"))
        lineEdit = QLineEdit(self.text)
        spinBox = QSpinBox()
        spinBox.setMinimum(1)
        spinBox.setValue(self.number)
        fontCombo = QFontComboBox()
# The first task we need to perform in the class's initialisation method is to call the equivalent method in the base class. We then define some attributes that will be used to customize the text displayed by the application. We use the tr() method to follow good practice, in case we want to translate the application into different languages in the future.
# The window will contain a number of standard widgets, arranged in a grid layout. On the left will be a QGraphicsView widget - a canvas-like widget. To the right of this will be a line edit, a spin box and a combobox, each with associated labels. The user will enter the text to be displayed on the canvas using the line edit, use the spin box to indicate how many times it should be displayed, and set the display font using the font combobox:

# We set the minimum value of 1 for the spin box, since we want the user's text to be displayed at least once.
# Each of the labels is associated with an input widget using the following assignments:

        textLabel.setBuddy(lineEdit)
        numberLabel.setBuddy(spinBox)
        fontLabel.setBuddy(fontCombo)

# These enable the user to use the mnemonics specified using & characters in the labels to nagivate directly to the input widgets themselves.
# Since we want the view to be updated whenever the user changes the parameters influencing the text displayed there, we connect signals in each of these widgets to appropriate slots (defined later) in the Window class:

        self.connect(lineEdit, SIGNAL("textChanged(const QString &)"),
                     self.setText)
        self.connect(spinBox, SIGNAL("valueChanged(int)"), self.setNumber)
        self.connect(fontCombo, SIGNAL("currentFontChanged(const QFont &)"),
                     self.setFont)

# Each signal is specified using a C++ signature that indicate the type of data that is communicated. Since the slots are just Python methods, we can specify them without providing any type information.
# We set up the layout of these widgets as described earlier, using a QGridLayout instance to arrange the input widgets and labels, and place this alongside the QGraphicsView widget:

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(textLabel, 0, 0)
        controlsLayout.addWidget(lineEdit, 0, 1)
        controlsLayout.addWidget(numberLabel, 1, 0)
        controlsLayout.addWidget(spinBox, 1, 1)
        controlsLayout.addWidget(fontLabel, 2, 0)
        controlsLayout.addWidget(fontCombo, 2, 1)
        controlsLayout.setRowStretch(3, 1)

        layout = QHBoxLayout()
        layout.addWidget(self.view, 1)
        layout.addLayout(controlsLayout)
        self.setLayout(layout)

# Once the layout is set up, we create a scene for the view using the initial default parameters defined earlier, and set the window title:

        self.createScene()
        self.setWindowTitle(self.tr("Text Effects"))

# Initially, the QGraphicsView instance has no scene to display. The createScene() method is used to remove any old scene, create a new QGraphicsScene instance, populate it with text items, and add it to the view:

    def createScene(self):

        scene = QGraphicsScene()
        self.view.setScene(scene)

# We first create a new scene and replace the old scene in the view.

# The text items will be arranged in a evenly-spaced circular formation, so we calculate the angle between each item using the number specified by the user in the spin box, and we obtain information about the font to be used so that we can position the items more accurately:

        angle = 360.0 / self.number
        fontMetrics = QFontMetricsF(self.font)
        height = fontMetrics.height()

        for i in range(self.number):

            item = scene.addText(self.text, self.font)
            item.rotate(i * angle)
            item.translate(20.0, -height/2.0)

# Each of the text items is created with the desired text and font using a QGraphicsScene convenience method. We rotate each item by the appropriate angle before translating it along its local x-axis, and translate it upwards along its local y-axis by half the font's height to improve the overall visual effect.

        self.scene = scene
        self.view.update()

# The new scene is stored in an attribute, replacing any old scene previously created, and the view is updated with a call to its update() method.
# When any of the values in the input widgets change, the signal emitted by the widget will be delivered to one of the following slots, which will be called with the value specified in the signal:

    def setNumber(self, number):

        self.number = number
        self.createScene()

    def setText(self, text):

        self.text = QString(text)
        self.createScene()

    def setFont(self, font):

        self.font = QFont(font)
        self.createScene()

# Each of these slots simply updates the appropriate attribute in the instance and call createScene() to update the text displayed in the view.
# The main program is as simple as possible. We create an application instance, create a widget by instantiating the Window class, and show it:

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
