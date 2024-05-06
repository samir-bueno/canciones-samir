from flask import Flask, render_template


app = Flask(__name__)


with app.app_context():
  from . import db
  db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/canciones')
def canciones():
    base_de_datos = db.get_db()
    consulta = """
        select g.name as genero, t.name as canciones, a.Title as albuns from genres g
        join tracks t on g.GenreId = t.GenreId
        join albums a on t.AlbumId = a.AlbumId
        """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultados = resultado.fetchall()
    return render_template("canciones.html", canciones=lista_de_resultados)

