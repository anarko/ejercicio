PRODUCTOS = {
    'super1':[
        {'id':1,'categoria':'categoria1','nombre': 'Producto 1','precio_compra':10,'precio_venta':13,'precio_mayorista':12},
        {'id':2,'categoria':'categoria2','nombre': 'Producto 2','precio_compra':20,'precio_venta':23,'precio_mayorista':22},
        {'id':3,'categoria':'categoria3','nombre': 'Producto 3','precio_compra':30,'precio_venta':33,'precio_mayorista':32},
        {'id':4,'categoria':'categoria4','nombre': 'Producto 4','precio_compra':40,'precio_venta':43,'precio_mayorista':42},
        {'id':5,'categoria':'categoria5','nombre': 'Producto 5','precio_compra':50,'precio_venta':53,'precio_mayorista':52},
    ],
    'super2':[
        {'id':1,'categoria':'categoria1','nombre': 'Producto 1','precio_compra':10,'precio_venta':13,'precio_mayorista':12},
        {'id':2,'categoria':'categoria2','nombre': 'Producto 2','precio_compra':20,'precio_venta':23,'precio_mayorista':22},
        {'id':3,'categoria':'categoria3','nombre': 'Producto 3','precio_compra':30,'precio_venta':33,'precio_mayorista':32},
        {'id':4,'categoria':'categoria4','nombre': 'Producto 4','precio_compra':40,'precio_venta':43,'precio_mayorista':42},
        {'id':5,'categoria':'categoria5','nombre': 'Producto 5','precio_compra':50,'precio_venta':53,'precio_mayorista':52},
    ],
    'super3':[
        {'id':1,'categoria':'categoria1','nombre': 'Producto 1','precio_compra':10,'precio_venta':13,'precio_mayorista':12},
        {'id':2,'categoria':'categoria2','nombre': 'Producto 2','precio_compra':20,'precio_venta':23,'precio_mayorista':22},
        {'id':3,'categoria':'categoria3','nombre': 'Producto 3','precio_compra':30,'precio_venta':33,'precio_mayorista':32},
        {'id':4,'categoria':'categoria4','nombre': 'Producto 4','precio_compra':40,'precio_venta':43,'precio_mayorista':42},
        {'id':5,'categoria':'categoria5','nombre': 'Producto 5','precio_compra':50,'precio_venta':53,'precio_mayorista':52},
    ]
}

class data_productos:
   
    def get_producto(self,id_super,index,valor):
        ''' Busca un producto en base a los datos indicados y lo devuelve 
            trata todos los valores como string ( para bsucar por precios o id )
        '''
        if id_super not in PRODUCTOS: 
            return None
        for p in PRODUCTOS[id_super]:
            if index in p.keys():                
                
                if str(p[index]) == valor:
                    return p
        return None