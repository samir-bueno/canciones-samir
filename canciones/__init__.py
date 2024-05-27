from flask import Flask, render_template

app = Flask(__name__)


with app.app_context():
  from . import db
  db.init_app(app)


from . import artists
app.register_blueprint(artists.bp)

from . import generos
app.register_blueprint(generos.bp)

from . import canciones
app.register_blueprint(canciones.bp)

   
   