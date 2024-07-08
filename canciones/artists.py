from flask import Flask, render_template, Blueprint, request, redirect, url_for
from . import db

bp = Blueprint("artists",__name__, url_prefix="/artist")


@bp.route('/')
def artistas():
    consulta_artistas = """
             SELECT name, ArtistId FROM artists 
          """
    
    base_de_datos = db.get_db()
    

    resultado = base_de_datos.execute(consulta_artistas)
    lista_de_artistas = resultado.fetchall()

    pagina = render_template("artistas.html", artista=lista_de_artistas)
    return pagina

@bp.route("/<int:id>")
def detalle(id):
    consulta_artista = """
        SELECT Name FROM artists
        WHERE ArtistId = ? ;
    """
    consulta_detalle_artista = """
        SELECT Title, AlbumId FROM albums 
        WHERE ArtistId = ? ;
    """
    base_de_datos = db.get_db()
    
    resultado = base_de_datos.execute(consulta_artista, (id, ))
    artistas = resultado.fetchone()

    resultado = base_de_datos.execute(consulta_detalle_artista, (id, ))
    lista_de_albums = resultado.fetchall()

    pagina = render_template("detalle_artista.html", artista = artistas, albums = lista_de_albums)
    return pagina


@bp.route('/new', methods=('GET', 'POST'))
def nuevo():
    if request.method == "POST":
          name = request.form['name']

          con = db.get_db()
          consulta = """
                    INSERT INTO artists (Name)
                    VALUES (?)
          """
            
          con.execute(consulta, (name,))
          con.commit()
          return redirect(url_for('artists.artistas'))
    else:
        pagina = render_template('nuevo_artista.html')
        return pagina









