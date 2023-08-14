"""
De flask importamos el módulo Flask, también trabajaremos con archivos Json, por lo tanto también importamos 
el método jsonify, para poder recibir valores y mostrarlos, vamos a importar el método request.
"""
from flask import Flask, jsonify, request
from products import products #Importamos de products el método proucts.
app = Flask(__name__)

#----------------------------- READ PRODUCTS -----------------------------
#Se crea la ruta para nuestro servidor.
@app.route('/ping')#Va a tener un método GET.
def ping(): #Función para comprar el funcionamienro.
    return jsonify({"message": "pong!"}) #Se envía un objeto.


@app.route('/products')#Ruta productos, se mostrará la lista de productos.
def getProcucts():
    #Se envía un objeto, el cual, tiene la propiedad products, y su valor es
    #la lista de3 productos.
    return jsonify({"products": products, "message": "Product's List"}) 

#En caso de querer llamar un solo nombre de la lista de productos, creamos una nueva ruta al igual que una nueva función.
@app.route('/products/<string:product_name>')
def getProduct(product_name):
    #Recorre el método products, para encontrar el valor ingresado por los clientes,
    #por medio de un ciclo For.
    productsFound = [product for product in products if product['name'] == product_name]
    #Ahora creamos una condición, la cuál nos ayudará a definir si el valor ingresado el mayor a cero.
    #Se utilizará una función, Len, esta se encarga de darnos la lóngitud de un arreglo, en este caso nos dará
    #la lóngitud de la lista.
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]}) #En el caso de que el producto sea mayor a cero, nos retornará el primer valor que encuentre.
    return jsonify({"message": "Product no found."})#Si no encuentra nada, se retornará un mensaje avisando.)

#----------------------------- CREATE PRODUCTS -----------------------------

@app.route('/products', methods=['POST'])
def addProduct():
    #En la variable se agregan los productos ingresados y se guardan.
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)#Se agrega el nuevo producto a products.
    return jsonify({"message": "Product added succesfully.", "products": products})#Retorna mensaje de creación correcta y muestra los datos ingresados.
#----------------------------- UPDATE PRODUCTS -----------------------------

@app.route('/products/<string:product_name>', methods=['PUT']) #El método PUT, actualiza los objetos.
def editProduct(product_name):
    #Por medio de un bucle for, se recorre la lista buscando el objeto que será mófidicado.
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product updated succesfully.", 
            "product": productFound[0]
        })
    return jsonify({"message": "Product no found"})

#----------------------------- DELETE PRODUCTS -----------------------------

@app.route('/products/<string:product_name>', methods=['DELETE'])#El método DELETE, elimina un objeto.
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product delete.",
            "products": products
            })
    return jsonify({"message": "Product no found."})
    
#------------------ Se crea una condición, de que si el archivo se esta ejecutando como principal. ------------------
if __name__ == '__main__': 
    app.run(debug=True, port=4000)
