from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("canciones",__name__, url_prefix="/canciones")

@bp.route('/')
def canciones():
    consulta_canciones = """
            select name from tracks
          """
    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_canciones)

    lista_de_canciones = resultado.fetchall()

    pagina = render_template("canciones.html", canciones=lista_de_canciones)
    return pagina


@bp.route("/<int:id>")
def album_detalle(id):
    consulta1 = """
        SELECT Title, AlbumId FROM albums
        WHERE AlbumId = ? ;
    """
    consulta2 = """
        SELECT a.name, g.Title FROM albums g
        JOIN tracks a ON g.AlbumId = a.AlbumId
        WHERE g.AlbumId = ? ;
    """
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta1, (id, ))
    cancion = resultado.fetchone()

    resultado = base_de_datos.execute(consulta2, (id, ))
    lista_canciones = resultado.fetchall()

    pagina = render_template("detalle_canciones.html", cancion = cancion, canciones = lista_canciones)
    return pagina
