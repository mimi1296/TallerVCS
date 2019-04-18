#El problema, es realizar un programa en el que la dueÃ±a de una empresa, pueda
#ingresar la cantidad de productos, los clientes que atiende, le indique sus ganancias o perdidas.
#Entradas: int(Cantidad de clientes) int(cantidad de productos)
#str(nombre) int(edad) int(premios) int(costo) int(venta)
#Salidas: eval(ganancias) int(promEdad) int(TotalCosto)
#int(TotalVenta) int(premios)str (nombre cliente)
#Restricciones: Debe haber al menos 1 cliente y 1 producto
#Pesudocodigo: Se digitan todos los datos requeridos de los clientes,
#despues, dependiendo de si son mas de 1 cliente, se calcula la edad promedio
#y el valor de su compra, junto con la ganancia/perdida que obtenga la dueÃ±a.
#Se mostrara una factura individual para cada cliente que compre x cantidad de productos.


clientes = int(input("Ingrese la cantidad de clientes que va a antender\n"))
productos = int(input("Ingrese la cantidad de productos\n"))
def Venta (clientes, productos):
    if clientes == 1 and productos == 1:
        nombre = str(input("Ingrese el nombre del cliente, por favor:\n"))
        edad = int(input("Ingrese la edad del cliente, por favor:\n"))
        productoF = str(input("Ingrese el producto favorito, por favor:\n"))
        campaÃ±a = int(input("Ingrese el nÃºmero de campaÃ±a, por favor:\n"))
        Premio = int(input("Â¿CuÃ¡ntos premios recibe por esta venta?\n"))
        producto = str(input("Diga el nombre del producto\n"))
        valorCosto = int(input("Ingrese el costo del producto\n"))
        valorVenta = int(input("Ingrese el valor de venta del producto\n"))
        Ingreso = productos * valorVenta
        Costo = productos * valorCosto
        Ganancia = Ingreso - Costo
        Porcentaje = Ganancia / Ingreso
        print ("El cliente es: ",nombre)
        print ("La edad del cliente es: ",edad)
        print ("El producto favorito es: ",productoF)
        print ("Premios ganados: ", Premio)
        print ("El valor de costo es: ", valorCosto,"$")
        print ("El valor de venta es: ", valorVenta,"$")
        print ("El procentaje de ganancia es: ", Porcentaje, "%")
    elif clientes > 1 and productos > 1:
        contador = 1
        while contador <= clientes and contador <= productos:
            nombre = str(input("Ingrese el nombre del cliente, por favor:\n"))
            edad = int(input("Ingrese la edad del cliente, por favor:\n"))
            productoF = str(input("Ingrese el producto favorito, por favor:\n"))
            campaÃ±a = int(input("Ingrese el nÃºmero de campaÃ±a, por favor:\n"))
            Premio = int(input("Â¿CuÃ¡ntos premios recibe por esta venta?\n"))
            producto = str(input("Diga el nombre del producto\n"))
            valorCosto = int(input("Ingrese el costo del producto\n"))
            valorVenta = int(input("Ingrese el valor de venta del producto\n"))
            contador = contador + 1
            edadSuma= edad + edad
            Edadprom = edadSuma / clientes
            TotalCosto = valorCosto + valorCosto
            TotalVenta = valorVenta + valorVenta
            Ingreso = productos * TotalVenta
            Costo = productos * TotalCosto
            Ganancia = Ingreso - Costo
            Porcentaje = Ganancia / Ingreso
            print ("Los clientes son: ",nombre)
            print ("El producto favorito es: ",productoF)
            print ("Premios ganados: ", Premio)
            print ("El valor total de costo es: ", TotalCosto,"$")
            print ("El valor total de venta es: ", TotalVenta,"$")
            print ("El procentaje de ganancia es: ", Porcentaje, "%")
        print ("La edad promedio es: ",Edadprom)
        print ("La cantidad de productos vendidos fue: ", productos)
    else:
        print ("Valor invÃ¡lido")

Venta(clientes, productos)
