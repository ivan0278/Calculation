from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

app= QApplication([])
window = QWidget()
window.resize(500,400)
window.setWindowTitle("Розрахунки")

Number1=QLabel('Число1:')
Number2=QLabel('Дія:')
Number3=QLabel('Число2:')

btn_ok=QLabel("Відповідь:")


Number5=QLineEdit()
btn_ok1=QPushButton("+")
Number7=QLineEdit()
btn_ok2=QPushButton("-")
btn_ok3=QPushButton("*")
btn_ok4=QPushButton("/")




v=QVBoxLayout()
v.addWidget(Number1)
v.addWidget(Number7)


v.addWidget(Number3)
v.addWidget(Number5)
h=QHBoxLayout()
h.addWidget(btn_ok1)
h.addWidget(btn_ok2)
h.addWidget(btn_ok3)
h.addWidget(btn_ok4)
v.addWidget(Number2)
v.addLayout(h)




v.addWidget(btn_ok)


window.setLayout(v)




def plus():
    a=int(Number5.text())
    b=int(Number7.text())
    c=a+b
    btn_ok.setText(str(c))
btn_ok1.clicked.connect(plus)

def minus():
    d=int(Number5.text())
    n=int(Number7.text())
    k=n-d
    btn_ok.setText(str(k))
btn_ok2.clicked.connect(minus)

def mnogenna():
    u=int(Number5.text())
    o=int(Number7.text())
    y=u*o
    btn_ok.setText(str(y))
btn_ok3.clicked.connect(mnogenna)

def dilena():
    p=int(Number5.text())
    e=int(Number7.text())
    q=e/p
    btn_ok.setText(str(q))
btn_ok4.clicked.connect(dilena)

window.show()
app.exec_()