¿Cómo se usa el programa?
Como se utiliza el programa: Una vez entremos al sitio estaremos parados en la pantalla de inicio, desde ahí tendremos acceso a la barra de navegación, en la cual vamos a poder adentrarnos en las diferentes utilidades: 1- En la barra de navegación encontramos “Lista Completa”, en la que podremos ver todas las compras realizadas y cada uno de los clientes. 2- Luego tendremos la utilidad “Productos por Cliente” en la que podremos buscar el nombre de un cliente (Con solo ingresar 3 letras nos dará a elegir nombres que posean las mismas o podremos ingresar el nombre completo si a si se deseara), y esto nos permitirá ver todas las compras que realizo el cliente. 3- Seguido podremos ver la solapa de “Clientes por Producto”, nos permite elegir determinado producto y nos dirá que clientes lo han comprado. 4- Luego podremos ver “Productos más Vendidos”, mostrará un top de productos que sean los que tengan la mayor cantidad de compras. 5- Y la última solapa nos muestra a los “Mejores Clientes”, brindándonos una informe de los productos que compro y la cantidad total gastada.

Archivo CSV: Para leer este archivo se creó una función, llamada “AskTable” que recorre el archivo, lo mete en una string y lo presenta en forma una matriz.

Las Funciones y clases son:
¿Por qué?

salesData 
Esta función es la que utilizamos para leer el archivo.csv.

consultedDataProduct 
Al ingresar un producto devuelve la tabla del mismo.

consultedDataClient
Al ingresar un cliente devuelve la tabla del mismo.

completeTable 
Se muestra por completo la tabla y todo su contenido.

orderTable 
Ordena los datos ingresados en la tabla en base a producto y cantidad (de mayor a menor.

productosMasVendidos 
Nos informa los productos más vendidos

ordenarTablaDescendente 
Ordena de mayor a menor.

clientesQueMasCompraron
 Muestra los mejores clientes.



¿Qué estructura se utilizará para representar la información del archivo?
Se creó un array para contener el archivo.csv, luego para recorrerlo se creó la función salesList, que recorre cada una de las líneas (listas dentro del array) para buscar datos luego de ingresarlos en el cuadro de búsqueda y presionando el botón de Submit, además presentamos que la estructura para representar la información sea como una tabla, con un espacio de 4 lugares distintos para que el usuario esté al tanto de las diferentes formas en la que se puede consultar.


