from Extractor import Extractor
from Compteur import Compteur
from User import User
from Consommation import Consommation
from datetime import datetime,timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
"""
Cette module contient le code concernant l'interface graphique
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(933, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxClients = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxClients.setGeometry(QtCore.QRect(10, 10, 411, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxClients.setFont(font)
        self.groupBoxClients.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxClients.setFlat(False)
        self.groupBoxClients.setObjectName("groupBoxClients")
        self.usersList = QtWidgets.QTableWidget(self.groupBoxClients)
        self.usersList.setGeometry(QtCore.QRect(10, 70, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usersList.setFont(font)
        self.usersList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.usersList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.usersList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.usersList.setObjectName("usersList")
        self.usersList.setColumnCount(3)
        self.usersList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.usersList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.usersList.setHorizontalHeaderItem(2, item)
        self.usersList.horizontalHeader().setVisible(True)
        self.usersList.horizontalHeader().setStretchLastSection(True)
        self.usersList.verticalHeader().setVisible(False)
        self.usersList.verticalHeader().setStretchLastSection(False)
        self.clientsCB = QtWidgets.QComboBox(self.groupBoxClients)
        self.clientsCB.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.clientsCB.setObjectName("clientsCB")
        self.clientsCB.addItem("")
        self.groupBoxCompteurs = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxCompteurs.setGeometry(QtCore.QRect(430, 10, 491, 151))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxCompteurs.setFont(font)
        self.groupBoxCompteurs.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxCompteurs.setObjectName("groupBoxCompteurs")
        self.compteursList = QtWidgets.QTableWidget(self.groupBoxCompteurs)
        self.compteursList.setGeometry(QtCore.QRect(10, 70, 461, 71))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.compteursList.setFont(font)
        self.compteursList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.compteursList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.compteursList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.compteursList.setObjectName("compteursList")
        self.compteursList.setColumnCount(2)
        self.compteursList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.compteursList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.compteursList.setHorizontalHeaderItem(1, item)
        self.compteursList.horizontalHeader().setStretchLastSection(True)
        self.compteursList.verticalHeader().setVisible(False)
        self.compteursCB = QtWidgets.QComboBox(self.groupBoxCompteurs)
        self.compteursCB.setGeometry(QtCore.QRect(10, 30, 191, 22))
        self.compteursCB.setObjectName("compteursCB")
        self.compteursCB.addItem("")
        self.groupBoxConsommations = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxConsommations.setGeometry(QtCore.QRect(10, 390, 471, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxConsommations.setFont(font)
        self.groupBoxConsommations.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBoxConsommations.setObjectName("groupBoxConsommations")
        self.consommationsTable = QtWidgets.QTableWidget(self.groupBoxConsommations)
        self.consommationsTable.setGeometry(QtCore.QRect(10, 30, 431, 141))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.consommationsTable.setFont(font)
        self.consommationsTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.consommationsTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.consommationsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.consommationsTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.consommationsTable.setObjectName("consommationsTable")
        self.consommationsTable.setColumnCount(2)
        self.consommationsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.consommationsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.consommationsTable.setHorizontalHeaderItem(1, item)
        self.consommationsTable.horizontalHeader().setSortIndicatorShown(True)
        self.consommationsTable.horizontalHeader().setStretchLastSection(True)
        self.consommationsTable.verticalHeader().setVisible(False)
        self.consommationsTable.verticalHeader().setDefaultSectionSize(30)
        self.consommationsTable.verticalHeader().setMinimumSectionSize(30)
        self.consommationsTable.verticalHeader().setStretchLastSection(False)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 170, 911, 211))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(340, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.startDate = QtWidgets.QCalendarWidget(self.groupBox_3)
        self.startDate.setGeometry(QtCore.QRect(50, 20, 281, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startDate.setFont(font)
        self.startDate.setMinimumDate(QtCore.QDate(1995, 9, 15))
        self.startDate.setGridVisible(True)
        self.startDate.setNavigationBarVisible(True)
        self.startDate.setDateEditEnabled(False)
        self.startDate.setObjectName("startDate")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.calculerBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.calculerBtn.setGeometry(QtCore.QRect(670, 20, 201, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.calculerBtn.setFont(font)
        self.calculerBtn.setObjectName("calculerBtn")
        self.endDate = QtWidgets.QCalendarWidget(self.groupBox_3)
        self.endDate.setGeometry(QtCore.QRect(370, 20, 281, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.endDate.setFont(font)
        self.endDate.setMinimumDate(QtCore.QDate(1995, 9, 15))
        self.endDate.setGridVisible(True)
        self.endDate.setNavigationBarVisible(True)
        self.endDate.setDateEditEnabled(False)
        self.endDate.setObjectName("endDate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 390, 421, 171))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.compteurCons = QtWidgets.QLabel(self.groupBox_2)
        self.compteurCons.setGeometry(QtCore.QRect(170, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.compteurCons.setFont(font)
        self.compteurCons.setObjectName("compteurCons")
        self.compteursCons = QtWidgets.QLabel(self.groupBox_2)
        self.compteursCons.setGeometry(QtCore.QRect(170, 40, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.compteursCons.setFont(font)
        self.compteursCons.setObjectName("compteursCons")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 933, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.init()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RedisBD  application"))
        self.groupBoxClients.setTitle(_translate("MainWindow", "Clients:"))
        item = self.usersList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.usersList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.usersList.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Catégorie"))
        self.groupBoxCompteurs.setTitle(_translate("MainWindow", "Compteurs"))
        item = self.compteursList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.compteursList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Adresse"))
        self.groupBoxConsommations.setTitle(_translate("MainWindow", "Consommations"))
        item = self.consommationsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Consommation"))
        item = self.consommationsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Intervalle"))
        self.label_6.setText(_translate("MainWindow", "à :"))
        self.label_5.setText(_translate("MainWindow", "De:"))
        self.calculerBtn.setText(_translate("MainWindow", "Afficher"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Moyenne des consommations en KWH"))
        self.compteurCons.setText(_translate("MainWindow", "0.0"))
        self.compteursCons.setText(_translate("MainWindow", "0.0"))
        self.label_4.setText(_translate("MainWindow", "Moyenne du client:"))
        self.label.setText(_translate("MainWindow", "Moyenne du compteur:"))

    def init(self):
        self.sUser = None
        self.sCompteur = None
        self.ex = Extractor()
        """
            Here we set the data
        """
        self.setData()
        self.clientsCB.activated.connect(lambda item : self.userSelected(item))
        self.compteursCB.activated.connect(lambda item : self.compteurSelected(item))
        dateNow = datetime.now()
        dayPrevFromNow = dateNow-timedelta(hours=24)
        self.startDate.setSelectedDate (dayPrevFromNow)
        self.endDate.setSelectedDate (dateNow)
        self.calculerBtn.clicked.connect(self.calculateTotale)
    def clearCompteursTable(self):
        self.compteursList.clear()
        self.compteursList.setColumnCount(2)
        self.compteursList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setText("ID")
        self.compteursList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Adresse")
        self.compteursList.setHorizontalHeaderItem(1, item)
    def clearUsersTable(self):
        self.usersList.clear()
        self.usersList.setColumnCount(3)
        self.usersList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.usersList.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("ID")
        self.usersList.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Nom")
        self.usersList.setHorizontalHeaderItem(1, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setText("Categorie")
        self.usersList.setHorizontalHeaderItem(2, item)
    def clearTable(self):
        self.consommationsTable.clear()
        self.consommationsTable.setColumnCount(2)
        self.consommationsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.consommationsTable.setVerticalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText("Consommation")
        self.consommationsTable.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setText("Date")
        self.consommationsTable.setHorizontalHeaderItem(1, item)
        self.consommationsTable.setSortingEnabled(True)

    def setData(self):
        self.clearUsersTable()
        self.clearCompteursTable()
        self.clientsCB.clear()
        """
        self.usersList
        self.compteursList
        self.consommationsTable
        """
        for user in self.ex.users:
            self.addClient(user)

    def userSelected(self,item):
        user =  self.clientsCB.itemData(item)
        if user!=None:
        	self.showClientDetails(user)
        	self.sUser = user
        	self.setCompteurs(user.compteurs)
    def compteurSelected(self,item):
        self.clearCompteursTable()
        compteur =  self.compteursCB.itemData(item)
        if compteur!=None:
            self.sCompteur = compteur
            self.showCompteurDetails(compteur)
            self.setConsommations(compteur.consommations)
    def setCompteurs(self,compteurs):
        self.compteursCB.clear()
        self.clearCompteursTable()
        for compteur in compteurs:
            self.addCompteur(compteur)
    def addClient(self,user):
        self.clientsCB.addItem(user.id,user)
    def showClientDetails(self,user):
        self.clearUsersTable()
        rowPosition = 0
        self.usersList.insertRow(rowPosition)

        item = QtWidgets.QTableWidgetItem()
        item.setText(user.id)
        self.usersList.setItem(rowPosition, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText(user.name)
        self.usersList.setItem(rowPosition, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText(user.cat)
        self.usersList.setItem(rowPosition, 2, item)
    def showCompteurDetails(self,compteur):
    	rowPosition = 0
    	self.compteursList.insertRow(rowPosition)
    	item = QtWidgets.QTableWidgetItem()
    	item.setText(compteur.id)
    	self.compteursList.setItem(rowPosition, 0, item)
    	item = QtWidgets.QTableWidgetItem()
    	item.setText(compteur.adresse)
    	self.compteursList.setItem(rowPosition, 1, item)
    def addCompteur(self,compteur):
        self.compteursCB.addItem(compteur.id+" - "+compteur.adresse,compteur)
    def setConsommations(self,consommations):
        if consommations!=None:
            self.clearTable()
            for consommation in consommations:
            	startDate = self.startDate.selectedDate()
            	endDate = self.endDate.selectedDate()
            	if consommation.date >= startDate and consommation.date<=endDate:
	                rowPosition = self.consommationsTable.rowCount()
	                self.consommationsTable.insertRow(rowPosition)
	                valeurItem = QtWidgets.QTableWidgetItem()
	                valeurItem.setText(str(consommation.valeur)+"KWH")
	                self.consommationsTable.setItem(rowPosition, 0, valeurItem)
	                dateItem = QtWidgets.QTableWidgetItem()
	                dateItem.setText(str(consommation.date))
	                self.consommationsTable.setItem(rowPosition, 1, dateItem)
    def calculateTotale(self):
        if self.sUser!=None and self.sCompteur!=None:
            startDate = self.startDate.selectedDate()
            endDate = self.endDate.selectedDate()
            comteurValeur = self.ex.calculateByCompteur(self.sCompteur,startDate,endDate)
            compteursValeur = self.ex.calculateByUser(self.sUser,startDate,endDate)
            self.compteurCons.setText(str(comteurValeur))
            self.compteursCons.setText(str(compteursValeur))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

