from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request
from fpdf import FPDF
from ...model.frmInventario import FrmInventario
from ...model.DBIngresos import DBIngresos

from datetime import datetime
from ...model.DBProductos import DBProductos
from ...model.DBSalidas import DBSalidas
from WebApp import db
inventario_bp = Blueprint("inventario_bp",__name__)
@inventario_bp.route('/inventario/',methods=['GET','POST'])
def inventario_add():
    frmInventario = FrmInventario(meta={'csrf': False})
    if frmInventario.validate_on_submit():
        fecha1 = request.form.get('nombre')
        return redirect(url_for('hola',fecha1))
    return render_template("inventario.html",form = frmInventario)
@inventario_bp.route('/download',methods=['GET','POST'])
def download():
    request.args.get('nombre')
    return render_template("pdf.html")