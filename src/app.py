import pyodbc
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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
## Agregar tarea

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tareas (descripcion, estado) VALUES (?, ?)", (descripcion, 'No Completado'))
        conn.commit()
        conn.close()
    return redirect(url_for('mostrar_tareas'))



if __name__ == '__main__':
    app.run(debug=True)


