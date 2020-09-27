import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
from main import start
from utils import Config
from tracker import end_gui
from shutil import copyfile

class Worker(QThread):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''
    message_signal = pyqtSignal(str)
    def __init__(self, fn, fileName, config):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.fileName = fileName
        self.config = config

    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(self.fileName, self.config, self.message_signal.emit)
        print ("done here")

class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title = 'SlideCast'
        self.config = Config()
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.threadpool = QThreadPool()
        self.initUI()

        self.recording = False
        self.pdfChosen = False 
    
    def initUI(self):
        name = QLabel('Name')
        pdf = QLabel('PDF Location')
        log = QLabel('Log')
        self.pdfEdit = QLineEdit()
        self.logEdit = QTextEdit()
        
        pdfButton = QPushButton('Choose PDF', self)
        pdfButton.setToolTip('Choose PDF for the Recording')

        pdfButton.clicked.connect(self.choose_pdf)

        self.recordButton = QPushButton('Begin Recording', self)
        self.recordButton.setToolTip('Begin Recording')
        self.recordButton.clicked.connect(self.record)

        self.pdfEdit.setReadOnly(True)
        self.logEdit.setReadOnly(True)      

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(pdf, 1, 0)
        grid.addWidget(self.pdfEdit, 1, 1)

        grid.addWidget(log, 2, 0)
        grid.addWidget(self.logEdit, 2, 1, 1, 1)

        grid.addWidget(pdfButton, 3, 0)
        grid.addWidget(self.recordButton, 3, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('SlideCast')
        self.show()
    
    @pyqtSlot()
    def record(self):
        if not self.recording:
            
            if not self.pdfChosen:
                QMessageBox.about(self, "PDF Not Chosen", "Choose a PDF first!")
            else:
                self.recording  = True 
                self.recordButton.setText("Stop Recording")
                self.worker = Worker(start, self.fileName, self.config)
                self.worker.start()
                self.worker.message_signal.connect(self.emit_message)
                # self.threadpool.start(self.worker) 

        else:
            self.logEdit.append("finished recording.. Please wait while the file is processed")
            end_gui(self.config)
            time.sleep(0.1)

            self.worker.wait()
            self.config = Config()
            self.recording = False 
            self.recordButton.setText("Begin Recording")
            self.outputFile = self.saveFileDialog("Save Recording")
            if self.outputFile.split(".")[-1] != "sld":
                self.outputFile += ".sld"

            copyfile("output/recording.sld", self.outputFile)
            self.logEdit.clear()

    @pyqtSlot(str)
    def emit_message(self, message):
        self.logEdit.append(message)

    @pyqtSlot()
    def choose_pdf(self):
        self.fileName = self.openFileNameDialog("Choose PDF for recording")
        self.pdfEdit.setText(self.fileName)
        self.pdfChosen = True
    
    def openFileNameDialog(self, heading):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, heading, "","PDF Files (*.pdf)", options=options)
        return fileName
    
    
    def saveFileDialog(self, heading):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, heading,"","SlideCast Files(*.sld)", options=options)
        return fileName

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())