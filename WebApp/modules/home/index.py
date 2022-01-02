from flask import render_template, flash, redirect, url_for, request
from flask.blueprints import Blueprint
from sqlalchemy.orm import query
from flask_login import login_required
from WebApp import db
from WebApp.model.inicio import Usuario
from WebApp.modules.iniciar.login_user import login

index = Blueprint("index", __name__)
@index.before_request
@login_required
def constructor():
    pass
@index.route("/")
def main_page():
    return render_template("index.html")