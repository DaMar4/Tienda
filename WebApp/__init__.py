from flask import Flask,redirect,url_for,flash,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user,logout_user
from functools import wraps
app = Flask(__name__)

app.config.from_object("configuration.DevelopmentConfig")

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "blue_login.login"
login_manager.login_message=""
def admin_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if(current_user.rol.value==1):
            return render_template("denied_acces.html")
        return f(*args, **kwds)
    return wrapper

from WebApp.modules.iniciar.login_user import blue_login
from WebApp.modules.home.index import index
from WebApp.modules.home.CRUD import crud
from WebApp.modules.home.ingresos import ingresos_bp
from WebApp.modules.home.productos import productos_bp
from WebApp.modules.home.proveedores import proveedores_bp
from WebApp.modules.home.salidas import salidas_bp
from WebApp.modules.home.empleados import empleados_bp
from WebApp.modules.home.registro import registrar_bp
from WebApp.modules.home.inventario import inventario_bp

app.register_blueprint(index)
app.register_blueprint(blue_login)
app.register_blueprint(crud)
app.register_blueprint(ingresos_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(proveedores_bp)
app.register_blueprint(salidas_bp)
app.register_blueprint(empleados_bp)
app.register_blueprint(registrar_bp)
app.register_blueprint(inventario_bp)
db.create_all()
