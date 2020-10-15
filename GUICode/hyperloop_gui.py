from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class EmergencyButton(QWidget):
#     def __init__(self, parent=None):
#         super(EmergencyButton, self).__init__(parent)
#         self.msgBox = QMessageBox()
#         self.btn = QWidget()
#         self.btn.setWindowTitle("Click button")
#         self.push = QPushButton(self.btn)
#         self.push.setText("Emergency!")
#         self.push.move(50,50)
#         self.push.clicked.connect(self.pushedEmergency)
        
#     def msgButtonClick(self, i):
#         print("Button clicked is:", i.text())

#     def pushedEmergency(self):
#         self.msgBox.setIcon(QMessageBox.Information)
#         self.msgBox.setText("Do you want to terminate program?")
#         self.msgBox.setWindowTitle("Emergency Button Pushed!")
#         self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#         self.msgBox.buttonClicked.connect(self.msgButtonClick)

#         returnValue = self.msgBox.exec()
#         if returnValue == QMessageBox.Ok:
#             print('OK clicked')
#             sys.exit()
#         else:
#             print("Action cancelled")

        
class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

def msgButtonClick(i):
    print("Button clicked is:",i.text())

def pushedEmergency():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("Do you want to terminate program?")
    msgBox.setWindowTitle("Emergency Button Pushed!")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.buttonClicked.connect(msgButtonClick)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        print('OK clicked')
        sys.exit()
    else:
        print("Action cancelled")

class Tab(QTabWidget):
    def __init__(self, parent = None):
        super(Tab, self).__init__(parent)
        self.imu_tab = QWidget()
        self.lds_tab = QWidget()
        self.ps_tab = QWidget()
        self.pes_tab = QWidget()
        self.re_tab = QWidget()
            
        self.addTab(self.imu_tab,"IMU")
        self.addTab(self.lds_tab,"LDS")
        self.addTab(self.ps_tab,"PS")
        self.addTab(self.pes_tab,"PES")
        self.addTab(self.re_tab,"RE")
        self.ImuTab()
        self.LdsTab()
        self.PsTab()
        self.PesTab()
        self.ReTab()

        self.setWindowTitle("Sensors Data")
		
    def ImuTab(self):
        mainLayout = QGridLayout()
        imuLayout = QGridLayout()
        imuLayout.addWidget(QLabel('IMU'), 0, 0)
        imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.imu_tab.setLayout(mainLayout)
		
    def LdsTab(self):
        mainLayout = QGridLayout()

        imuLayout = QGridLayout()
        imuLayout.addWidget(QLabel('LDS'), 0, 0)
        imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.lds_tab.setLayout(mainLayout)
            
    def PsTab(self):
        mainLayout = QGridLayout()

        imuLayout = QGridLayout()
        imuLayout.addWidget(QLabel('PS'), 0, 0)
        imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.ps_tab.setLayout(mainLayout)
    
    def PesTab(self):
        mainLayout = QGridLayout()

        imuLayout = QGridLayout()
        imuLayout.addWidget(QLabel('PES'), 0, 0)
        imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.pes_tab.setLayout(mainLayout)
    
    def ReTab(self):
        mainLayout = QGridLayout()

        imuLayout = QGridLayout()
        imuLayout.addWidget(QLabel('RE'), 0, 0)
        imuLayout.addWidget(QTableWidget(2, 2), 1, 0)
        mainLayout.addLayout(imuLayout, 1, 0)
        self.re_tab.setLayout(mainLayout)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Hyperloop GUI")

        hbox = QHBoxLayout(self)
		
        top_left = QFrame()
        top_left.setFrameShape(QFrame.StyledPanel)
        middle_left = QFrame()
        middle_left.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)

        # emergency_button = EmergencyButton()
        emergency_button = QWidget()
        btn = QPushButton(emergency_button)
        btn.setText("Emergency!")
        btn.move(50,50)
        btn.clicked.connect(pushedEmergency)
        emergency_button.setWindowTitle("Click button")
        splitter1.addWidget(top_left)
        splitter1.addWidget(emergency_button)
        splitter1.setSizes([300, 50])

        splitter_cameras = QSplitter(Qt.Vertical)
        splitter_cameras.addWidget(Color('black'))
        splitter_cameras.addWidget(Color('black'))

        splitter2 = QSplitter(Qt.Horizontal)
        sensors_tab = Tab()
        splitter2.addWidget(splitter_cameras)
        splitter2.addWidget(sensors_tab)
        splitter2.setSizes([150,200])
            
        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.addWidget(bottom)
        splitter3.setSizes([50,200,50])
            
        hbox.addWidget(splitter3)
            
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
            
        self.setGeometry(300, 300, 300, 200)
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

