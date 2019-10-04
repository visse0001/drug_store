from flask import render_template, request, redirect, Blueprint, get_flashed_messages, flash
from db_utils import get_connection
from auth import login_required


meds_bp = Blueprint('meds_bp', __name__)


@meds_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('add.html', messages=messages)

    if request.method == 'POST':
        name = str(request.form['name']).title()
        active_substance = str(request.form['active_substance']).lower()
        price = float(request.form['price'])
        dosage_form = request.form['dosage_form']
        quantity = int(request.form['quantity'])
        capacity = int(request.form['capacity'])

        parameters_dosage_form = ('pills', 'mixture', 'drops' 'suspension', 'injection', 'plaster', 'aerosol')

        if '' in (name, active_substance, price, quantity, capacity,):
            flash('Please try again.')
            return redirect('/add')
        elif dosage_form not in parameters_dosage_form:
            return redirect('/add')
        elif price is not float:
            price = float(price)  # Czy to ma sens?
        elif capacity < 0 or quantity < 0 or price < 0:
            flash('Wrong data. Please try again.')
            return redirect('/add')
        else:
            return redirect('/add')

        conn = get_connection()
        c = conn.cursor()

        query = 'INSERT INTO "medicines" ("name", "active_substance", "price", "dosage_form", "capacity", "quantity") ' \
                'VALUES (?, ?, ?, ?, ?, ?)'
        parameters = (name, active_substance, price, dosage_form, capacity, quantity,)

        c.execute(query, parameters)
        conn.commit()

        return redirect('/')


@meds_bp.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('delete.html', messages=messages)

    if request.method == 'POST':
        id = int(request.form['id'])

        conn = get_connection()
        c = conn.cursor()

        if id == None:
            flash('Please try again.')
            return redirect('/delete')

        query = 'DELETE FROM "medicines" WHERE id = ?'
        parameters = (id,)

        c.execute(query, parameters)
        conn.commit()

        if c.rowcount != 1:
            flash('Wrong id. Try again.')
            return redirect('/delete')
        else:
            return redirect('/')


@meds_bp.route('/find', methods=['GET', 'POST'])
@login_required
def find():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('find.html', messages=messages)

    if request.method == 'POST':
        find_name = request.form['find_name'].title()
        find_active_substance = request.form['find_active_substance'].lower()


        conn = get_connection()
        c = conn.cursor()

        query = "SELECT * FROM medicines WHERE name LIKE ? AND active_substance LIKE ?"

        find_name = f'%{find_name}%'
        find_active_substance = f'%{find_active_substance}%'
        parameters = (find_name, find_active_substance)
        result = c.execute(query, parameters)
        meds = result.fetchall()

        context = {'meds': meds}

        return render_template('find.html', **context)


@meds_bp.route('/find_in_pharmacy', methods=['GET', 'POST'])
@login_required
def find_in_pharmacy():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('find_in_pharmacy.html', messages=messages)
    if request.method == 'POST':
        find_name_pharmacy = request.form['find_name_pharmacy']
        if find_name_pharmacy:
            return redirect('https://www.aptekagemini.pl/search/st_search/?q=' + find_name_pharmacy)
        else:
            flash('Try again.')
            return redirect('/find_in_pharmacy')
