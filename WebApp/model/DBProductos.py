from WebApp import db
class DBProductos(db.Model):
    __tablename__="productos"
    id_producto = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descripcion = db.Column(db.String(255))
    unidad = db.Column(db.String(255))
    categoria = db.Column(db.String(255))
    def __init__(self,descripcion,unidad,categoria):
        self.descripcion = descripcion
        self.unidad = unidad
        self.categoria = categoria
    def __repr__(self) -> str:
        return "<DBProductos %r>" % self.descripcion