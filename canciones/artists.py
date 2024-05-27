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

@bp.route("/<int:id>")
def detalle(id):
    consulta1 = """
        SELECT Name, ArtistId FROM artists
        WHERE ArtistId = ? ;
    """
    consulta2 = """
        SELECT t.name, g.Title FROM tracks t
        JOIN albums g ON t.AlbumId = g.AlbumId
        JOIN artists a ON g.ArtistId = a.ArtistId
        WHERE a.ArtistId = ? ;
    """
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta1, (id, ))
    artista = resultado.fetchone()

    resultado = base_de_datos.execute(consulta2, (id, ))
    lista_canciones = resultado.fetchall()

    pagina = render_template("detalle_artista.html", artista = artista, canciones = lista_canciones)
    return pagina










