from operator import pos
import re
from turtle import clear
from ventana_ui import *
import GenerateJava
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    manup = ''
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.botton_ingresar.clicked.connect(self.analizar)
        self.botton_reiniciar.clicked.connect(self.reiniciar)
        self.botton_Generar.blockSignals(True)
        self.palabras = []
        self.pila = []
        self.tabla_predictiva = [["", "a..z", "0..9", "(", ")", ":", ".", "-", ",", "def", "mysql", "class", "connect", "conexion:", "database", "passwd", "=", "mydb=", "host", "user", '"', "connector", "$"],
                                 ["C", "", "", "", "", "", "", "", "", "", "", [
                                     "CLASE", "DF", "ESTRUCTURA"], "", "", "", "", "", "", "", "", "", "", ""],
                                 ["CLASE", "", "", "", "", "", "", "", "", "", "", [
                                     "CLASS", "CONNECT", "DP"], "", "", "", "", "", "", "", "", "", "", ""],
                                 ["CLASS", "", "", "", "", "", "", "", "", "", "",
                                  "class", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["CONNECT", "", "", "", "", "", "", "", "", "", "", "",
                                  "connect", "", "", "", "", "", "", "", "", "", ""],
                                 ["CONEXION", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "conexion:", "", "", "", "", "", "", "", "", ""],
                                 ["CONNECTOR", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "connector", ""],
                                 ["MYSQL", "", "", "", "", "", "", "", "", "", "mysql",
                                  "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["DP", "", "", "", "", ":", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", ""],
                                 ["IG", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "=", "", "", "", "", "", ""],
                                 ["DF", "", "", "", "", "", "", "", "", ["DEF", "CONEXION"],
                                  "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["DEF", "", "", "", "", "", "", "", "", "def", "",
                                  "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["ESTRUCTURA", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ["MYDB", "SQLC", "PA",
                                                                                                                 "H", "RH", "CO", "US", "RUS", "CO", "PWD", "RPWD", "CO", "DB", "RDB", "PC"], "", "", "", "", ""],
                                 ["MYDB", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "mydb=", "", "", "", "", ""],
                                 ["SQLC", "", "", "", "", "", "", "", "", "", ["MYSQL", "PT", "CONNECTOR",
                                                                               "PT", "CONNECT"], "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["PA", "", "", "(", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["H", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", ["host", "IG"], "", "", "", ""],
                                 ["RH", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", ["CM", "ID", "CM"], "", ""],
                                 ["CO", "", "", "", "", "", "", "", ",", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", ""],
                                 ["US", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", ["user", "IG"], "", "", ""],
                                 ["CM", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", '"', "", ""],
                                 ["RUS", "", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", ["CM", "ID", "CM"], "", ""],
                                 ["PWD", "", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", ["passwd", "IG"], "", "", "", "", "", "", ""],
                                 ["RPWD", "", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", ["CM", "ID", "CM"], "", ""],
                                 ["DB", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                  ["database", "IG"], "", "", "", "", "", "", "", ""],
                                 ["RDB", "", "", "", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", ["CM", "ID", "CM"], "", ""],
                                 ["PT", "", "", "", "", "", ".", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", ""],
                                 ["LETRA", "a..z", "", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["DIGITO", "", "0..9", "", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["ID", ["LETRA", "COMPLEMENTO"], "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["IP", "", ["DIGITO", "COMPLEMENTOIP"], "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["COMPLEMENTO", ["LETRA", "COMPLEMENTO"], "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["COMPLEMENTOIP", "", ["DIGITO", "PT"], "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
                                 ["PC", "", "", "", ")", "", "", "", "", "", "", "",
                                  "", "", "", "", "", "", "", "", "", "", ""],
                                 ]

    def fragmentar_lineas(self):
        manup = self.palabras.copy()
        self.palabras.clear()
        for i in manup:
            aux = i.split(" ")
            print(aux)
            for y in aux:
                self.palabras.append(y)

    def fragmentar_texto(self, manup):
        manup = manup.split("\n")
        for i in manup:
            print(i)
            aux = i.split("\t")
            if len(aux) == 1:
                self.palabras.append(aux[0])
            else:
                self.palabras.append(aux[1])
        self.fragmentar_lineas()
        print(self.palabras)

    def eval_id(self, id):
        patron2 = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        patron = re.compile('\Alocalhost')
        patron3 = re.compile('[a-z]+')
        if patron.match(id) != None or patron2.match(id) != None or patron3.match(id) != None:
            return True
        else:
            return False
    def eval_ip(self, ip):
        patron2 = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if patron2.match(ip) != None:
            return True
        else:
            return False

    def algoritmo_tabla_predictiva(self,manup):
        
        self.pila.append("C")
        while len(self.palabras) != 0:
            print("Cima de la pila: ", self.pila[0])
            print("Palabra de entrada: ", self.palabras[0])
            if self.palabras[0] == self.pila[0] or self.pila[0] == "ID":
                if self.pila[0] == "ID":
                    if self.eval_id(self.palabras[0]) == False:
                        self.aviso.setText("Error: El algoritmo no es valido.")
                        break
                self.palabras.pop(0)
                self.pila.pop(0)
            else:
                posx = 0
                posy = 1
                while self.palabras[0] != self.tabla_predictiva[posx][posy] and posy < 22:
                    posy += 1
                print("Selccionado FINAL x: ",
                      self.tabla_predictiva[posx][posy])
                posx2 = 0
                posy2 = 0
                while self.pila[0] != self.tabla_predictiva[posx2][posy2] and posx2 < 33:
                    posx2 += 1
                print("Selccionado FINAL y: ",
                      self.tabla_predictiva[posx2][posy2])
                if self.tabla_predictiva[posx2][posy] == "":
                    self.aviso.setText("Error: El algoritmo no es valido.")
                    break
                else:
                    self.pila.pop(0)
                    if(type(self.tabla_predictiva[posx2][posy]) == list):
                        print("Lista", self.tabla_predictiva[posx2][posy])
                        aux = self.tabla_predictiva[posx2][posy].copy()
                        aux = aux[::-1]
                        print("Aux: ", aux)
                        for i in aux:
                            self.pila.insert(0, i)
                    else:
                        self.pila.insert(0, self.tabla_predictiva[posx][posy])
        if len(self.pila) == 0  and len(self.palabras)== 0 :
            self.aviso.setText("El algoritmo es valido.")
            bandera = True
            if bandera == True:
                self.botton_Generar.blockSignals(False)
                self.botton_Generar.clicked.connect(lambda: MainWindow.generar_archivo_java(manup))
        else:
            self.aviso.setText("Error: El algoritmo no es valido.")
    def validar_host(self,manup):
        patron2 = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        patron3 = re.compile(r"localhost\\b")
        patron = r'"(.*?)"'
        texto = re.findall(patron,manup)
        datos=[]
        for i in texto:
            datos.append(i)
            print(datos[0])
        host = datos[0].split(" ")
        print(host)
        if host[1] == "localhost" or patron2.match(host[1]) != None:
            print("Host Correcto")
            self.fragmentar_texto(manup)
        else:
            print("Host incorrecto")
            self.aviso.setText("Error: El algoritmo no es valido.")
    def generar_archivo_java(manup):
        GenerateJava.GenerateJava.extraer_datos_clave(manup)
    def analizar(self):
        manup = self.ingreso_texto.toPlainText()
        self.validar_host(manup)
        self.algoritmo_tabla_predictiva(manup)
    def reiniciar(self):
        self.ingreso_texto.clear()
        self.aviso.clear()
        self.palabras.clear()
        self.pila.clear()
        os.system("cls")
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
