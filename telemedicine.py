from app import app, db # Imports the application instance
from app.models import User, Appointments
import datetime


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Appointments': Appointments,
        'datetime': datetime
    }