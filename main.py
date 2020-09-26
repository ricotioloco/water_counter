import sys, random
from PyQt5 import QtCore, QtGui, QtWidgets
from generator_window import *
from functools import reduce

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Generator()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.mainFunction)

    def mainFunction(self):
        number_of_days = self.ui.textEdit.toPlainText()
        total_amount_water = self.ui.textEdit_2.toPlainText()
        coefficient = self.ui.textEdit_3.toPlainText()
        coefficient = float(coefficient)
        number_of_days = int(number_of_days)
        total_amount_water = int(total_amount_water)

        res = 0
        step_for = 0
        step_while = 0

        while res != total_amount_water:
            values = []
            for i in range(number_of_days):
                value = random.randint(round((total_amount_water / number_of_days) -
                                             ((total_amount_water / number_of_days) * coefficient)),
                                       round((total_amount_water / number_of_days) + (
                                                   (total_amount_water / number_of_days) * coefficient)))
                if step_for == 0 or value != values[i - 1]:
                    values.append(value)
                else:
                    values.append(value - 1)
                step_for += 1
            step_for = 0
            step_while += 1
            res = reduce(lambda x, y: x + y, values)

            # values = [(random.randint(
            #     round((total_amount_water / number_of_days) - ((total_amount_water / number_of_days) * coefficient)),
            #     round((total_amount_water / number_of_days) + ((total_amount_water / number_of_days) * coefficient))))
            #           for i in range(number_of_days)]
            # res = reduce(lambda x, y: x + y, values)

        res = []
        day = 1
        for value in values:
            res.append(f'День {day}\t-\t{value}')
            day += 1

        res = '\n'.join(res)

        self.ui.textBrowser.setText(res)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    sys.exit(app.exec_())
