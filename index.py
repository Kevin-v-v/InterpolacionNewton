from tkinter import ttk
from tkinter import *

valores_x = []
valores_y = []


class interpolacion_newton:

    def __init__(self, window):

        self.wind = window
        self.wind.title('Interpolacion de Newton')

        style = ttk.Style()

        style.configure('TButton', font=('calibri', 10, 'bold', 'underline'),
                        background='red', relief="flat")

        self.frame = Frame(self.wind)
        self.frame.grid(row=0, column=0,
                        pady=(16, 0), padx=16, sticky=W+E)

        self.button_frame = Frame(self.wind)
        self.button_frame.grid(
            row=1, column=0, pady=(0, 16), padx=16, sticky=W+E)

        self.table_frame = Frame(self.wind)
        self.table_frame.grid(
            row=2, column=0, pady=(0, 16), padx=16, sticky=W+E)

        self.error_frame = Frame(self.wind)
        self.error_frame.grid(
            row=3, column=0, pady=(0, 16), padx=16, sticky=W+E)

        self.result_button_frame = Frame(self.wind)
        self.result_button_frame.grid(
            row=4, column=0, pady=(0, 16), padx=16, sticky=W+E)

        self.result_frame = LabelFrame(self.wind, text="Resultado")
        self.result_frame.grid(
            row=5, column=0, pady=(0, 16), padx=16, sticky=W+E)

        Label(self.frame, text='Ingrese el número de pares ordenados:').grid(
            row=0, column=0)

        cantidad = Entry(self.frame)
        cantidad.grid(row=0, column=1, sticky=W+E,
                      padx=5, pady=5,  columnspan=4)
        cantidad.focus()

        self.message = Label(self.frame, text='', fg='red')
        self.message.grid(row=1, column=0, columnspan=4, sticky=W + E)

        Button(self.button_frame, text='Generar tabla', bg="#7986cb", fg="white", relief="flat", command=lambda: self.table_generator(
            cantidad.get())).grid(row=0, column=0, sticky=W+E)

        self.wind.columnconfigure(0, weight=1)

        self.button_frame.rowconfigure(0, weight=1)
        self.button_frame.columnconfigure(0, weight=1)

        self.result_frame.rowconfigure(0, weight=1)
        self.result_frame.columnconfigure(0, weight=1)

        self.result_button_frame.rowconfigure(0, weight=1)
        self.result_button_frame.columnconfigure(0, weight=1)

        self.error_frame.rowconfigure(0, weight=1)
        self.error_frame.columnconfigure(0, weight=1)

        self.table_frame.rowconfigure(0, weight=1)

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

    def table_generator(self, cant):
        if valores_x == []:
            self.message['text'] = ''
        if self.validation_table(cant):
            self.cant = int(cant)
            self.delete_last()
            title1 = Label(self.table_frame, text='x')
            title1.grid(row=0, column=0)
            title2 = Label(self.table_frame, text='y')
            title2.grid(row=1, column=0)

            for i in range(0, int(cant)):
                self.table_frame.columnconfigure(i+1, weight=1)
                x1 = Entry(self.table_frame)
                valores_x.append(x1)
                x1.grid(row=0, column=i+1, padx=5, pady=5, sticky=E+W)
                y1 = Entry(self.table_frame)
                valores_y.append(y1)
                y1.grid(row=1, column=i+1, padx=5, pady=5, sticky=E+W)
            self.exl = Label(
                self.table_frame, text='Ingrese el valor de x a interpolar')
            self.exl.grid(row=2, column=0)
            self.exv = Entry(self.table_frame)
            self.exv.grid(row=2, column=1, padx=5, pady=5, sticky=E+W)
            self.calcB = Button(self.result_button_frame, text='Calcular',
                                bg="#7986cb", fg="white", relief="flat",
                                command=lambda: self.calcular(self.exv.get()))
            self.calcB.grid(row=0, column=0, sticky=W+E)
            self.message2 = Label(self.error_frame, text='', fg='red')
            self.message2.grid(row=0, column=0, sticky=W + E)
        else:
            if valores_x == []:
                self.message['text'] = 'Ingrese una cantidad de pares ordenados válida, Entre 2 y 9'

            else:
                self.message2['text'] = 'Ingrese una cantidad de pares ordenados válida, Entre 2 y 9'

    def delete_last(self):

        self.message = ''
        global valores_x, valores_y
        band = True if valores_x != [] else False
        for element in valores_y:
            element.destroy()

        valores_y.clear()

        for element in valores_x:
            element.destroy()

        valores_x.clear()
        if band:
            self.exl.destroy()
            self.exv.destroy()
            self.message2.destroy()
            self.calcB.destroy()
        if hasattr(self, 'result'):
            self.result.destroy()

    def validation_table(self, cant):
        if cant.isnumeric():
            return int(cant) >= 2 and int(cant) < 10
        else:
            return False

    def validation_x(self, x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def validation_values(self):
        for element in valores_y:
            try:
                float(element.get())
            except ValueError:
                return False
        for element in valores_x:
            try:
                float(element.get())
            except ValueError:
                return False
        return True

    def calcular(self, x):
        try:
            if not self.validation_x(x):
                self.message2['text'] = 'Ingrese un valor a interpolar valido'
                return
            if not self.validation_values():
                self.message2['text'] = 'Ingrese valores validos en los pares ordenados'
                return
            # borrar
            if hasattr(self, 'result'):
                self.result.destroy()
            self.message2['text'] = ''
        

            c_vec = [[0] * (self.cant+1) for i in range(self.cant)]

            for i in range(0, self.cant):

                for j in range(0, self.cant):
                    current = 1
                    for k in range(0, j):
                        current *= float(valores_x[i].get()) - \
                            float(valores_x[k].get())
                    c_vec[i][j] = current
                c_vec[i][j+1] = float(valores_y[i].get())

            print(c_vec)
            res = [0] * self.cant

            for i in range(0, self.cant):
                for k in range(0, i):
                    c_vec[i][self.cant] -= c_vec[i][k]*res[k]
                res[i] = c_vec[i][self.cant] / c_vec[i][i]

            print(res)
            func_sum = 0

            for i in range(0, self.cant):
                current = res[i]
                for k in range(0, i):
                    current *= float(x)-float(valores_x[k].get())
                func_sum += current

            self.result = Label(
                self.result_frame, text='f({}) = {}'.format(x, func_sum))
            self.result.grid(row=0, column=0, pady=16)
            print(func_sum)
        except:
            self.message2['text'] = 'El par ordenado ingresado no puede ser interpolado'


if __name__ == '__main__':
    window = Tk()
    application = interpolacion_newton(window)
    window.mainloop()
