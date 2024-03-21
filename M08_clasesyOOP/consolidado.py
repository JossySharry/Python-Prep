class Total_funciones:
    def __init__(self, lis_num):
        self.lista = lis_num
    # mostrar primo o no
    def func_primo(self):
        
        for i in self.lista:
            if (self.__func_primo(i)):
                print('El número', i, 'SI es primo')
            else:
                print('El número', i, 'NO es primo')
    # mostrar grados
    def convertir_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__convertir_grados(i,origen,destino),'grados', destino)

    #mostrar factorial
    def factorial_num(self):
        for i in self.lista:
            print('el factorial de ', i, 'es ', self.__factorial_num(i))

    # verifica primo
    def __func_primo(self, num):
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        return primo #print('El número', str(num), 'es primo')


    # Valor modal
    def elemento_mas_repetido(self):
        contador = {}#creamos un diciconario vacio para almacenar la cantidad de veces que un elemento parece en la lista
        for elemento in self.lista:
            if elemento in contador:
                contador[elemento] += 1
            else:
                contador[elemento] = 1
        
        elemento_mas_repetido = None
        max_repeticiones = 0
        for elemento, repeticiones in contador.items():
            if repeticiones > max_repeticiones:
                max_repeticiones = repeticiones
                elemento_mas_repetido = elemento
        
        return elemento_mas_repetido, max_repeticiones

    # conversion grados
    def __convertir_grados(self,num, grado_orgin,grado_dest):
        devuelve_valor= None
        if grado_orgin=='celsius':
            if grado_dest=='celsius':
                devuelve_valor=num
            elif grado_dest=='kelvin':
                devuelve_valor=num+273.15
            elif grado_dest=='farenheit':
                devuelve_valor=(num*9/5)+32 
            else:
                print('Los valores ingresados son incorrectos')
        elif grado_orgin=='kelvin':
            if grado_dest=='celsius':
                devuelve_valor=num-273.15
            elif grado_dest=='kelvin':
                devuelve_valor=num
            elif grado_dest=='farenheit':
                devuelve_valor=((num-273.15)*9/5)+32
            else: 
                print('Los valores ingresados son incorrectos')
        elif grado_orgin=='farenheit':
            if grado_dest=='celsius':
                devuelve_valor=(num-32)*5/9
            elif grado_dest=='kelvin':
                devuelve_valor=((num-32)*5/9)+273.15
            elif grado_dest=='farenheit':
                devuelve_valor=num
            else:
                print('Los valores ingresados son incorrectos')
        else:
            print('Valores ingresados incorrectos')
        return devuelve_valor

    # Factorial
    def __factorial_num(self, valor):
        if type(valor) != int:
            return('Ingrese un número entero')
        if valor <0:
            return print('El número debe ser positivo')
        if valor <=1:
            return 1
        devuelve_factorial = valor * self.__factorial_num(valor-1)
        return devuelve_factorial