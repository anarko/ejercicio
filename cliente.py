from requests import put, get

IP_SERVER = "localhost"
PUERTO = "5000"

class Cliente:
    #los productos son almacenados en una lista de diccionarios
    productos_consultados = []

    def __init__(self,cual_super):
        #decidimos a cual supermercado le vamos a pedir informacion
        self.cual_super = cual_super

    def pedir_producto_super(self,index_busq,dato_busq):

        req = get('http://'+IP_SERVER+':'+PUERTO+'/productos/buscar/'+self.cual_super+'/'+index_busq+'/'+dato_busq)
        if req.status_code == 200:
            self.productos_consultados.append(req.json())
        elif req.status_code == 404:
            raise RuntimeError("No se han encontrado los datos") 

    def get_productos_consultados(self):
        return self.productos_consultados

if __name__ == "__main__":

    # me subscribo al super1 para pedir los datos
    c1 = Cliente('super1')
    c1.pedir_producto_super('categoria','categoria1')
    c1.pedir_producto_super('id','3')
    c1.pedir_producto_super('nombre','Producto 1')
    try:
        c1.pedir_producto_super('precio_venta','2')
    except:
        print("Producto no encontrado")
    
    print ( c1.get_productos_consultados() )
    