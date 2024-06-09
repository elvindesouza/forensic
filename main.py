from imaging_tool.gui import ForensicImagingTool
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ForensicImagingTool()
    ex.show()
    sys.exit(app.exec_())
