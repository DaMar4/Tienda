from flask import render_template, redirect, session, url_for, flash, get_flashed_messages,request
from flask.blueprints import Blueprint
from flask_login import login_user, logout_user, current_user,login_required
from WebApp import login_manager
from WebApp.model.inicio import Iniciar, Usuario, Registrar, db
from WebApp.model.frmPerfil import FrmPerfil
from WebApp import db
registrar_bp = Blueprint("registrar_bp", __name__)
@registrar_bp.route("/registrar", methods=['GET', 'POST'])
def register():
    form = Registrar(meta={"csrf": False})
    if form.validate_on_submit():
        if Usuario.query.filter_by(username=form.Usuario.data).first():
            flash("El usuario ya se encuentra registrado")
        else:
            # Registrar
            nuevo_usuario = Usuario(form.nombre_completo.data,form.Usuario.data, form.contrasena.data,form.tipo_de_cuenta.data)
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash("Usuario registrado exitosamente")
            return redirect(url_for("registrar_bp.register"))
    if form.errors:
        flash("error")
    return render_template("register.html", form=form)
@registrar_bp.route('/lista-usuarios')
def user_list():
    lista_user = Usuario.query.all()
    return render_template("lista_user.html",usuarios=lista_user)
@registrar_bp.route('/eliminar-usuario/<int:id>')
def usuario_delete(id):
    del_usuario = Usuario.query.filter(Usuario.id == id).first()
    db.session.delete(del_usuario)
    db.session.commit()
    flash("Usuario eliminado Exitosamente!")
    return redirect(url_for('registrar_bp.user_list'))
@registrar_bp.route('/editar-perfil',methods=['GET','POST'])
def perfil_edit():
    frmPerfil = FrmPerfil(meta={"csrf": False})
    frmPerfil.nombre_completo.data = current_user.fullname
    if frmPerfil.validate_on_submit():
        usuario_nuevo_dato = Usuario.query.filter(Usuario.id == current_user.id)
        usuario_nuevo_dato.fullname = frmPerfil.nombre_completo.data
        usuario_nuevo_dato.pwhash = Usuario.check_password(frmPerfil.contrasena.data)
        db.session.add(usuario_nuevo_dato)
        db.session.commit()
        flash("Perfil moidificado exitosamente")
        return redirect(url_for("registrar_bp.perfil_edit"))
    return render_template("perfil.html", form = frmPerfil)