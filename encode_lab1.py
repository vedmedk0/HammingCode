import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import Encode
import math
class ExampleApp(QtWidgets.QMainWindow, Encode.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(enter)
def enter():
    global window
    string=window.lineEdit.text()
    k=len(string)
    window.lineEdit_2.setText(str(k))
    m=math.ceil(math.log2(k))+1
    window.lineEdit_3.setText(str(m))
    window.lineEdit_4.setText(str(m+k))
def main():
    global window
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()