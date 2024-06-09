import subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from imaging_tool.imaging import image_disk
from imaging_tool.utils import calculate_checksums
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Create an ImagingThread class that extends QThread
# This class will handle the imaging process in a separate thread
class ImagingThread(QThread):
    progress = pyqtSignal(int)
    status = pyqtSignal(str)

    def __init__(self, source_disk, dest_path):
        super().__init__()
        self.source_disk = source_disk
        self.dest_path = dest_path

    def run(self):
        try:
            self.log('INFO: Imaging in progress...')
            self.progress.emit(0)
            image_disk(self.source_disk, self.dest_path, self.progress)
            self.log('INFO: Generating checksums...')
            self.progress.emit(100)
        except Exception as e:
            self.log(f"ERROR: Error during imaging - {str(e)}")

    def log(self, msg: str):
        logger.debug(msg)
        self.status.emit(msg)

    def compress_image(self, image_path):
        compress_command = ['gzip', image_path]
        process = subprocess.run(compress_command, capture_output=True, text=True)
        logger.debug(process.stdout)
        if process.returncode == 0:
            self.log("INFO: Compression completed successfully")
        else:
            self.log("ERROR: Compression failed")

class Controller:
    def __init__(self, gui):
        self.gui = gui

    def startImaging(self):
        source_disk = self.gui.sourceDiskComboBox.currentText()
        dest_path = self.gui.destinationPath.text()

        self.imaging_thread = ImagingThread(source_disk, dest_path)
        self.imaging_thread.progress.connect(self.updateProgress)
        self.imaging_thread.status.connect(self.updateStatus)
        self.imaging_thread.start()

    def updateProgress(self, value):
        self.gui.progressBar.setValue(value)

    def updateStatus(self, message):
        self.gui.statusLabel.setText(message)



