from tkinter import *
from tkinter.ttk import Treeview


class Empresa:

    def __init__(self, app):
        self.app = app
        self.app.title('CRUD de Empresas')
        self.app.geometry('640x480')

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
        btn_insertar.grid(row=4, column=1, columnspan=2)
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
        self.tree.grid(row=5, column=0, pady=20, padx=20)

    def insertar(self):
        nueva_empresa = (self.txt_ruc.get(), self.txt_razon.get(), self.txt_direccion.get())
        self.tree.insert('', END, values=nueva_empresa)
        self.txt_ruc.delete(0, END)
        self.txt_razon.delete(0, END)
        self.txt_direccion.delete(0, END)


app = Tk()

if __name__ == '__main__':
    app_empresa = Empresa(app)
    app.mainloop()
