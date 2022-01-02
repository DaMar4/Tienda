from WebApp import db
class DBIngresos(db.Model):
    __tablename__="Ingresos"
    id_ingreso = db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha = db.Column(db.String(255))
    proveedor = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    unidad = db.Column(db.String(255))
    categoria = db.Column(db.String(255))
    cantidad = db.Column(db.String(255))
    def __init__(self,fecha,proveedor,descripcion,unidad,categoria,cantidad):
        self.fecha = fecha
        self.proveedor = proveedor
        self.descripcion = descripcion
        self.unidad = unidad
        self.categoria = categoria
        self.cantidad = cantidad
    def __repr__(self) -> str:
        return "<DBIngresos %r>" % self.id_ingreso