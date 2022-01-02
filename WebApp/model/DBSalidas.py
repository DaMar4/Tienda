from WebApp import db
class DBSalidas(db.Model):
    __tablename__="salidas"
    id_salida = db.Column(db.Integer,primary_key=True,autoincrement=True)
    empleado_que_recibe = db.Column(db.String(255))
    descripcion =db.Column(db.String(255))
    observacion=db.Column(db.String(255))
    cantidad=db.Column(db.String(255))
    fecha=db.Column(db.String(255))
    def __init__(self,empleado_que_recibe,descripcion, observacion,cantidad,fecha):
        self.empleado_que_recibe = empleado_que_recibe
        self.descripcion = descripcion
        self.observacion = observacion
        self.cantidad = cantidad
        self.fecha = fecha
    def __repr__(self) -> str:
        return "<DBSalidas %r>" % self.descripcion