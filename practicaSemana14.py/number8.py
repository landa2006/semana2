def buscar_producto(productos, buscar):
    for producto in productos:
        if producto.lower() == buscar.lower():
            return True
    return False


productos = ["Laptop", "Mouse", "Teclado", "Monitor", "USB"]

buscar = input("Ingrese producto a buscar: ")

if buscar_producto(productos, buscar):
    print("Producto encontrado")
else:
    print("Producto no encontrado")
