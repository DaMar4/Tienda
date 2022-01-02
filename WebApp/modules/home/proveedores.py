from flask import render_template,Blueprint,flash,redirect,url_for,request
from ...model.frmProveedores import FrmProveedores
from ...model.DBProveedores import DBProveedor
from WebApp import db
proveedores_bp = Blueprint("proveedores_bp",__name__)
@proveedores_bp.route('/proveedores',methods=['GET','POST'])
def proveedores():
    frmProveedores = FrmProveedores(meta={'csrf': False})
    proveedores = DBProveedor.query.order_by(DBProveedor.id_proveedor)
    if frmProveedores.validate_on_submit():
        nuevo_proveedor = DBProveedor(frmProveedores.proveedor.data)
        db.session.add(nuevo_proveedor)
        db.session.commit()
        flash("Proveedor Registrado Exitosamente!")
        return redirect(url_for('proveedores_bp.proveedores'))
    if frmProveedores.errors:
        flash(frmProveedores.errors, "danger")
    return render_template("proveedores.html",form=frmProveedores,proveedores = proveedores)
@proveedores_bp.route('/editar-proveedor/<int:id>',methods=['GET','POST'])
def proveedor_edit(id):
    proveedor=DBProveedor.query.get_or_404(id)
    frmProveedores = FrmProveedores(meta={'csrf': False})
    frmProveedores.proveedor.data = proveedor.proveedor
    if frmProveedores.validate_on_submit():
        p_edit = DBProveedor.query.filter(DBProveedor.id_proveedor == id).first()
        p_edit.proveedor = request.form['proveedor']
        db.session.add(p_edit)
        db.session.commit()
        flash("Proveedor Editado Exitosamente!")
        return redirect(url_for('proveedores_bp.proveedores'))
    return render_template("editar_proveedor.html",form = frmProveedores,proveedor=proveedor)
@proveedores_bp.route('/eliminar-proveedor/<int:id>',methods=['GET','POST'])
def producto_del(id):
    del_proveedor = DBProveedor.query.filter(DBProveedor.id_proveedor == id).first()
    db.session.delete(del_proveedor)
    db.session.commit()
    flash("Proveedor Eliminado Exitosamente!")
    return redirect(url_for('proveedores_bp.proveedores'))