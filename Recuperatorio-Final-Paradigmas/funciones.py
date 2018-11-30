import csv

def salesData():
    limitCode = 6
    maxFields = 5
    saleData = []
    fila = 1

    try:
        with open('archivo.csv') as file:
            file_csv = csv.reader(file)
            data = next(file_csv, None)
            while data:
                saleData.append(data)
                data = next(file_csv, None)

            positionAmount = saleData[0].index('CANTIDAD')
            positionPrice = saleData[0].index('PRECIO')
            positionCode = saleData[0].index('CODIGO')
            

            for line in saleData[1:]:
                cont = 0
                validationFloat = line[positionPrice].count('.')
                validationInt = line[positionAmount].count('.')

                #Validacion en caso de que haya mas o menos campos en el archivo csv
                if len(line) != maxFields:
                    saleData = [[f"El archivo csv no contiene todos los campos en la fila {fila}."]]
                    break
                #Validacion en caos de que haya numeros enteros en la columna PRECIO
                if validationFloat == 0:
                    saleData = [[f"El archivo csv no puede contener numeros enteros en la columna PRECIO en la Fila: {fila} "]]
                    break
                #validaicon en caso de que haya numeros flotantes en la columna CANTIDAD
                if validationInt ==  1:
                    saleData = [[f"El archivo csv no puede contener numeros enteros en la columna PRECIO en la fila {fila}."]]
                    break
                #validacion en codigo.
                while cont < len(line[positionCode]):
                    if cont >= limitCode:
                        saleData = [[f'El archivo csv no puede conterner mas de 6 caracteres los campos de la columna CODIGO en la fila {fila}.']]
                        break
                    elif len(line[positionCode]) < limitCode:
                        saleData = [[f'El archivo csv no puede conterner menos de 6 caracteres los campos de la columna CODIGO en la fila {fila}.']]
                        break
                    elif cont < 3:
                        if line[positionCode][cont].isdigit():
                            saleData = [[f'El archivo csv no puede conterner en los primeros 3 caracteres numeros en la fila {fila}.']]
                            break
                    elif cont >=  3 and cont < limitCode:
                        if line[positionCode][cont].isalpha():
                            saleData = [[f'El archivo csv no puede conterner en los ultimos 3 caracteres letras en la fila {fila}.']]
                            break
                    cont+=1
    except:
        saleData = [['El archivo csv no existe.']]
    return saleData

#Retorna una lista del dato consultado (CLIENTE) por el usuario en caso de que se encuentre en la lista de ventas.
def consultedDataClient(data, table):
    newList = []
    positionClient = table[0].index('CLIENTE')

    for line in table[1:]:
        if data in line[positionClient] and line[positionClient] not in newList:
            newList.append(line[positionClient])
    return newList

#Retorna una lista del dato consultado (PRODUCTO) por el usuario en caso de que se encuentre en la lista de ventas.
def consultedDataProduct(data, table):
    newList = []
    positionProduct = table[0].index('PRODUCTO')

    for line in table[1:]:
        if data in line[positionProduct] and line[positionProduct] not in newList:
            newList.append(line[positionProduct])
    return newList

#Retorna una lista del dato consultado con su informacion completa que se encuentra en la lista de ventas
def completeTable(data, saleData):
    rowShow = []

    for title in saleData[:1]:
        rowShow.append(title)

    for line in saleData[1:]:
        for dato in line:
            if dato == data:
                rowShow.append(line)

    return rowShow

#Esta funcion nos permite ver los productos mas vendidos
def productosMasVendidos(salesData):
    listProducts = []
    table = []
    positionPrice = salesData[0].index('PRODUCTO')
    positionAmount = salesData[0].index('CANTIDAD')

    #Recorre la lista para obtener los titulos requeridos.
    for line in salesData[1:]:
        if line[positionPrice] not in listProducts:
            listProducts.append(line[positionPrice])
    
    #Recorre la lista sumando los productos repetidos en caso de haberlos.
    for product in listProducts:
        amount = 0
        for line in salesData[1:]:
            if line[positionPrice] == product:
                amount = amount + int(line[positionAmount])
            newList = [product, amount]
        table.append(newList)
    return table

#Función que retorna una lista de los mejores clientes.
def clientesQueMasCompraron(salesData):
    listClients = []
    table = []
    positionClient = salesData[0].index('CLIENTE')
    positionAmount = salesData[0].index('PRECIO')

    #Recorre la lista para obtener los titulos requeridos.
    for line in salesData[1:]:
        if line[positionClient] not in listClients:
            listClients.append(line[positionClient])

    #Recorre la lista sumando los montos gastados por los clientes que salgan mas de una vez.
    for cliente in listClients:
        price = 0
        for line in salesData[1:]:
            if line[positionClient] == cliente:
                price = price + float(line[positionAmount])
            newList = [cliente, round(price, 2)]
        table.append(newList)
    return table

#Función que ordena de mayor a menor la lista.
def ordenarTablaDescendente(tabla, column1, column2):
    list = []
    orderList = []
    showTable = [[column1, column2]]
    posicion = showTable[0].index(column2)

    #Recorre la que se desea ordenar
    for line in tabla:
        list.append(line[posicion])
    
    list.sort() #Sort nos ordena la lista de manera descendente.
    for i in reversed(list):
        orderList.append(i)
    
    #Recorre y ordena la lista.
    for i in orderList:
        for line in tabla:
            for data in line:
                if data == i:
                    showTable.append(line)
    return showTable