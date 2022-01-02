from os import abort
from flask import render_template, flash, redirect, url_for, request,send_file,abort
from flask.blueprints import Blueprint
from flask_login import login_required,current_user
from fpdf import FPDF
from WebApp.model.model import ProductForm, StockTienda
from WebApp import db
from WebApp import admin_need
import os
crud = Blueprint("crud", __name__)
@crud.before_request
@login_required
def constructor():
    pass


@crud.route('/reporte/')
@admin_need
def reporte():
    salida = StockTienda.query.all()
    return render_template("reportes.html",salida=salida)
@crud.route('/reporte/<int:id>')
def download(id):
    salida_id = StockTienda.query.get(id)
    try:
        return send_file("static/reportes/"+str(salida_id.fecha)+".pdf",None,as_attachment=True)
    except:
        return abort(404)