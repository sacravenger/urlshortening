import json
import sqlite3
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for
# Inital flask
app = Flask(__name__)
# Create the environment variable of the secret key for hash id
app.config['SECRET_KEY'] = 'CsigT83vPa31N0sZ7dQo'

# create the 4 bits hashid
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


# Connect the database and return the sqlite3 connect object
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# The api is to use the post function shorten the url.
@app.route('/shortenurl', methods=['POST'])
def shortenurl():
    conn = get_db_connection()
    message={}
    if request.method == 'POST':

        if request:
            url = request.get_json().get('url')
        else:
            return json.dumps({'error':'body cannot be empty'}), 400, {'ContentType': 'application/json'}

        # check if the url is empty
        if not url:
            return json.dumps({'error':'url is required'}), 400, {'ContentType': 'application/json'}
        #update the url in the datbase
        url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))
        conn.commit()
        conn.close()
        # get the id of the url in the database
        url_id = url_data.lastrowid
        # endcode the id of the record
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid
        message['shorted url']=short_url

    return json.dumps(message), 200, {'ContentType':'application/json'}

# This function is to redirect the url
@app.route('/<id>',methods=['GET'])
def url_redirect(id):
    conn = get_db_connection()
    # Decode the shorted id to real id in the database
    original_id = hashids.decode(id)
    print(original_id)
    if original_id:
        original_id = original_id[0]
        # Get the data from the database by original id
        url_data = conn.execute('SELECT original_url FROM urls'
                                ' WHERE id = (?)', (original_id,)
                                ).fetchone()
        original_url = url_data['original_url']

        conn.close()
        # redirected to the original_url
        return redirect(original_url)


