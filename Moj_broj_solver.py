#sdasdasda
"""
ovo je moj komentar 
E - set of all valid expressions
Q - queue of expressions that have not been expanded yet
N - set of input numbers
v - target value

Goal: To create an expression N->v, which uses all numbers from N to produce value v

for all numbers n in N
    Add expression n->n to Q
    Add expression n->n to E

while Q is not empty and E does not contain expression N->v
    begin
        e = expression dequeued from Q
        for each expression f in E
            begin
                G = set of expressions obtained by combining e and f
                for each expression g in G
                    if g is not in E then
                        Enqueue g to Q
                        Add g to E
            end
    end

if E contains expression N->v then
    print expression N->v"""

import queue
import math
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QLineEdit,QMessageBox,QPushButton,QLabel
import sys
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QPainter, QColor , QIcon, QPixmap


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Moj Broj Resavac'
        self.left = 500
        self.right = 300
        self.width = 780
        self.height = 365
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.right,self.width,self.height)

        self.setStyleSheet("background:rgb(186,228,245)")

        self.label = QLabel(self)
        self.label.move(400,20)
        pixmap = QPixmap('logo.jpg')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width()-20,pixmap.height())

        self.resultTextBox = QLineEdit(self)
        self.resultTextBox.move(150,20)
        self.resultTextBox.resize(100,30)
        self.resultTextBox.setStyleSheet("background:white;")

        self.textBox1 = QLineEdit(self)
        self.textBox1.move(20,80)
        self.textBox1.resize(40,20)
        self.textBox1.setStyleSheet("background:white;")

        self.textBox2 = QLineEdit(self)
        self.textBox2.move(70,80)
        self.textBox2.resize(40,20)
        self.textBox2.setStyleSheet("background:white;")

        self.textBox3 = QLineEdit(self)
        self.textBox3.move(120,80)
        self.textBox3.resize(40,20)
        self.textBox3.setStyleSheet("background:white;")

        self.textBox4 = QLineEdit(self)
        self.textBox4.move(170,80)
        self.textBox4.resize(40,20)
        self.textBox4.setStyleSheet("background:white;")

        self.textBox5 = QLineEdit(self)
        self.textBox5.move(240,80)
        self.textBox5.resize(60,20)
        self.textBox5.setStyleSheet("background:white;")

        self.textBox6 = QLineEdit(self)
        self.textBox6.move(310,80)
        self.textBox6.resize(60,20)
        self.textBox6.setStyleSheet("background:white;")

        self.button = QPushButton('RESI',self)
        self.button.move(150,120)
        self.button.clicked.connect(self.on_click)
        self.button.setStyleSheet("background:rgb(95,137,245);")

        self.resultStringBox = QLineEdit(self)
        self.resultStringBox.move(20,180)
        self.resultStringBox.resize(350,30)
        self.resultStringBox.setStyleSheet("background:white;")
        
        self.show()


    @pyqtSlot()
    def on_click(self):
        input_numbers=[]
        indikator_greske=0
        if(self.textBox1.text().isnumeric()):
            input_numbers.append(int(self.textBox1.text()))
            indikator_greske+=1
        if(self.textBox2.text().isnumeric()):
            input_numbers.append(int(self.textBox2.text()))
            indikator_greske+=1
        if(self.textBox3.text().isnumeric()):    
            input_numbers.append(int(self.textBox3.text()))
            indikator_greske+=1
        if(self.textBox4.text().isnumeric()):
            input_numbers.append(int(self.textBox4.text()))
            indikator_greske+=1
        if(self.textBox5.text().isnumeric()):
            input_numbers.append(int(self.textBox5.text()))
            indikator_greske+=1
        if(self.textBox6.text().isnumeric()):
            input_numbers.append(int(self.textBox6.text()))
            indikator_greske+=1
        if(self.resultTextBox.text().isnumeric()):
            result  = int(self.resultTextBox.text())
            indikator_greske+=1
        if(indikator_greske==7):
            string = solveAndPrint(input_numbers,result)
        else:
            string = "neispravan unos! "
        self.resultStringBox.setText(string)


#500,300,800,500
def solveAndPrint(input_numbers, result):
    targetKeys=[]
#    for i in range (0,2**6-1):
#        targetKeys.append((result<<len(input_numbers))+i)


    #skup kljuceva koji jedinstvenp pdredjuju izraz (vrednost+brojevi)
    solvedKeys= set([])

    #mapa koja slika kljuc izraza u kljuc levog roditelja
    keyToLeftParent={}

    #mapa koja slika kljuc izraza u kljuc desnog roditelja
    keyToRightParent={}

    #mapa koja slika kljuc izraza u operator kojim je dobijen
    keyToOperator={}

    #red koji ce sadrzati sve izraze koji cekaju da se obrade
    red=queue.Queue()
    newKeys= []
    #dodajemo sve brojeve ulaza u red
    for i in range(0,len(input_numbers)):
        key=(input_numbers[i]<<len(input_numbers))+(1<<i)
        solvedKeys.add(key)
        red.put(key)
    while not red.empty():
#        for item in targetKeys:
#            if solvedKeys.__contains__(item):
#                break
        curKey=red.get()
        # trenutna vrednost
        curValue = curKey>>len(input_numbers)
        #trenutne vrednosi upotrebljene
        curMask=curKey & ((1<<len(input_numbers))-1)

        #kopiramo trenutno stanje kljuceva
#        keys=[]
#        for key in solvedKeys:
#            keys.append(key)
        #prolazimo kroz sve validne kljuceve/izraze]
        for Key in newKeys:
            solvedKeys.add(Key)

        newKeys=[]

        newKey=0
        targetKey=0
        
        for izraz in solvedKeys:
            #izvlacimo promenljive koje su u izrazu
            mask=izraz & ((1<<len(input_numbers))-1)

            #vrednost tog izraza
            value=izraz >> len(input_numbers)

            #ukoliko koristimo disjunktne ulazne brojeve mozemo dalje
            if (curMask & mask)==0:
                for j in range(0,len(['+','*','-','/'])):
                    newValue=0
                    opSign=''
                    if j==0:
                        newValue=curValue+value
                        opSign='+'
                    elif j==1:
                        newValue=curValue*value
                        opSign='*'
                    elif j==2:
                        newValue=curValue-value
                        opSign='-'
                    elif j==3:
                        newValue=-1
                        if value != 0 and curValue % value ==0:
                            newValue=curValue // value
                            opSign='/'
                    else:
                        newValue=-1
                    if newValue>=0:
                        newMask=(curMask|mask)
                        newKey = (newValue << len(input_numbers))+newMask
                        if not solvedKeys.__contains__(newKey) and not newKeys.__contains__(newKey):
                            newKeys.append(newKey)
                            keyToLeftParent.update({newKey:curKey})
                            keyToRightParent.update({newKey:izraz})
                            keyToOperator.update({newKey:opSign})
                            red.put(newKey)
                        if newValue == result: 
                            targetKey=newKey
                            return printExpression(keyToLeftParent,keyToRightParent,keyToOperator,targetKey,len(input_numbers))+"= "+str(result)
                            return
    closest = nadjiNajblize(solvedKeys , result,len(input_numbers))
    return printExpression(keyToLeftParent,keyToRightParent,keyToOperator,closest, len(input_numbers)) +"= "+str(closest>>len(input_numbers)) 

def nadjiNajblize(solvedKeys,result,n):
    closest=0
    for izraz in solvedKeys:
        if(abs(result-(izraz>>n))<abs(result-(closest>>n))):
            closest = izraz 
    return closest
def printExpression(keyToLeftParent,keyToRightParent,keyToOperator,targetKey,n):
    if not keyToOperator.keys().__contains__(targetKey):
        return str(targetKey>>n)
#        print(str(targetKey>>n)+"",end='')
    else:
#        print("(",end='')
#        printExpression(keyToLeftParent,keyToRightParent,keyToOperator,keyToLeftParent.get(targetKey),n)
#        print(keyToOperator.get(targetKey),end='')
#        printExpression(keyToLeftParent,keyToRightParent,keyToOperator,keyToRightParent.get(targetKey),n)
#        print(")",end='')
        return "(" +printExpression(keyToLeftParent,keyToRightParent,keyToOperator,keyToLeftParent.get(targetKey),n) +keyToOperator.get(targetKey)+printExpression(keyToLeftParent,keyToRightParent,keyToOperator,keyToRightParent.get(targetKey),n)+")"

def main():
#    result=int(input("Ciljni broj: "))
#    input_numbers=[]
#    for i in range(0,6):
#        broj=int(input("Unesi broj : "))
#        input_numbers.append(broj)
#    start_time=time.time()
#    print(solveAndPrint(input_numbers,result))
#    end_time=time.time()
#    print("\n")
#    print(str(end_time-start_time),end='\n')

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#    app = QApplication(sys.argv)
#    win = QMainWindow()
#    win.setGeometry(500,300,800,500)
#    win.setWindowTitle("Moj broj resavac")
#    textBox1= QLineEdit(win)
#    textBox1.move(20,20)
#    textBox1.resize(200,40)
#    textBox1.setText("Proba")


#    button = QPushButton('Show text',win)
#    button.move(20,80)

#    button.clicked.connect(on_click)

#    win.show()
#    sys.exit(app.exec_())

if __name__=="__main__":
    main()


