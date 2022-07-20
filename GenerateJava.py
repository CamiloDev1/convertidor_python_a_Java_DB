import os
import re
class GenerateJava:
    def extraer_datos_clave(manup):
        patron = r'"(.*?)"'
        texto = re.findall(patron,manup)
        datos=[]
        for i in texto:
            datos.append(i)
            print(datos[0])
        GenerateJava.generar_Archivo(datos)

    def generar_Archivo(datos):
        file = open("ConnecDataBase.java", "w")
        file.write("\nimport java.sql.Connection;")
        file.write("\nimport java.sql.DriverManager;")
        file.write("\nimport java.sql.SQLException;"+os.linesep)
        file.write("\npublic class connect {")
        file.write('public String driver = "com.mysql.jdbc.Driver";'+os.linesep)
        file.write('public String database = "'+datos[3]+'";'+os.linesep)
        file.write('public String hostname = "'+datos[0]+'";'+os.linesep)
        file.write('public String port = "3306";'+os.linesep)
        file.write('public String url = "jdbc:mysql://" + hostname + ":" + port + "/" + database + "?useSSL=false";'+os.linesep)
        file.write('public String username = "'+datos[1]+'";'+os.linesep)
        file.write('public String password = "'+datos[2]+'";'+os.linesep)
        file.write('    public Connection conexion() {'+os.linesep)
        file.write('        Connection conn = null;'+os.linesep)
        file.write('        try {'+os.linesep)
        file.write('            Class.forName(driver);'+os.linesep)
        file.write('            conn = DriverManager.getConnection(url, username, password);'+os.linesep)
        file.write('        } catch (ClassNotFoundException | SQLException e) {'+os.linesep)
        file.write('            e.printStackTrace();'+os.linesep)
        file.write('        }'+os.linesep)
        file.write('        return conn;'+os.linesep)
        file.write('    }'+os.linesep)
        file.write('}'+os.linesep)
        file.close()
