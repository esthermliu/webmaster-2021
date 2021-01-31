from flask import Flask, request # Creates app as an instance of class Flask imported from the flask package
from flaskext.markdown import Markdown

app = Flask(__name__) # __name__ is a Python predefined variable, set to the name of the module in which it is used
Markdown(app)

from app import routes # Importing the routes module, imported at the bottom to avoid circular imports
