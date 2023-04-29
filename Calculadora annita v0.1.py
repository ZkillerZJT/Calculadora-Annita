import sys
import io
import os
import time
import datetime
import csv
objetos=[]
class Producto:
    def __init__(self, Id, nombre_producto, alto, ancho, precio_unit, tipo):
        self.Id = Id
        self.nombre_Producto = nombre_producto
        self.alto = alto
        self.ancho = ancho
        self.precio_unit = precio_unit
        self.tipo = tipo
        
def ajustar_precio(altoP1, anchoP1, altoP2, anchoP2, precio_unitario_P1):
    area_P1 = altoP1 * anchoP1
    area_P2 = altoP2 * anchoP2
    multiplicador_precio_para_P2 = area_P1 / area_P2
    precio_unitario_P2 = precio_unitario_P1*multiplicador_precio_para_P2
    return precio_unitario_P2

def obtener_productos(): #sub funcion
    # Leer el archivo productos.csv y guarda la información en una lista de diccionarios
    with open("productos.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        productos = [row for row in lector]
        print(f"productos es: {productos}")
    return productos

def obtener_id_mas_grande(productos): #sub funcion
    # Iterar sobre la lista de diccionarios para encontrar el ID más grande
    ids = [int(p["Id"]) for p in productos]
    if ids==[]:
        ids=[1]
        print(f"se supone que ids ahora es 1: {max(ids)}")
        return max(ids)
    else:
        print(f"vamo a conseguir max ids {max(ids)} y ids es {ids}")
        return max(ids)

def crear_nuevo_producto(nombre_producto, alto, ancho, precio_unit, tipo): #entregar input_user como datos.
    # Obtener la lista de productos y el ID más grande
    productos = obtener_productos()
    id_mas_grande = obtener_id_mas_grande(productos)
    print(f"el id del producto a crear es:{id_mas_grande}")
    nuevo_producto = Producto(id_mas_grande+1, nombre_producto, alto, ancho, precio_unit, tipo)
   # id_counter+=1
    
    # nuevo_producto.Id = id_mas_grande + 1  # Asignar el siguiente número después del ID más grande encontrado
    # Agregar el nuevo producto a la lista de productos y guardarla en el archivo productos.csv
    productos.append(nuevo_producto.__dict__)
    with open("productos.csv", "w", newline="") as file:
        fieldnames = ["Id", "nombre_Producto", "alto", "ancho", "precio_unit", "tipo"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(productos)#con un listado de objetos, esto funcionará correctamente. todavia no.
    return nuevo_producto
""" Versión arcaica de escribir en csv.
def archivoproductos(){ 
    open("productos.csv", "a")
        print("Agregar producto")
        nombre_producto = input("Indique nombre del producto: ")
        alto = input("Indique alto del producto: ")
        ancho = input("Indique ancho del producto: ")
        precio_unitario = input("Indique precio unitario del producto: ")
        tipo = input("Indique tipo del producto(Sticker,Foto,Agenda,Carnet,etc): ")
        id = # por definir, deberia consultar id más grande actualmente, y hacer id++.
        f.write(nombre_producto + "," + alto + "," + ancho + "," + precio_unitario + "," + tipo + "," + id + "\n")
        f.close()
        mi_producto = Producto(nombre_producto, alto, ancho, precio_unitario, tipo, id)
}
"""
def inputToObject(): #ESTA FUNCION SE REPITE, REVISAR CICLO LOGICO
    print("Agregar producto")
    nombre_producto = input("Indique nombre del producto: ")
    alto = input("Indique alto del producto: ")
    ancho = input("Indique ancho del producto: ")
    precio_unit = input("Indique precio unitario del producto: ")
    tipo = input("Indique tipo del producto(Sticker,Foto,Agenda,Carnet,etc): ")
    nuevo_producto=crear_nuevo_producto(nombre_producto, alto, ancho, precio_unit, tipo)
    # nuevo_producto debe ser creado iterativamente, subiendo de numero.
    return nuevo_producto

def aplicar_descuento(precio_unitario, cantidad_producto):
    if cantidad_producto <= 10:
        precio_con_descuento = precio_unitario * 1 * cantidad_producto
    elif cantidad_producto <= 19:  #si no se cumple lo anterior, se comple esto. asi para todos los siguientes elif.
        precio_con_descuento = precio_unitario * 0.985 * cantidad_producto
    elif cantidad_producto <= 29:
        precio_con_descuento = precio_unitario * 0.97 * cantidad_producto
    elif cantidad_producto <= 39:
        precio_con_descuento = precio_unitario * 0.955 * cantidad_producto
    elif cantidad_producto <= 49:
        precio_con_descuento = precio_unitario * 0.94 * cantidad_producto
    elif cantidad_producto <= 59:
        precio_con_descuento = precio_unitario * 0.925 * cantidad_producto
    elif cantidad_producto <= 69:
        precio_con_descuento = precio_unitario * 0.91 * cantidad_producto
    elif cantidad_producto <= 79:
        precio_con_descuento = precio_unitario * 0.895 * cantidad_producto
    elif cantidad_producto <= 89:
        precio_con_descuento = precio_unitario * 0.88 * cantidad_producto
    elif cantidad_producto <= 99:
        precio_con_descuento = precio_unitario * 0.865 * cantidad_producto
    else:
        precio_con_descuento = precio_unitario * 0.85
        return precio_con_descuento
    print("Precio con descuento:", precio_con_descuento)
def interfaz():
    print("    |   Bienvenida Annita a tu asistente.                 |")
    print("    |            1 para agregar un producto.              |")
    print("    |            2 para modificar/eliminar producto.      |")
    print("    |            3 para consultar precio mayorista.       |")
    print("    |            4 menú inventario materia prima.         |")
    print("    |            7 Cerrar programa                        |")
    print("    |        (Digite un numero, y presione enter)         |")
    print("    |_____________________________________________________|")
    opcion = input()
    opcion = int(opcion)
    if opcion == 1:
        opcion=None
        inputToObject()
        producto_creado=inputToObject()
        print(producto_creado.nombre_Producto)
    elif opcion == 2:
        opcion=None
        print("Modificar/Eliminar producto")
    elif opcion == 3:
        opcion=None
        print("Consultar precio mayorista")
    elif opcion == 4:
        opcion=None
        print("Menú inventario materia prima.")
    elif opcion == 7:
        opcion=None
        exit(0)
    else:
        opcion=None
        print("Digite un numero valido")
        interfaz()

def main():
    """input_cantidad = input("Indique cantidad de producto: ")
input_preciounit = input("Indique precio unitario de producto: ")
    precio_con_descuento_main = calcular_descuento(precio_unitario, cantidad_producto)"""
    interfaz()
    

if __name__ == '__main__':
    main()
