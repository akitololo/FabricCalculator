import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()

	def initUI(self):
		self.setStyleSheet('font-size: 12pt; font-family: Comic Sans MS;')
		self.setGeometry(100, 100, 250, 550)
		self.setWindowTitle("Opening Fabric Size & Price Calculator")
		self.setWindowIcon(QtGui.QIcon('curtain-938541_1280.jpg'))
		self.initUserSpace()

	def initUserSpace(self):
		vbox = QtGui.QVBoxLayout()
		headerLabel = QtGui.QLabel("Please input the measurements of the below opening in cm")
		lengthLabel = QtGui.QLabel("Length:")
		widthLabel = QtGui.QLabel("Width:")
		self.lengthInput = QtGui.QLineEdit(self)
		self.widthInput = QtGui.QLineEdit(self)
		userInputSpace = QtGui.QFormLayout()
		userInputSpace.addRow(lengthLabel, self.lengthInput)
		userInputSpace.addRow(widthLabel, self.widthInput)
		vbox.addWidget(headerLabel)
		vbox.addLayout(userInputSpace)
		btn = QtGui.QPushButton("Calculate", self)
		vbox.addWidget(btn)
		btn.clicked.connect(self.retrieveText)
		self.setLayout(vbox)
		self.show()

	def retrieveText(self):
		self.l = self.lengthInput.text()
		self.w = self.widthInput.text()


def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()