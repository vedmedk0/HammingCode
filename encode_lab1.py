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
        self.a=[]
        self.m=0
        self.e0=0
        self.pushButton.clicked.connect(enter)
        self.pushButton_2.clicked.connect(self.encode)
        self.pushButton_3.clicked.connect(self.decode)
        self.string=""
    def inverse(self,num):
        return (num+1)%2
    def decode(self):
        first=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
        second=[2,3,6,7,10,11,14,15,18,19,22,23,26,27]
        third=[4,5,6,7,12,13,14,15,20,21,22,23,28,29]
        fourth=[8,9,10,11,12,13,14,15,23,24,25,26,27,28]
        fifth=[15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        e1=0
        e2=0
        e3=0
        e4=0
        e5=0
        e0=0
        e0_string=window.lineEdit_5.text()
        string=window.lineEdit_6.text()
        print(string)
        updated_e0=0
        e0=window.lineEdit_6.text()[0]
        for counter in range(1,len(string)):
            if string[counter]=="1":
                updated_e0+=1
            if counter in first and string[counter]=="1":
                e1=e1+1
            if counter in second and string[counter]=="1":
                e2=e2+1
            if counter in third and string[counter]=="1" and len(string)>4:
                e3=e3+1
            if counter in fourth and string[counter]=="1"and len(string)>8:
                e4=e4+1
            if counter in fifth and string[counter]=="1"and len(string)>16:
                e5=e5+1
        e1=e1%2
        e2=e2%2
        e3=e3%2
        e4=e4%2
        e5=e5%2
        updated_e0=updated_e0%2
        if str(updated_e0)!=e0:
            e0=str(updated_e0)
        self.comboBox_2.clear()
        if self.m>0:
            self.comboBox_2.addItem("e1="+str(e1))
            if self.m>1:
                self.comboBox_2.addItem("e2="+str(e2))
                if self.m>2:
                    self.comboBox_2.addItem("e3="+str(e3))
                    if self.m>3:
                        self.comboBox_2.addItem("e4="+str(e4))
                        if self.m>4:
                            self.comboBox_2.addItem("e5="+str(e5))
        self.comboBox_2.addItem("e0="+str(e0))
        #e0=self.inverse(e0)
        print(e0,e1,e2,e3,e4,e5)
        print(self.a)
        check=str(e5)+str(e4)+str(e3)+str(e2)+str(e1)
        print(check)
        S=int(check,2)
        print(S)
        window.lineEdit_7.setText((check))
        r=0
        if S==0 and e0=="0":
           pass
        if (S!=0) and e0=="1":
            r=1
        if  S!=0 and e0=="0":
            r=2
        if S==0 and e0=="1":
            r=2
        window.lineEdit_8.setText(str(r))
        window.lineEdit_9.setText(str(S))
        if r==0:
            
            new_string=list(string)
            del(new_string[0])
            if self.m>0:
                del(new_string[0])
                if self.m>1:
                    del(new_string[0])
                    if self.m>2:
                        del(new_string[1])
                        if self.m>3:
                            del(new_string[4])
            window.lineEdit_9.setText("")
            window.lineEdit_10.setText(str(S))
            res=""
            for x in new_string:
                res+=x
            window.lineEdit_10.setText(res)
        if r==1:

            new_string=list(string)        
            new_string[S-1]=str(self.inverse(int(string[S-1])))
            del(new_string[0])
            if self.m>0:
                del(new_string[0])
                if self.m>1:
                    del(new_string[0])
                    if self.m>2:
                        del(new_string[1])
                        if self.m>3:
                            del(new_string[4])
            window.lineEdit_9.setText(str(S))
            res=""
            for x in new_string:
                res+=x
            window.lineEdit_10.setText(res)
            print(new_string)
        if r==2:
            window.lineEdit_9.setText("")
            window.lineEdit_10.setText("Повторная передача")
    def encode(self):
        first=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28]
        second=[1,2,5,6,9,10,13,14,17,18,20,21,23,24,26]
        third=[3,4,5,6,11,12,13,14,19,20,21,22,27,28]
        fourth=[7,8,9,10,11,12,13,14,23,24,25,26,27,28]
        fifth=[15,16,17,18,19,20,21,22,23,24,25,26,27,28]
        a1=0
        a2=0
        a3=0
        a4=0
        a5=0
        string=self.string
        for counter in range(0,len(string)):
            if counter in first and string[counter]=="1":
                a1=a1+1
            if counter in second and string[counter]=="1":
                a2=a2+1
            if counter in third and string[counter]=="1":
                a3=a3+1
            if counter in fourth and string[counter]=="1":
                a4=a4+1
            if counter in fifth and string[counter]=="1":
                a5=a5+1
        string=list(string)
        if a1%2==1:
            string[0]="1"
        if a2%2==1:
            string[1]="1"
        if a3%2==1:
            string[3]="1"
        if a4%2==1:
            string[7]="1"
        if a5%2==1:
            string[15]="1"   
        a1=a1%2
        a2=a2%2
        a3=a3%2
        a4=a4%2
        a5=a5%2 
        print(a1,a2,a3,a4,a5)
        self.a.append(a1)
        self.a.append(a2)
        self.a.append(a3)
        self.a.append(a4)
        self.a.append(a5)
        self.comboBox.clear()
        if self.m>0:
            self.comboBox.addItem("a1="+str(a1))
            if self.m>1:
                self.comboBox.addItem("a2="+str(a2))
                if self.m>2:
                    self.comboBox.addItem("a3="+str(a3))
                    if self.m>3:
                        self.comboBox.addItem("a4="+str(a4))
                        if self.m>4:
                            self.comboBox.addItem("a5="+str(a5))
        print(string)
        string2=""
        for x in string:
                string2+=x
        for counter in range(0,len(string2)):
            if string2[counter]=="1":
                self.e0+=1
        self.e0=self.e0%2
        string2=str(self.e0)+string2
        window.lineEdit_5.setText(string2)
        window.lineEdit_6.setText(string2)
        print(int(string2,2))
def enter():
    global window
    string=window.lineEdit.text()
    k=len(string)
    window.lineEdit_2.setText(str(k))
    m=math.ceil(math.log2(k))+1
    window.m=m
    window.lineEdit_3.setText(str(m))
    window.lineEdit_4.setText(str(m+k))
    
    pows=[]
    for x in range(0,m):
        string=string[:(2**x)-1]+"0"+string[(2**x)-1:]
        pows.append((2**x)-1)
    print(string)
    window.string=string
def main():
    global window
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()