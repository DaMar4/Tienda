from flask_wtf import FlaskForm
from wtforms import StringField,DateField,SelectField
from wtforms.validators import DataRequired
class FrmIngresos_edit(FlaskForm):
    fecha = DateField("Fecha:", validators=[DataRequired()], format='%Y-%m-%d')
    proveedor = StringField("Proveedor:",validators=[DataRequired()],render_kw={'readonly': True})
    descripcion = StringField("Descripción:",validators=[DataRequired()],render_kw={'readonly': True})
    unidad = StringField("Unidad:",validators=[DataRequired()],render_kw={'readonly': True})
    categoria = StringField("Categoría:",validators=[DataRequired()],render_kw={'readonly': True})
    cantidad = StringField("Cantidad:",validators=[DataRequired()])