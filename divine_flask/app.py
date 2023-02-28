from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime


app = Flask(__name__)

# Connect to the MySQL database
cnx = mysql.connector.connect(user='sql8600590',
                              password='gg9TmutCxU',
                              host='sql8.freemysqlhosting.net',
                              database='sql8600590')
cursor = cnx.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polling_unit_form')
def polling_unit_form():
    cursor.execute("SELECT DISTINCT polling_unit_uniqueid  FROM announced_pu_results")
    results = cursor.fetchall()
    unit_ids = [result[0] for result in results]
    return render_template('polling_unit_form.html', unit_ids=unit_ids)



@app.route('/polling_unit_result')
def polling_unit_result():
    polling_unit_id = request.args.get('polling_unit_id')
    # Retrieve polling unit result from database
    cursor.execute(
        "SELECT party_abbreviation, party_score FROM announced_pu_results WHERE polling_unit_uniqueid = %s",
        (polling_unit_id,)
    )
    results = cursor.fetchall()
    # Retrieve polling unit information from database
    cursor.execute(
        "SELECT polling_unit_number, polling_unit_name, lga_name FROM polling_unit INNER JOIN lga ON polling_unit.lga_id = lga.lga_id WHERE polling_unit.uniqueid = %s",
        (polling_unit_id,)
    )
    polling_unit_info = cursor.fetchone()
    return render_template('polling_unit_result.html', results=results, polling_unit_info=polling_unit_info)


@app.route('/displayform')
def displayform():
    cursor.execute("SELECT lga_name FROM lga")
    lgas = cursor.fetchall()
    return render_template('displayform.html', lgas=lgas)

@app.route('/display', methods=['POST'])
def display():
    lga_name = request.form['lga_name']
    print('lga_name:', lga_name)
    cursor.execute("SELECT l.lga_name, p.partyname, SUM(ar.party_score) as total_votes FROM polling_unit pu JOIN announced_pu_results ar ON pu.polling_unit_id = ar.polling_unit_uniqueid JOIN party p ON ar.party_abbreviation = p.partyid JOIN lga l ON pu.lga_id = l.lga_id WHERE l.lga_name =%s GROUP BY l.lga_name, p.partyname ORDER BY total_votes DESC", (lga_name,))
    result = cursor.fetchall()
    # Calculate the total score
    total_score = sum(int(row[2]) for row in result)
    print(total_score)  # add this line to see the result in the console
    return render_template('display.html', result=result, total_score=total_score)


@app.route('/new_polling_unit', methods=['GET', 'POST'])
def new_polling_unit():
    if request.method == 'POST':
        # Get form data
        polling_unit_name = request.form['polling_unit_name']
        lga_name = request.form['lga_name']
        ward_id = request.form['ward_id']
        polling_unit_id = request.form['polling_unit_id']
        party_scores = request.form.getlist('party_score')
        entered_by_user = request.form.get('entered_by_user')
        party_abbreviations = request.form.getlist('party_abbreviation')
        
        # Retrieve the lga_id from the lga table using the lga_name submitted with the form data
        cursor.execute("SELECT lga_id FROM lga WHERE lga_name = %s", (lga_name,))
        lga_id = cursor.fetchone()[0]

        # Create new polling unit entry
        cursor.execute("INSERT INTO polling_unit (polling_unit_id, polling_unit_name, lga_id, ward_id) VALUES (%s, %s, %s, %s)", ( polling_unit_id, polling_unit_name, lga_id, ward_id))
        # get the current date and time
        current_date_time = datetime.now()
        # get the user ip address
        user_ip_address = request.remote_addr
        # Create new party result entries
        for i in range(len(party_scores)):
            cursor.execute("INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score, entered_by_user, date_entered, user_ip_address) VALUES (%s, %s, %s,%s, %s,%s)", (polling_unit_id, party_abbreviations[i], party_scores[i], entered_by_user, current_date_time,user_ip_address))
        
        # Commit changes and redirect to confirmation page
        cnx.commit()
        Flask('submitted sucesssfully')
    
    # If GET request, render form template with dropdown menus for LGA and party names
    cursor.execute("SELECT lga_name FROM lga")
    lgas = cursor.fetchall()
    cursor.execute("SELECT partyname FROM party")
    parties = cursor.fetchall()
    return render_template('new_polling_unit.html', lgas=lgas, parties=parties)


if __name__ == '__main__':
    app.run(debug=True)


