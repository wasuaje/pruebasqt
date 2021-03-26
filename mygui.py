
from PyQt4 import *
from PyQt4.QtGui import QApplication, QDialog

from form1 import *
import sys



class MyMain(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)        
        self.setupUi(self)        

    def Limpia(self):
		self.comboBox.clear()
		print "limpiaS"

    def AddEntry(self):
        e=self.lineEdit.text()        
        self.comboBox.addItem(e)
        self.lineEdit.clear()                
        print "agrega"	
	

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMain()
    myapp.show()
    sys.exit(app.exec_())