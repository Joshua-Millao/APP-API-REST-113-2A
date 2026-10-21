
#Nombre: Eric Railef Mansilla
#App- Python API REST

import requests


BASE_URL = "https://dummyjson.com/products"


def mostrar_resp(respuesta):
    # muestra codigo http y sus datos 
    print("Codigo HTTP", respuesta.status_code)

    if respuesta.text():
        print("Respuesta JSON")
        print(respuesta.json())

    else:
        print("La respuesat no tiene datos")
    
try:

    # ====================================================
    # 1. GET CONSULTAR UN PRODUCTO
    # ====================================================

    print("---- GET: CONSULTAR PRODUCTO ----")

    respuesta = requests.get(
        f"{BASE_URL}/0",
        timeout=10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto", producto["title"])
    print("Precio", producto["price"])
    print("Categoria", producto["category"])

    # ====================================================
    # 2. POST CREAR UN PRODUCTO
    # ====================================================


except requests.exceptions.Timeout:
    print("Error se agoto el tiempo de espera")
