import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
import pyqtgraph as pg
import numpy as np


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Why must programming be so hard"
        self.left = 300
        self.top = 200
        self.width = 1600
        self.height = 900
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.plot_widget = pg.PlotWidget(self)
        self.plot_widget.setGeometry(200, 200, 1000, 600)
        self.plot_widget.showGrid(x=True, y=True)    # show grid on graph
        self.plot_widget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))

        self.lblMouseCoords = QLabel("Hi Mickey! can you read this?  Is it wide enough?? must be wider", self)
        font = self.lblMouseCoords.font()
        font.setPointSize(12)
        self.lblMouseCoords.setFont(font)
        self.lblMouseCoords.move(600, 150)

        btnPlot = QPushButton("Plot Data", self)
        btnPlot.move(50, 500)
        btnPlot.clicked.connect(self.btnPlot_click)

        self.plot_widget.plot(y=np.random.normal(size=100), pen='r')
        self.plot_widget.setTitle("Basic array plotting")
        #self.showMaximized()    # This shows the window full screen

        self.plot_widget.scene().sigMouseMoved.connect(self.mouse_moved)
        self.plot_widget.scene().sigMouseClicked.connect(self.mouse_clicked)

        self.show()

    @pyqtSlot()
    def btnPlot_click(self):
        self.lblMouseCoords.setText("Hey Mickey, where's Goofy?")

    def mouse_moved(self, evt):
        vb = self.plot_widget.plotItem.vb
        if self.plot_widget.sceneBoundingRect().contains(evt):
            mouse_point = vb.mapSceneToView(evt)
            self.lblMouseCoords.setText("X: {:.3f}   Y: {:.3f}".format(mouse_point.x(), mouse_point.y()))

    def mouse_clicked(self, evt):
        vb = self.plot_widget.plotItem.vb
        scene_coords = evt.scenePos()
        if self.plot_widget.sceneBoundingRect().contains(scene_coords):
            mouse_point = vb.mapSceneToView(scene_coords)
            print(f'clicked plot X: {mouse_point.x()}, Y: {mouse_point.y()}, event: {evt}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
