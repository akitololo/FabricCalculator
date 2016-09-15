import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
#	[!] Note that all prices (except blinds and labour) is in metres
		self.FABRIC_PRICE = 1000
		self.LINING_PRICE = 300
		self.BLACKOUT_PRICE = 1300
		self.TAPE_PRICE = 275
		self.SHEERS_PRICE = 900
		self.BLINDS_PRICE = 4500 # Just a reminder: This is per m^2
		self.LABOUR_PRICE = 700 # This one is per Wd (width [according to Dad])
		self.initUI()

	def initUI(self):
		self.setStyleSheet('font-size: 12pt; font-family: Comic Sans MS;')
		self.setGeometry(100, 100, 250, 350)
		self.setWindowTitle("Opening Fabric Size & Price Calculator")
		self.setWindowIcon(QtGui.QIcon('curtain-938541_1280.jpg'))
		self.initUserSpace()

	def initUserSpace(self):
		vbox = QtGui.QVBoxLayout()
		headerLabel = QtGui.QLabel("Please input the measurements of the below opening in cm")
		lengthLabel = QtGui.QLabel("Length:")
		widthLabel = QtGui.QLabel("Width:")
		panelLabel = QtGui.QLabel("No. of panels:")
		self.lengthInput = QtGui.QLineEdit(self)
		self.widthInput = QtGui.QLineEdit(self)
		self.panelInput = QtGui.QLineEdit(self)
		userInputSpace = QtGui.QFormLayout()
		userInputSpace.addRow(lengthLabel, self.lengthInput)
		userInputSpace.addRow(widthLabel, self.widthInput)
		userInputSpace.addRow(panelLabel, self.panelInput)
		vbox.addWidget(headerLabel)
		vbox.addLayout(userInputSpace)
		btn = QtGui.QPushButton("Calculate", self)
		vbox.addWidget(btn)
		btn.clicked.connect(self.retrieveCalculateShow)
		self.popup = None
		self.setLayout(vbox)
		self.show()

	def retrieveCalculateShow(self):
		self.l = float(self.lengthInput.text())
		self.w = float(self.widthInput.text())
		self.p = float(self.panelInput.text())
		Wd = (((self.w)*2) + (10*(self.p))) / 140 # No unit for this particular mini calc
		L = (((self.l) + 28) * Wd) / 100 # This calc ends up in metres (m)
		fabric = lining = blackout = sheers = L
		tape = ((self.w)*2) / 100 # Comes out in m
		labour = Wd
		blinds = (self.w*self.l)/(100**2) # Comes out in m^2

		fabricPrice = fabric * self.FABRIC_PRICE
		liningPrice = lining * self.LINING_PRICE
		blackoutPrice = blackout * self.BLACKOUT_PRICE
		sheersPrice = sheers * self.SHEERS_PRICE
		tapePrice = tape * self.TAPE_PRICE
		labourPrice = labour * self.LABOUR_PRICE
		blindsPrice = blinds * self.BLINDS_PRICE
		totalPrice = fabricPrice + liningPrice + blackoutPrice + sheersPrice + tapePrice + labourPrice + blindsPrice

		fabricCalculatedPriceLabel = QtGui.QLabel(str(int(fabricPrice)))
		liningCalculatedPriceLabel = QtGui.QLabel(str(int(liningPrice)))
		blackoutCalculatedPriceLabel = QtGui.QLabel(str(int(blackoutPrice)))
		sheersCalculatedPriceLabel = QtGui.QLabel(str(int(sheersPrice)))
		tapeCalculatedPriceLabel = QtGui.QLabel(str(int(tapePrice)))
		labourCalculatedPriceLabel = QtGui.QLabel(str(int(labourPrice)))
		blindsCalculatedPriceLabel = QtGui.QLabel(str(int(blindsPrice)))
		totalCalculatedPriceLabel = QtGui.QLabel(str(int(totalPrice)))

##############################################################################################
#							Pop-up handling begins here 									 #
##############################################################################################

		popup = QtGui.QDialog()
		popup.setStyleSheet('font-size: 12pt; font-family: Comic Sans MS;')
		popup.setGeometry(150,150, 200, 230)
		popup.setWindowIcon(QtGui.QIcon('curtain-938541_1280.jpg'))
		popup.setWindowTitle("Your Answers")

		answerSpace = QtGui.QFormLayout()
		fabricSizeLabel = QtGui.QLabel("Fabric (m):")
		liningSizeLabel = QtGui.QLabel("Lining (m):")
		blackoutSizeLabel = QtGui.QLabel("Blackout (m):")
		tapeSizeLabel = QtGui.QLabel("Tape (m):")
		sheersSizeLabel = QtGui.QLabel("Sheers (m):")
		blindsSizeLabel = QtGui.QLabel("Blinds (m^2):")
		labourSizeLabel = QtGui.QLabel("Labour (Wd):")
		fabricPriceLabel = QtGui.QLabel("Fabric price total (Ksh):")
		liningPriceLabel = QtGui.QLabel("Lining price total (Ksh):")
		blackoutPriceLabel = QtGui.QLabel("Blackout price total (Ksh):")
		tapePriceLabel = QtGui.QLabel("Tape price total (Ksh):")
		sheersPriceLabel = QtGui.QLabel("Sheers price total (Ksh):")
		blindsPriceLabel = QtGui.QLabel("Blinds price total (Ksh):")
		labourPriceLabel = QtGui.QLabel("Labour price total (Ksh):")
		totalPriceLabel = QtGui.QLabel("Total (Ksh):")
		line = QtGui.QLabel("   ______________________")
		answerSpace.addRow(fabricSizeLabel, QtGui.QLabel(str(round(fabric, 3))))
		answerSpace.addRow(liningSizeLabel, QtGui.QLabel(str(round(lining, 3))))
		answerSpace.addRow(blackoutSizeLabel, QtGui.QLabel(str(round(blackout, 3))))
		answerSpace.addRow(tapeSizeLabel, QtGui.QLabel(str(round(tape, 3))))
		answerSpace.addRow(sheersSizeLabel, QtGui.QLabel(str(round(sheers, 3))))
		answerSpace.addRow(blindsSizeLabel, QtGui.QLabel(str(round(blinds, 3))))
		answerSpace.addRow(labourSizeLabel, QtGui.QLabel(str(round(labour, 3))))
		answerSpace.addRow(line)
		answerSpace.addRow(fabricPriceLabel, fabricCalculatedPriceLabel)
		answerSpace.addRow(liningPriceLabel, liningCalculatedPriceLabel)
		answerSpace.addRow(blackoutPriceLabel, blackoutCalculatedPriceLabel)
		answerSpace.addRow(tapePriceLabel, tapeCalculatedPriceLabel)
		answerSpace.addRow(sheersPriceLabel, sheersCalculatedPriceLabel)
		answerSpace.addRow(blindsPriceLabel, blindsCalculatedPriceLabel)
		answerSpace.addRow(labourPriceLabel, labourCalculatedPriceLabel)
		answerSpace.addRow(totalPriceLabel, totalCalculatedPriceLabel)

		popup.setLayout(answerSpace)

		popup.exec_()


def main():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()