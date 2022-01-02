from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmProductos import FrmProductos
from ...model.DBProductos import DBProductos
from WebApp import db
productos_bp = Blueprint("productos_bp",__name__)
@productos_bp.route('/productos/',methods=['GET','POST'])
def productos_add():
    frmProductos = FrmProductos(meta={'csrf': False})
    productos = DBProductos.query.order_by(DBProductos.id_producto)
    if frmProductos.validate_on_submit():
        nuevo_ingreso = DBProductos(frmProductos.descripcion.data,frmProductos.unidad.data,frmProductos.categoria.data)
        db.session.add(nuevo_ingreso)
        db.session.commit()
        flash("Producto Agregado Exitosamente!")
        return redirect(url_for('productos_bp.productos_add'))
    if frmProductos.errors:
        flash(frmProductos.errors, "danger")
    return render_template("productos.html",form = frmProductos,productos=productos)
@productos_bp.route('/editar-producto/<int:id>',methods=['GET','POST'])
def producto_edit(id):
    frmProductos = FrmProductos(meta={'csrf': False})
    productos = DBProductos.query.get_or_404(id)
    frmProductos.descripcion.data = productos.descripcion
    frmProductos.unidad.data = productos.unidad
    frmProductos.categoria.data = productos.categoria
    if frmProductos.validate_on_submit():
        p_edit = DBProductos.query.filter(DBProductos.id_producto == id).first()
        p_edit.descripcion = request.form['descripcion']
        p_edit.unidad = request.form['unidad']
        p_edit.categoria = request.form['categoria']
        db.session.add(p_edit)
        db.session.commit()
        flash("Catalogo Editado Exitosamente!")
        return redirect(url_for('productos_bp.productos_add'))
    return render_template("editar_producto.html",form = frmProductos,productos = productos)
@productos_bp.route('/eliminar-producto/<int:id>',methods=['GET','POST'])
def producto_del(id):
    del_producto = DBProductos.query.filter(DBProductos.id_producto == id).first()
    db.session.delete(del_producto)
    db.session.commit()
    flash("ProveedorEliminado Exisotsamente!")
    return redirect(url_for('productos_bp.productos_add'))