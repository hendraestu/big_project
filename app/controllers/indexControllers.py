from app import app
from flask import render_template

@app.route('/beranda', methods=['GET'])
def beranda():
    return render_template('beranda.html')

@app.route('/ambilFoto', methods=['GET'])
def ambil():
    return render_template('ambilFoto.html')

@app.route('/riwayat', methods=['GET'])
def histori():
    return render_template('riwayat.html')


