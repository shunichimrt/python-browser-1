import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QLineEdit, QGridLayout, QApplication, QPushButton,  QDesktopWidget)

class PythonBrowser(QWidget):

    def __init__(self):
        super().__init__()
        self.name = 'PythonBrowser'
        self.initUI()

    def initUI(self):

        initurl = 'https://www.yahoo.co.jp/'

        self.browser = QWebEngineView()
        self.browser.load(QUrl(initurl))        
        self.browser.resize(1000,600)
        self.browser.move(200,200)
        self.browser.setWindowTitle(self.name)
        
        self.back_button = QPushButton('戻る')
        self.back_button.clicked.connect(self.browser.back)        
        self.forward_button = QPushButton('進む')
        self.forward_button.clicked.connect(self.browser.forward)
        self.reload_button = QPushButton('更新')
        self.reload_button.clicked.connect(self.browser.reload)
        self.url_edit = QLineEdit()
        self.move_button = QPushButton('検索')
        self.move_button.clicked.connect(self.loadPage)
        self.browser.urlChanged.connect(self.updateCurrentUrl)

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.move_button, 1, 13)
        grid.addWidget(self.browser,2, 0, 5, 15)
        self.setLayout(grid) 
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle(self.name)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadPage(self):
        move_url = QUrl(self.url_edit.text())
        self.browser.load(move_url)
        self.updateCurrentUrl

    def updateCurrentUrl(self):
        self.url_edit.clear()
        self.url_edit.insert(self.browser.url().toString())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = PythonBrowser()
    sys.exit(app.exec_())
