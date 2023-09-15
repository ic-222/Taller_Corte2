import pyodbc
from flask import Flask, render_template

app = Flask(__name__)

## CONECTAR BASE DE DATOS DESDE ACCESS
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\cuc\Documents\1509\Parcial1\TaskDB.accdb;'
)

def conectar_bd():
    return pyodbc.connect(conn_str)

# ## APP
@app.route('/')
def mostrar_tasks():
    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Tareas')
    tareas = cursor.fetchall()
    conn.close()
    return render_template('mostrar_tareas.html', tareas=tareas)

## AGREGAR ACCIONES



if __name__ == '__main__':
    app.run(debug=True)


