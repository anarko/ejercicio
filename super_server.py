from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from data_model import data_productos

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id_super')
parser.add_argument('index_busqueda')
parser.add_argument('valor')

class SupermercadoBuscarProducto(Resource):
    
    def __init__(self):
        # Instanciamos el modelo de datos para poder traer la informacion
        self.data_prod = data_productos()
    
    def get(self,id_super,index_busqueda,valor): 
        ''' devulve JSON del producto buscado o error en caso de no encontrarlo '''

        p = self.data_prod.get_producto(id_super,index_busqueda,valor) 
        if p: return p        
        else: return "{'error':'producto o supermercado no encontrado'}",404

api.add_resource(SupermercadoBuscarProducto, '/productos/buscar/<string:id_super>/<string:index_busqueda>/<string:valor>')

if __name__ == '__main__':
    app.run(debug=True)