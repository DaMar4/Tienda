from flask import render_template,Blueprint,flash,redirect,url_for,request
from flask_login import current_user
from ...model.frmSalidas import FrmSalidas
from ...model.DBSalidas import DBSalidas
from ...model.DBEmpleados import DBEmpleados
from ...model.DBProductos import DBProductos
from ...model.frm_edit_Salida import FrmEditSalida
from WebApp import db
salidas_bp = Blueprint("salidas_bp",__name__)
@salidas_bp.route('/salidas/',methods=['GET','POST'])
def salidas_add():
    frmSalidas = FrmSalidas(meta={'csrf': False})
    list_empleado = [(empleado.nombre_empleado,empleado.nombre_empleado)for empleado in DBEmpleados.query.all()]
    frmSalidas.empleado_que_recibe.choices = list_empleado
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBProductos.query.all()]
    frmSalidas.descripcion.choices = list_descripcion
    lista_salidas = DBSalidas.query.order_by(DBSalidas.id_salida)
    if frmSalidas.validate_on_submit():
        nueva_salida = DBSalidas(frmSalidas.empleado_que_recibe.data,frmSalidas.descripcion.data,frmSalidas.observacion.data,frmSalidas.cantidad.data,frmSalidas.fecha.data)
        db.session.add(nueva_salida)
        db.session.commit()
        flash("Salida completada Exitosamente!")
        return redirect(url_for('salidas_bp.salidas_add'))
    if frmSalidas.errors:
        flash(frmSalidas.errors, "danger")
    return render_template("salidas.html",salidas = lista_salidas,form = frmSalidas)
@salidas_bp.route('/editar-salida/<int:id>',methods=['GET','POST'])
def salida_edit(id):
    id_salida = DBSalidas.query.get_or_404(id)
    form_edit_salida = FrmEditSalida(meta={'csrf': False})
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBProductos.query.all()]
    form_edit_salida.descripcion.choices = list_descripcion
    form_edit_salida.cantidad.data = id_salida.cantidad
    if form_edit_salida.validate_on_submit():
        nuevo_dato = DBSalidas.query.filter(DBSalidas.id_salida == id).first()
        nuevo_dato.descripcion = request.form['descripcion']
        nuevo_dato.cantidad = request.form['cantidad']
        nuevo_dato.fecha = request.form['fecha']
        db.session.add(nuevo_dato)
        db.session.commit()
        flash("Salida Editada Exitosamente!")
        return redirect(url_for('salidas_bp.salidas_add'))
    if form_edit_salida.errors:
        flash(form_edit_salida.errors, "danger")
    return render_template("editar_salida.html",form = form_edit_salida, id_salida=id_salida)
@salidas_bp.route('/eliminar-salida/<int:id>',methods=['GET','POST'])
def salida_del(id):
    del_salida = DBSalidas.query.filter(DBSalidas.id_salida == id).first()
    db.session.delete(del_salida)
    db.session.commit()
    flash("Salida eliminada Exitosamente!")
    return redirect(url_for('salidas_bp.salidas_add'))