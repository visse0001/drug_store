from flask import render_template, Blueprint
from db_utils import get_connection

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    conn = get_connection()
    c = conn.cursor()

    result = c.execute('SELECT * FROM medicines')
    meds = result.fetchall()

    context = {'meds': meds}

    return render_template('index.html', **context)

