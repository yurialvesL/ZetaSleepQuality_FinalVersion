import sqlite3

connection = sqlite3.connect('/home/pi/Documents/projeto tcc/ZSQ/ZSQ/testedb2.db')
cursor = connection.cursor()
#values = ("Sidnei",'1234567','567.681.019-00',0,22,1,7,1,0,5,0,4,'fhfhf')
#cursor.execute("INSERT INTO `usuarios` (`Nome`, `Senha`, `CPF`, `Admin`, `Idade`, `Sexo`,"\
#                " `HorasdeSono`, `Cafe`, `AlcoolOuCigarro`, `Exercícios`, `SonoAgitado`, `NvlStress`, `Previsão`) " \
#                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",values)
#connection.commit()

c = cursor.execute("select * from usuarios")
for row in c :
      print(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
cursor.close()
