from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("albums",__name__, url_prefix="/albums")


@bp.route('/')
def bandas():
    consulta_albums = """
             select Title from albums
          """
    
    base_de_datos = db.get_db()
    

    resultado = base_de_datos.execute(consulta_albums)
    lista_de_albums = resultado.fetchall()

    pagina = render_template("albums.html", albums=lista_de_albums)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    consulta_album = """
        SELECT Title, AlbumId from albums
        where AlbumId = ?;
    """
    consulta_detalle_album= """
       SELECT name, AlbumId from tracks 
       where AlbumId = ?;
    """
    base_de_datos = db.get_db()
    
    resultado = base_de_datos.execute(consulta_album, (id, ))
    albums = resultado.fetchone()

    resultado = base_de_datos.execute(consulta_detalle_album, (id, ))
    lista_de_albums = resultado.fetchall()

    pagina = render_template("detalle_albums.html", album = albums, albums_lista = lista_de_albums)
    return pagina