from imaging_tool.gui import ImagingTool
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ImagingTool()
    ex.show()
    sys.exit(app.exec_())
