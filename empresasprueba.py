from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector

class Empresa:

    def __init__(self, app):
        self.app = app
        self.app.title('CRUD de Empresas')
        self.app.geometry('640x480')

        self.empresa_id = 0

        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='db_g4'
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error al conectar o ejecutar la consulta: {e}")

        frame = LabelFrame(self.app, text='Nueva Empresa')
        frame.grid(row=0, column=0, columnspan=2, pady=10, padx=10)
        lb_ruc = Label(frame, text='RUC : ')
        lb_ruc.grid(row=1, column=0)
        self.txt_ruc = Entry(frame)
        self.txt_ruc.grid(row=1, column=1)

        lb_razon = Label(frame, text='Razón Social : ')
        lb_razon.grid(row=2, column=0)
        self.txt_razon = Entry(frame)
        self.txt_razon.grid(row=2, column=1)
        lb_direccion = Label(frame, text='Dirección : ')
        lb_direccion.grid(row=3, column=0)
        self.txt_direccion = Entry(frame)
        self.txt_direccion.grid(row=3, column=1)

        btn_insertar = Button(frame, text='Insertar Nueva Empresa', command=self.insertar)
        btn_insertar.grid(row=4, column=0, columnspan=2)

        btn_eliminar = Button(frame, text='Eliminar Empresa', command=self.eliminar)
        btn_eliminar.grid(row=5, column=0, columnspan=2)

        self.tree = Treeview(self.app)
        self.tree['columns'] = ('RUC', 'Razón Social', 'Dirección')

        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('RUC')
        self.tree.column('Razón Social')
        self.tree.column('Dirección')

        self.tree.heading('#0', text='id')
        self.tree.heading('RUC', text='RUC')
        self.tree.heading('Razón Social', text='Razón Social')
        self.tree.heading('Dirección', text='Dirección')

        self.tree.grid(row=6, column=0, pady=20, padx=20)

    def limpiar_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def cargar_empresas(self):
        self.limpiar_tree()
        self.cursor.execute("SELECT id, ruc, razon_social, direccion FROM empresa ORDER BY id ASC")
        for row in self.cursor.fetchall():
            empresa_row = (row[1], row[2], row[3])
            self.tree.insert('', 0, text=row[0], values=empresa_row)

    def insertar(self):
        nueva_empresa = (
            self.txt_ruc.get(),
            self.txt_razon.get(),
            self.txt_direccion.get()
        )
        query = "INSERT INTO empresa (ruc, razon_social, direccion) VALUES (%s, %s, %s)"
        self.cursor.execute(query, nueva_empresa)
        self.connection.commit()
        self.cargar_empresas()

    def eliminar(self):
        seleccion = self.tree.selection()
        if seleccion:
            self.empresa_id = self.tree.item(seleccion[0])["text"]
            respuesta = messagebox.askyesno("Confirmación", "¿Está seguro que desea eliminar el registro?")
            if respuesta:
                query = "DELETE FROM empresa WHERE id=%s"
                self.cursor.execute(query, (self.empresa_id,))
                self.connection.commit()
                self.cargar_empresas()
        else:
            messagebox.showerror('Alerta', 'Por favor seleccione un registro')

app = Tk()

if __name__ == '__main__':
    app_empresa = Empresa(app)
    app_empresa.cargar_empresas()
    app.mainloop()
