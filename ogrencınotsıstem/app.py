from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/kaydet', methods=['POST'])
def kaydet():

    adi = request.form['adi']
    soyadi = request.form['soyadi']
    sifre = request.form['sifre']
    vize = int(request.form['vize'])
    final = int(request.form['final'])

    ort = (vize + final) / 2
    gectiMi = "EVET" if ort >= 50 else "HAYIR"

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kitrvm231229069",
        database="okuldb"
    )

    cursor = conn.cursor()

    sql = "INSERT INTO ogrenciler (adi, soyadi, sifre, vize, final, ort, gectiMi) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    cursor.execute(sql,(adi,soyadi,sifre,vize,final,ort,gectiMi))

    conn.commit()
    conn.close()

    return render_template("sonuc.html", ort=ort, durum=gectiMi)

app.run(debug=True)