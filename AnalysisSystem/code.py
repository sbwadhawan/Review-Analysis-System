from PyQt5 import QtCore, QtGui, QtWidgets
import SentimentAnalysis
import csv, re
import numpy as np
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 90, 711, 191))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 340, 401, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 351, 51))
        self.label.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 791, 531))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 141, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 141, 41))
        self.label_3.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 121, 41))
        self.label_4.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 100, 111, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 170, 111, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 250, 111, 31))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 370, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(460, 50, 291, 411))
        self.listWidget.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.listWidget.setObjectName("listWidget")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 10, 801, 521))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 600, 300))
        self.label_5.setObjectName("label_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 370, 120, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Review"))
        self.label.setText(_translate("MainWindow", "Review Analysis System"))
        self.label_2.setText(_translate("MainWindow", "Positive Review"))
        self.label_3.setText(_translate("MainWindow", "Negative Review"))
        self.label_4.setText(_translate("MainWindow", "Total Review"))
        self.pushButton_2.setText(_translate("MainWindow", "Show Accuracy"))
        self.pushButton_3.setText(_translate("MainWindow", "Visualize"))
        self.frame.hide()

        self.pushButton.clicked.connect(self.showAnalysis)
        self.pushButton_2.clicked.connect(self.showAccuracy)
        self.pushButton_3.clicked.connect(self.visualize)
        # self.printAnalysis()

    def showAnalysis(self):
        self.frame.show()
        self.frame_2.hide()
        self.printAnalysis()
        self.prediction()

    def printAnalysis(self):
        try:
            file = open('prediction.txt')
            self.data = file.read()
            # print(self.data)
            pattern = '([0-9]\d+|[0-9])'
            counts = re.findall(pattern, self.data)
            self.negCount = int(counts[0])
            self.posCount = int(counts[1])
            self.textEdit_2.setText(counts[1])
            self.textEdit_3.setText(counts[0])
            self.textEdit_4.setText(str(int(counts[0])+int(counts[1])))

        except BaseException:
            file = open('prediction.txt','w')
            data = "Negative : 0, Positive : 0"
            file.write(data)
        finally:
            file.close()

    def prediction(self):
        text = self.textEdit.toPlainText()
        pred = SentimentAnalysis.test(text)
        # print(pred)
        if pred == 'Negative':
            self.negCount += 1
        else:
            self.posCount += 1

        self.readWrite(self.negCount, self.posCount)
        self.saveReview(text,pred)

    def readWrite(self,neg,pos):
        with open('prediction.txt','w') as file:
            data = "Negative : {}, Positive : {}".format(neg,pos)
            file.write(data)
        self.printAnalysis()

    def saveReview(self,text,pred):
        try:
            file = open('reviews.csv','a',newline='')
            data = {"review":text, "pred":pred}
            writer = csv.writer(file)
            writer.writerow(data.values())
            file.close()

            file = open('reviews.csv')
            reader = csv.reader(file)
            data = list(reader)
            for i in range(len(data)):
                self.listWidget.addItem(data[i][0])
                # item.setText(data[i][0])
            file.close()
        except BaseException as ex:
            print(ex)

    def visualize(self):
        try:
            self.frame_2.show()
            x = np.array([int(self.negCount), int(self.posCount)])
            # print(x)
            labels = ['Negative', 'Positive']
            plt.pie(x,labels=labels,autopct='%1.1f%%')
            # plt.show()
            plt.savefig('plot.png')
            image = QtGui.QPixmap('plot.png')
            self.label_5.setPixmap(image)
        except BaseException as ex:
            print(ex)

    def showAccuracy(self):
        self.frame_2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
