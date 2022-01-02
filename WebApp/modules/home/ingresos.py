from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmIngresos import FrmIngresos
from ...model.frm_edit_Ingreso import FrmIngresos_edit
from datetime import datetime
from ...model.DBIngresos import DBIngresos
from ...model.DBProductos import DBProductos
from WebApp import db
ingresos_bp = Blueprint("ingresos_bp",__name__)
@ingresos_bp.route('/ingresos/',methods=['GET','POST'])
def ingreso_add():
    frmIngresos = FrmIngresos(meta={'csrf': False})
    lista_ingresos = DBIngresos.query.order_by(DBIngresos.id_ingreso)
    list_descripcion = [(des.descripcion,des.descripcion)for des in DBProductos.query.all()]
    list_unidad = [(des.unidad,des.unidad)for des in DBProductos.query.all()]
    list_categoria = [(des.categoria,des.categoria)for des in DBProductos.query.all()]
    frmIngresos.descripcion.choices = list_descripcion
    frmIngresos.unidad.choices = list_unidad
    frmIngresos.categoria.choices = list_categoria
    if frmIngresos.validate_on_submit():
        nuevo_ingreso = DBIngresos(frmIngresos.fecha.data,frmIngresos.proveedor.data,frmIngresos.descripcion.data,frmIngresos.unidad.data,frmIngresos.categoria.data,frmIngresos.cantidad.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Nuevo Ingreso Registrado Exitosamente!")
        return redirect(url_for('ingresos_bp.ingreso_add'))
    if frmIngresos.errors:
        flash(frmIngresos.errors, "danger")
    return render_template("ingresos.html",ingresos = lista_ingresos,form = frmIngresos)
@ingresos_bp.route('/editar-ingreso/<int:id>',methods=['GET','POST'])
def editar_ingreso(id):
    frmIngresos = FrmIngresos_edit(meta={'csrf': False})
    ingreso = DBIngresos.query.get_or_404(id)
    fecha = ingreso.fecha
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    frmIngresos.fecha.data = fecha_dt
    frmIngresos.proveedor.data = ingreso.proveedor
    frmIngresos.descripcion.data = ingreso.descripcion
    frmIngresos.unidad.data = ingreso.unidad
    frmIngresos.categoria.data = ingreso.categoria
    frmIngresos.cantidad.data = ingreso.cantidad
    if frmIngresos.validate_on_submit():
        nuevos_datos = DBIngresos.query.filter(DBIngresos.id_ingreso==id).first()
        nuevos_datos.fecha = request.form['fecha']
        nuevos_datos.proveedor = request.form['proveedor']
        nuevos_datos.descripcion = request.form['descripcion']
        nuevos_datos.unidad = request.form['unidad']
        nuevos_datos.categoria = request.form['categoria']
        nuevos_datos.cantidad = request.form['cantidad']
        db.session.add(nuevos_datos)
        db.session.commit()
        flash("Ingreso Editado Exitosamente")
        return redirect(url_for("ingresos_bp.ingreso_add"))
    if frmIngresos.errors:
        flash(frmIngresos.errors, "danger")
    return render_template("editar_ingreso.html",form = frmIngresos)
@ingresos_bp.route('/eliminar-ingreso/<int:id>')
def eliminar(id):
    ingreso_eliminar =DBIngresos.query.filter(DBIngresos.id_ingreso==id).first()
    db.session.delete(ingreso_eliminar)
    db.session.commit()
    flash("Ingreso Eliminado Exitosamente!")
    return redirect(url_for("ingresos_bp.ingreso_add"))