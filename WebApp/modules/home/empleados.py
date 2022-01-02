from re import template
from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmEmpleados import FrmEmpleados
from ...model.DBEmpleados import DBEmpleados
from WebApp import db
empleados_bp = Blueprint("empleados_bp",__name__)
@empleados_bp.route('/empleados/',methods=['GET','POST'])
def empleados_add():
    frmEmpleados = FrmEmpleados(meta={'csrf': False})
    lista_empleados = DBEmpleados.query.order_by(DBEmpleados.id_empleado)
    if frmEmpleados.validate_on_submit():
        nuevo_empleado = DBEmpleados(frmEmpleados.nombre_empleado.data,frmEmpleados.area.data)
        db.session.add(nuevo_empleado)
        db.session.commit()
        flash("Empleado Registrado Exitosamente!")
        return redirect(url_for('empleados_bp.empleados_add'))
    if frmEmpleados.errors:
        flash(frmEmpleados.errors, "danger")
    return render_template("empleados.html",empleados = lista_empleados,form = frmEmpleados)
@empleados_bp.route('/editar-empleado/<int:id>',methods=['GET','POST'])
def empleado_edit(id):
    frmEmpleados = FrmEmpleados(meta={'csrf': False})
    empleados=DBEmpleados.query.get_or_404(id)
    frmEmpleados.nombre_empleado.data = empleados.nombre_empleado
    frmEmpleados.area.data = empleados.area
    if frmEmpleados.validate_on_submit():
        nuevos_datos = DBEmpleados.query.filter(DBEmpleados.id_empleado==id).first()
        nuevos_datos.nombre_empleado = request.form['nombre_empleado']
        nuevos_datos.area = request.form['area']
        db.session.add(nuevos_datos)
        db.session.commit()
        flash("Empleado Editado Exitosamente")
        return redirect(url_for("empleados_bp.empleados_add"))
    if frmEmpleados.errors:
        flash(frmEmpleados.errors, "danger")
    return render_template("editar_empleado.html",empleados=empleados,form = frmEmpleados)
@empleados_bp.route('/eliminar-empleado/<int:id>')
def eliminar(id):
    empleado_eliminar = DBEmpleados.query.filter(DBEmpleados.id_empleado==id).first()
    db.session.delete(empleado_eliminar)
    db.session.commit()
    flash("Empleado Eliminado Exitosamente!")
    return redirect(url_for("empleados_bp.empleados_add"))