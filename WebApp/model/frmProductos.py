from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired
class FrmProductos(FlaskForm):
    descripcion = StringField("Descripción:",validators=[DataRequired()])
    unidad = StringField("Unidad:",validators=[DataRequired()])
    categoria = StringField("Categoría:",validators=[DataRequired()])