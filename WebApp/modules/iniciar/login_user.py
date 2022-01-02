from flask import render_template, redirect, session, url_for, flash, get_flashed_messages,request
from flask.blueprints import Blueprint
from flask_login import login_user, logout_user, current_user,login_required
from WebApp import login_manager
from WebApp.model.inicio import Iniciar, Usuario
from WebApp import db
blue_login = Blueprint("blue_login", __name__)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

@blue_login.route("/iniciar", methods=['GET', 'POST'])
def login():
    if not Usuario.query.filter_by(username="usuario1").first():
        nuevo_usuario = Usuario("default","usuario1","123",6)
        db.session.add(nuevo_usuario)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for("index.main_page"))
    form = Iniciar(meta={"csrf": False})
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(username=form.Usuario.data).first()
        if usuario and usuario.check_password(form.contrasena.data):
            login_user(usuario)
            flash("Bienvenido "+str(usuario.fullname))
            next = request.form["next"]
            return redirect(next or url_for("index.main_page"))
        else:
            flash("El usuario y/o la contraseña es incorrecta")
    if form.errors:
        flash("El usuario no se encuentra registrado", "Error de formulario")
    return render_template("login.html", form=form)

@blue_login.route("/cerrar")
def closed():
    logout_user()
    return redirect(url_for("blue_login.login"))