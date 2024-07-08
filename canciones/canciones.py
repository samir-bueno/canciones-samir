from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint("canciones",__name__, url_prefix="/canciones")

@bp.route('/')
def canciones():
    consulta_canciones = """
            select name, composer from tracks
          """
    base_de_datos = db.get_db()

    resultado = base_de_datos.execute(consulta_canciones)

    lista_de_canciones = resultado.fetchall()

    pagina = render_template("canciones.html", canciones=lista_de_canciones)
    return pagina


@bp.route("/<int:id>")
def detalle(id):
    consulta1 = """
        select Name from tracks
        WHERE TrackId = ?
    """

    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta1, (id, ))
    cancion = resultado.fetchone()


    pagina = render_template("detalle_canciones.html", cancion = cancion)
    return pagina
