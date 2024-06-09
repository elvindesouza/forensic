from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QProgressBar, QComboBox, QFileDialog
from imaging_tool.controller import Controller
import subprocess


class ForensicImagingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Forensic Imaging Tool')

        layout = QVBoxLayout()

        self.sourceDiskLabel = QLabel('Source Disk:')
        self.sourceDiskComboBox = QComboBox()  # Create a combo box for disk selection
        self.populateDiskComboBox()  # Populate the combo box with available disks
        layout.addWidget(self.sourceDiskComboBox)
        layout.addWidget(self.sourceDiskLabel)

        self.destinationPathLabel = QLabel('Destination Path:')
        layout.addWidget(self.destinationPathLabel)

        self.destinationPath = QLineEdit()
        layout.addWidget(self.destinationPath)

        self.selectFolderButton = QPushButton('Select Folder')
        self.selectFolderButton.clicked.connect(self.openFileDialog)
        layout.addWidget(self.selectFolderButton)

        self.startButton = QPushButton('Start Imaging')
        self.startButton.clicked.connect(self.controller.startImaging)
        layout.addWidget(self.startButton)

        self.progressBar = QProgressBar(self)
        layout.addWidget(self.progressBar)

        self.statusLabel = QLabel('Status: Waiting to start')
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def populateDiskComboBox(self):
        disks = []
        lsblk_output = subprocess.run(['lsblk', '-d', '-o', 'PATH'], capture_output=True, text=True)
        if lsblk_output.returncode == 0:
            output_lines = lsblk_output.stdout.split('\n')
            output_lines[0] = "Select Disk"
            for line in output_lines:  # Exclude the first line
                disk_name = line.strip()
                if disk_name and 'loop' not in disk_name:  # Exclude loop devices
                    disks.append(disk_name)
        else:
            print("Error:", lsblk_output.stderr)

        self.sourceDiskComboBox.clear()
        self.sourceDiskComboBox.addItems(disks)

    def openFileDialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.destinationPath.setText(folder_path + "/disk.img")
