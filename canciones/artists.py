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
    consulta_artista = """
        SELECT Name, ArtistId FROM artists
        WHERE ArtistId = ? ;
    """
    consulta_detalle_artista = """
       SELECT Title, ArtistId FROM albums a
        WHERE a.ArtistId = ? ;
    """
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_artista, (id, ))
    artistas = resultado.fetchone()

    resultado = base_de_datos.execute(consulta_detalle_artista, (id, ))
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("detalle_banda.html", artista = artistas, bandas = lista_de_bandas)
    return pagina










