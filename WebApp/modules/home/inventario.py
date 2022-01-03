from flask import Flask,render_template,Blueprint,flash,redirect,url_for,request,send_file
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
    return render_template("inventario.html",form = frmInventario)
@inventario_bp.route('/download/',methods=['GET','POST'])
def download():
    f= request.form['fecha_inicio']
    datos = DBIngresos.query.filter(DBIngresos.fecha == f).all()
    datos_salida = DBSalidas.query.order_by(DBSalidas.cantidad).all()
    #creacion pdf
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_author("Powered By Gabino García")
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(0 ,0,0)
        pdf.image("WebApp/static/img/logo2.png",20,10,30,18)
        pdf.cell(0, 15, '(CGMAIG) COORDINACIÓN GENERAL DE MODERNIZACIÓN',0,1,"C")
        pdf.cell(0, 1, 'ADMINISTRATIVO E INNOVACIÓN GUBERNAMENTAL',0,1,"C")
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(0, 25,"REGISTRO DE INVENTARIO", border=0, fill=0, align="C", ln=25)
        ####tabla
        pdf.set_font('Arial', 'B', 9)
        pdf.cell(10,10,"No",1)
        pdf.cell(22,10,"FECHA",1)
        pdf.cell(60,10,"DESCRIPCIÓN",1)
        pdf.cell(25,10,"UNIDAD",1)
        pdf.cell(25,10,"CATEGORÍA",1)
        pdf.cell(25,10,"SALIDA",1)
        pdf.multi_cell(0,10,"STOCK",1)
        #BODY
        #25 registros
        pdf.set_font('Arial', '', 7)
        for i in datos:
            pdf.cell(10,6,"",1)
            pdf.cell(22,6,i.fecha,1)
            pdf.cell(60,6,i.descripcion,1)
            pdf.cell(25,6,i.unidad,1)
            pdf.cell(25,6,i.categoria,1)
            pdf.cell(25,6,"",1)
            pdf.multi_cell(0,6,"#",1)
        #ENDBODY
        pdf.rect(10,61.1,190.0,184,"D")
        pdf.set_xy(10,250)
        pdf.cell(48,5,"AUTORIZÓ",0,0,"C")
        pdf.cell(65,5,"",0)
        pdf.multi_cell(0,5,"SOLICITÓ",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.multi_cell(0,3,"",0,"C")
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(57,5,"SILVIA ELENA FLORES BANDA",0,0,"C")
        pdf.set_font('Arial', '', 11)
        pdf.cell(55,5,"",0)
        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(0,5,"TERESA DE JESUS LOPEZ HERNANDEZ",0,0,"C")
        pdf.set_font('Arial', '', 11)
        pdf.cell(64,5,"SUBDIRECTORA DE SUPERVISIÓN",0,0,"C")
        pdf.cell(69,5,"",0)
        pdf.multi_cell(0,5,"ADMINISTRADOR",0,0,"C")
        pdf.cell(52,5,"DE CALIDAD Y EVALUACIÓN",0,0,"C")
        pdf.output('WebApp/static/'+f+'.pdf', 'F')
        return send_file("static/"+f+".pdf",None,as_attachment=True)
    except:
        pass
    return render_template("pdf.html",fecha=f)