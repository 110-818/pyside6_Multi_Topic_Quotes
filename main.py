import sys
from main_window import Ui_Dialog
from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox,QDialog
from functools import partial
from database import SQl
import random as rand

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label.setWordWrap(True)
        self.items = []
        self.db = SQl("databaseDB.db")
        self.ui.comboBox_1.addItem("جوک")
        self.ui.comboBox_1.addItem("انگیزشی / اندرزی")
        self.ui.comboBox_1.addItem("اطلاعات فیلم")
        self.ui.comboBox_1.addItem("رخداد تاریخی")
        self.ui.pushButton_next.clicked.connect(partial(self.show_info))

    def load(self):
        if self.ui.comboBox_1.currentText() == "جوک":
            self.items = self.db.read("joke")

        elif self.ui.comboBox_1.currentText() == "انگیزشی / اندرزی":
            self.items = self.db.read("motivational")

        elif self.ui.comboBox_1.currentText() == "اطلاعات فیلم":
            self.items = self.db.read("Film_Information")

        elif self.ui.comboBox_1.currentText() == "رخداد تاریخی":
            self.items = self.db.read("Historical_event")


    def show_info(self):
        self.load()
        item = rand.choice(self.items)
        text = ""
        for i in range(len(item)):
            if i == 0:
                continue
            elif i == None:
                continue
            else:
                text = f"{text} \n {item[i]}"
        self.ui.label.setText(text)

app = QApplication(sys.argv)
main = Main()
main.show()
app.exec()