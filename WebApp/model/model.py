from flask_wtf import FlaskForm
from wtforms import StringField, DateField,SelectField,HiddenField
from wtforms.validators import DataRequired, InputRequired
from WebApp import db
class StockTienda(db.Model):
    __tablename__='entradas'
    id_producto = db.Column(db.BigInteger,primary_key=True,autoincrement=True)
    descripcion = db.Column(db.String(255))
    tipos = db.Column(db.String(255))
    categoria = db.Column(db.String(255))
    almacen = db.Column(db.String(255))
    cantidad = db.Column(db.String(255))
    fecha = db.Column(db.String(255))
    registrado_por=db.Column(db.String(255))
    def __init__(self,descripcion,tipos,categoria,almacen,cantidad,fecha,registrado_por):
        self.descripcion = descripcion
        self.tipos = tipos
        self.categoria = categoria
        self.almacen = almacen
        self.cantidad = cantidad
        self.fecha = fecha
        self.registrado_por = registrado_por
    def __repr__(self):
        return '<StockTienda %r>' % self.nombre_producto
class ProductForm(FlaskForm):
    descripcion = StringField("Descripcion:",validators=[InputRequired()])
    tipos = SelectField("Tipos:",validators=[InputRequired()],choices=[('Paquete', 'Paquete'), ('Pieza', 'Pieza'),('Rollo','Rollo'),('Litro','Litro'),('Metro','Metro'),('Caja','Caja'),('Kilogramo','Kilogramo'),('Garrafon','Garrafon'),('Galon','Galon')],coerce=str)
    categoria  = StringField("Categoria:",validators=[InputRequired()])
    proveedor = SelectField("Proveedor:",validators=[InputRequired()],choices=[('gobierno', 'gobierno'), ('donación', 'donación')],coerce=str)
    cantidad = StringField("Cantidad:",validators=[InputRequired()])
    fecha_registro = DateField("Fecha de entrada:", validators=[DataRequired()], format='%Y-%m-%d')
    registrado_por = HiddenField()
class FrmProductos(FlaskForm):
    descripcion = StringField("Descripcion:",validators=[InputRequired()])
    tipos = SelectField("Tipos:",validators=[InputRequired()],choices=[('Paquete', 'Paquete'), ('Pieza', 'Pieza'),('Rollo','Rollo'),('Litro','Litro'),('Metro','Metro'),('Caja','Caja'),('Kilogramo','Kilogramo'),('Garrafon','Garrafon'),('Galon','Galon')],coerce=str)
    categoria  = StringField("Categoria:",validators=[InputRequired()])


