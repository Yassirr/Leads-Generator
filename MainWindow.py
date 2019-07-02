#AUTHOR *__ 'Yassir' __*

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtGui

#from alexa_crawl.alexa_crawl.spiders.alexa import AlexaSpider
#from statshow_crawl.statshow_crawl.spiders.statshow import StatshowSpider

import sys

class Tab(QDialog):
	def __init__(self):
		super().__init__()
		
		self.setWindowTitle(" Leads Generator")
		self.setWindowIcon(QIcon("logo.png"))
		
		vbox = QVBoxLayout()
		tabWidget = QTabWidget()
		
		tabWidget.addTab(TabLeadsList(), "Domains")
		tabWidget.addTab(GoogleList(), "Google")
		tabWidget.addTab(TabCredits(), "Credits")
		vbox.addWidget(tabWidget)
		
		self.setLayout(vbox)

class TabLeadsList(QWidget):
	def __init__(self):
		super().__init__()
		
		vbox = QVBoxLayout()
		self.label = QLabel("Select .csv File with Domains to generate leads")
		vbox.addWidget(self.label)
		
		self.btn = QPushButton("Browse File")
		self.btn.clicked.connect(self.browseFile)
		vbox.addWidget(self.btn)
		
		self.runbtn = QPushButton("Run")
		self.runbtn.clicked.connect(self.executeScript)
		vbox.addWidget(self.runbtn)
		
		self.contents = QTextEdit()
		
		self.setLayout(vbox)
		
	def browseFile(self):
		sname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Excel files (*.csv)')
		selectPath = sname[0]
		
	def executeScript(self):
		#StatshowSpider()
		#AlexaSpider()
		print('crawls')

class GoogleList(QWidget):
	def __init__(self):
		super().__init__()
		
		vbox = QVBoxLayout()
		self.label = QLabel("Enter keywords :")
		vbox.addWidget(self.label)
		
		plainTextEdit = QPlainTextEdit()
		vbox.addWidget(plainTextEdit)
		
		self.runbtn = QPushButton("Search")
		self.runbtn.clicked.connect(self.executeScript)
		vbox.addWidget(self.runbtn)
		
		self.contents = QTextEdit()
		
		self.setLayout(vbox)
		
	def browseFile(self):
		sname = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', 'Excel files (*.csv)')
		selectPath = sname[0]
		
	def executeScript(self):
		#StatshowSpider()
		#AlexaSpider()
		print('crawls')

class TabCredits(QWidget):
	def __init__(self):
		super().__init__()
		
		vbox = QVBoxLayout()

		labelImage = QLabel(self)
		pixmap = QPixmap("credit.png")
		labelImage.setPixmap(pixmap)
		labelImage.setGeometry(10, 10, 10, 10)
		vbox.addWidget(labelImage)
		
		self.label2 = QLabel("""Application created to generate leads, results will 
give you the following : 
	
	- Monthly page visits
	- % of consumers from a country
	- Site flow + company info
	- Google Reviews
	- Company contact info 
	
You have two options to get leads :

	- Upload a file with a list of domain
	- Get domains from google (100 site/search)

	Application created by - Yassir - """)
	
		vbox.addWidget(self.label2)
		
		self.setLayout(vbox)


if __name__ == "__main__":
	App = QApplication(sys.argv)
	tabDialog = Tab()
	tabDialog.show()
	App.exec()