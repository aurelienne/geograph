"""
GeoGraph/interface.py
Developed by Aurelienne Jorge (aurelienne@gmail.com)
01/2017
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import converter as sg


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        menu = self.menuBar()
        menu.addMenu('File')

        self.statusBar().showMessage('Ready')

        shapeLbl = QLabel('Arquivo Origem:',self)
        shapeLbl.move(30, 25)
        shapeLbl.resize(150, 25)
        self.shapeEdit = QLineEdit(self)
        self.shapeEdit.setFixedWidth(520)
        self.shapeEdit.move(150, 25)
        bt_search = QPushButton("Localizar",self)
        bt_search.move(680, 25)
        bt_search.clicked.connect(self.showDialogOpen)

        destLbl = QLabel('Arquivo Destino:',self)
        destLbl.move(30, 65)
        destLbl.resize(150, 25)
        self.destEdit = QLineEdit(self)
        self.destEdit.setFixedWidth(520)
        self.destEdit.move(150, 65)
        bt_searchd = QPushButton("Localizar",self)
        bt_searchd.move(680, 65)
        bt_searchd.clicked.connect(self.showDialogSave)

        self.labelImg = QLabel(self)
        self.labelImg.move(30,160)
        self.labelImg.resize(450,300)

        self.labelImgHist = QLabel(self)
        self.labelImgHist.move(515,190)
        self.labelImgHist.resize(280,250)

        lblszx = 200
        lblszy = 20
        self.ordemLbl = QLabel('',self)
        self.ordemLbl.move(100, 480)
        self.ordemLbl.resize(lblszx,lblszy)
        self.compLbl = QLabel('',self)
        self.compLbl.resize(lblszx,lblszy)
        self.compLbl.move(100, 505)
        self.densLbl = QLabel('',self)
        self.densLbl.resize(lblszx, lblszy)
        self.densLbl.move(100, 530)
        self.grauLbl = QLabel('',self)
        self.grauLbl.resize(lblszx, lblszy)
        self.grauLbl.move(440, 480)
        self.coefLbl = QLabel('',self)
        self.coefLbl.resize(lblszx, lblszy)
        self.coefLbl.move(440, 505)
        self.diamLbl = QLabel('',self)
        self.diamLbl.resize(lblszx, lblszy)
        self.diamLbl.move(440, 530)

        bt_exec = QPushButton("Converter",self)
        bt_exec.move(350, 110)
        bt_exec.clicked.connect(self.convert_s2g)

        self.setGeometry(300, 20, 800, 600)
        self.setWindowTitle('GeoGraph')
        self.show()

    def showDialogOpen(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.shapeEdit.setText(fname[0])

    def showDialogSave(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file', '/home')
        self.destEdit.setText(fname[0])

    def convert_s2g(self):
        fnamein = self.shapeEdit.text()
        fnameout = self.destEdit.text()
        _sg = sg.Shp2Graph(fnamein, fnameout)

        pixmap = QPixmap(_sg.grf.figura)
        self.labelImg.setPixmap(pixmap)
        self.labelImg.show()
        pixmapH = QPixmap('histograma.png')
        self.labelImgHist.setPixmap(pixmapH)
        self.labelImgHist.show()

        self.ordemLbl.setText('Ordem: '+str(_sg.grf.ordem))
        self.compLbl.setText('Comprimento: '+str(_sg.grf.comp))
        self.densLbl.setText('Densidade: '+('%.4f' % _sg.grf.densidade))
        self.grauLbl.setText('Grau medio: '+('%.2f' % _sg.grf.grau_medio))
        self.coefLbl.setText('Coef. Aglom. Médio: '+('%.2f' %_sg.grf.coef_aglom_medio))
        self.diamLbl.setText('Diametro: '+('%.2f' % _sg.grf.diametro))

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ma = MyApp()
    sys.exit(app.exec_())