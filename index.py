from tkinter import ttk
from tkinter import *

valores_x = []
valores_y = []
class interpolacion_newton:

    def __init__(self, window):
        
        self.wind = window
        self.wind.title('Interpolacion de Newton')

        frame = LabelFrame(self.wind, text = 'Interpolacion con diferencias divididas de newton')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 5)
        
        Label(self.wind, text = 'Ingrese el número de pares ordenados:').grid(row = 1, column = 0)
        cantidad = Entry(self.wind)
        cantidad.grid(row = 1, column = 1)
        cantidad.focus()
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)
        Button(self.wind, text = 'Generar tabla', command = lambda: self.table_generator(cantidad.get())).grid(row = 3, column =0, sticky= W+E)


    def table_generator(self, cant):
        if valores_x == []:
            self.message['text'] = ''
        if self.validation_table(cant):
            self.cant = int(cant)
            self.delete_last()
            title1 = Label(self.wind, text = 'x')
            title1.grid(row = 4, column = 0)
            title2= Label(self.wind, text = 'y')
            title2.grid(row = 5, column = 0)

            for i in range(0,int(cant)):
                x1 = Entry(self.wind)
                valores_x.append(x1)
                x1.grid(row = 4, column = i+1)
                y1 = Entry(self.wind)
                valores_y.append(y1)
                y1.grid(row = 5, column = i+1)
            self.exl = Label(self.wind, text = 'Ingrese el valor de x a interpolar')
            self.exl.grid(row = 7, column = 0)
            self.exv = Entry(self.wind)
            self.exv.grid(row = 7, column = 1)
            self.calcB= Button(self.wind, text = 'Calcular', command = lambda: self.calcular(self.exv.get()))
            self.calcB.grid(row = 8, column = 0, sticky = W+E)
            self.message2 = Label(text = '', fg = 'red')
            self.message2.grid(row = 9, column = 0, sticky = W + E)
        else:
            if valores_x == []:
                self.message['text'] = 'Ingrese una cantidad de pares ordenados válida, Entre 2 y 9'
                
            else :
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
            return int(cant) >= 2 and int(cant)<10 
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
        if not self.validation_x(x):
            self.message2['text'] = 'Ingrese un valor a interpolar valido'
            return
        if not self.validation_values():
            self.message2['text'] = 'Ingrese valores validos en los pares ordenados'
            return
        #borrar
        if hasattr(self, 'result'):
            self.result.destroy()
        self.message2['text'] = ''
        # values_x = []
        # for element in valores_x:
        #     values_x.append(float (element.get()))
        # if values_x.sort() != values_x:
        #     self.message2['text'] = 'Ingrese valores de x en orden ascendente'
        #     return
        #Ordenamiento innecesario
        # vector_x = []
        # for element in valores_x:
        #     vector_x.append(float(element.get()))
        # vector_y = []
        # for element in valores_y:
        #     vector_y.append(float(element.get()))
        # temp = vector_x
        # vector_x.sort()
        # if temp != vector_x:
        #     print('not sorted')
        #     for index, element in enumerate(temp):
        #         new_index = vector_x.index(element)
        #         val_temp = vector_y[new_index]
        #         vector_y[new_index]= vector_y[index]
        #         vector_y[index]=val_temp
        # print(vector_x)
        # print(vector_y)

        c_vec = [[0] * (self.cant+1) for i in range(self.cant)]
        
        
        for i in range(0, self.cant):
            
            for j in range(0, self.cant):
                current = 1 
                for k in range(0, j):
                    current *= float(valores_x[i].get())-float(valores_x[k].get())
                c_vec[i][j] = current
            c_vec[i][j+1] = float(valores_y[i].get())

        print(c_vec)
        res = [0] * self.cant
        

        for i in range(0, self.cant):    
            for k in range(0, i):
                c_vec[i][self.cant] -= c_vec[i][k]*res[k]
            res[i]= c_vec[i][self.cant] / c_vec[i][i]

        print(res)
        func_sum = 0

        for i in range(0, self.cant):
                current = res[i] 
                for k in range(0, i):
                    current *= float(x)-float(valores_x[k].get())
                func_sum += current
        
        self.result = Label(self.wind, text = 'f({}) = {}'.format(x,func_sum))
        self.result.grid(row = 10, column = 0)
        print(func_sum)
        
if __name__ == '__main__':
    window = Tk()
    application = interpolacion_newton(window)
    window.mainloop()

