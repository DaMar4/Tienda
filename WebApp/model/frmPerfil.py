from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, PasswordField,HiddenField,SelectField
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms.validators import EqualTo, InputRequired
class FrmPerfil(FlaskForm):
    nombre_completo = StringField("Nombre completo:", validators=[InputRequired()])
    contrasena = PasswordField("Contraseña:", validators=[InputRequired(), EqualTo('confirmar_contrasena')])
    confirmar_contrasena = PasswordField('Confirmar contraseña:', validators=[InputRequired()])