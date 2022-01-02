from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, PasswordField,HiddenField,SelectField
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms.validators import EqualTo, InputRequired
from WebApp import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    pwhash = db.Column(db.String(255))
    rol = db.Column(db.Integer)

    def __init__(self,fullname, username, pwhash, rol=1):
        self.fullname = fullname
        self.username = username
        self.pwhash = generate_password_hash(pwhash)
        self.rol = rol

    def __repr__(self):
        return "<Usuario %r>" % (self.username)

    def get_id(self):
        return str(self.id)

    def check_password(self, password):
        return check_password_hash(self.pwhash, password)

    @property
    def is_authenticated(self):
        """The foo property."""
        return True

    @property
    def is_active(self):
        """The foo property."""
        return True

    @property
    def is_anonymous(self):
        """The foo property."""
        return False
class Iniciar(FlaskForm):
    Usuario = StringField("Usuario:", validators=[InputRequired()])
    contrasena = PasswordField("Contraseña:", validators=[InputRequired()])
    next = HiddenField("next")
class Registrar(FlaskForm):
    tipo_de_cuenta = SelectField(u'Tipo de cuenta', choices=[('1', 'Regular'), ('6', 'Administrador')],validators=[InputRequired()])
    nombre_completo = StringField("Nombre completo:", validators=[InputRequired()])
    Usuario = StringField("Usuario:", validators=[InputRequired()])
    contrasena = PasswordField("Contraseña:", validators=[InputRequired(), EqualTo('confirmar_contrasena')])
    confirmar_contrasena = PasswordField('Confirmar contraseña:', validators=[InputRequired()])
