from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("artistas",__name__, url_prefix="/proyecto_canciones")

@bp.route('/')
def hello():
    return 'Hello, World!'


@bp.route('/<int:id>')
def canciones(id):
    consulta_canciones = """
            select name from tracks where GenreId = ?;
          """
    
    consulta_generos = """
            select g.name from genres g 
            JOIN tracks t on g.GenreId = t.GenreId 
            where g.GenreId = ?;

          """
    
    consulta_bandas = """
             select name from artists
          """
    
    base_de_datos = db.get_db()
    
    resultado = base_de_datos.execute(consulta_canciones, (id,))
    lista_de_canciones = resultado.fetchall()

    resultado = base_de_datos.execute(consulta_generos, (id, ))
    lista_de_generos = resultado.fetchall()

    resultado = base_de_datos.execute(consulta_bandas)
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("canciones.html", canciones=lista_de_canciones, generos=lista_de_generos, bandas=lista_de_bandas)
    return pagina

   



