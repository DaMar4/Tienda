from WebApp import db
class DBEmpleados(db.Model):
    __tablename__="empleados"
    id_empleado = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre_empleado = db.Column(db.String(255))
    area = db.Column(db.String(255))
    def __init__(self,nombre_del_empleado,area):
        self.nombre_empleado = nombre_del_empleado
        self.area = area
    def __repr__(self):
        return "<DBEmpleados %r>" % self.nombre_empleado