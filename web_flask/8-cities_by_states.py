#!/usr/bin/python3

"""
Script that starts a Flask web application:
- Web appli must be listening on 0.0.0.0, port 5000
- You must use storage for fetching data from the storage engine)
- After each request you must remove the current SQLAlchemy Session:
- Declare a method to handle @app.teardown_appcontext
  Call in this method storage.close()
- To load all cities of a State:
  if your storage engine is DBStorage, you must use cities relationship
  otherwise, use the public getter method cities
- Routes:/cities_by_states: display a HTML page: (inside the tag BODY)
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with the cities_by_states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Close the storage"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
