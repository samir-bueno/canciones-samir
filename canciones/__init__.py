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
    consulta1 = """
           select name from tracks
        """
    consulta2 = """
             select name from artists
          """
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta1)
    lista_de_resultados = resultado.fetchall()

    resultado = base_de_datos.execute(consulta2)
    lista_de_bandas = resultado.fetchall()


    pagina = render_template("canciones.html", canciones=lista_de_resultados, bandas=lista_de_bandas)
    return pagina

