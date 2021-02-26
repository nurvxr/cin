from PyQt5 import QtWidgets,uic

#Bouton valider
def valid() :
    global call_2
    n=call.np.text()
    b=call.cin.text()
    c=call.age.text()
    d=call.tlf.text()

    
    call_2.show()
    
    x=f'Nom et prénom : {n}\nCIN : {b}\nAGE : {c}\nNuméro de téléphone : {d}'
    call_2.complete.setText(x)
    f=open("valid.txt","a")
    f.write("\n")
    f.write("nom&prenom :  ")
    f.write("\n")
    f.write(""+n)
    f.write("\n")
    f.write("CIN :")
    f.write("\n")
    f.write(""+b)
    f.write("\n")
    f.write("Age:")
    f.write("\n")
    f.write(""+c)
    f.write("\n")
    f.write("Numéro de téléphone  :")
    f.write("\n")
    f.write(""+d)
    f.write("\n")
    f.close()

    
def suprimer():
    cin=call.cin.text()
    a=open('valid.txt','r+')
    p=a.readlines()
    x=f''
    for i in range(len(p)):
        if cin in p[i]:
            p[i-3]=x
            p[i-2]=x
            p[i-1]=x
            p[i]=x
            p[i+1]=x
            p[i+2]=x
            p[i+3]=x
            p[i+4]=x
    ch="".join(p)
    a.close()
    a=open('valid.txt','w+')
    a.write(ch)
    a.close()
def quit_2():
    app.quit()

#Boutton annuler
def canceling():
    app.quit()
def main5():
    call5.show()
def rech():
    cin=call5.cin2.text()
    fichier = open("valid.txt","r+")
    p=fichier.readlines()
    for i in range(len(p)):
        if cin in p[i]:
            cin=(p[i])
            np=(p[i-2])
            date=(p[i+2])
            decision=(p[i+4])
            call5.np.setText(np)
            call5.age.setText(date)
            call5.cin.setText(cin)
            call5.descision.setText(decision)
    fichier.close()

#Program principal
app=QtWidgets.QApplication([])
call=uic.loadUi("main.ui")
call_2=uic.loadUi("okform.ui")
call5=uic.loadUi("rechercher.ui")

call.pushButton_3.clicked.connect(main5)
call.pushButton.clicked.connect(valid)
call5.pushButton.clicked.connect(rech)
call5.ok1.clicked.connect(canceling)
call.ok1.clicked.connect(suprimer)
call_2.ok1.clicked.connect(quit_2)
call.show()
app.exec()
