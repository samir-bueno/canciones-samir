from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("artists",__name__, url_prefix="/artist")


@bp.route('/')
def bandas():
    consulta_bandas = """
             select name from artists
          """
    
    base_de_datos = db.get_db()
    

    resultado = base_de_datos.execute(consulta_bandas)
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("bandas.html", bandas=lista_de_bandas)
    return pagina











