from app import app
from flask import request, jsonify
from flask_marshmallow import Marshmallow
from app.models.dosenModel import db, Dosen

ma = Marshmallow(app)


class DosenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nama_dosen', 'mata_kuliah')


# init schema
dosenSchema = DosenSchema()
dosensSchema = DosenSchema(many=True)



def createDosen():
    nama_dosen = request.form['nama_dosen']
    mata_kuliah = request.form['mata_kuliah']

    newsDosen = Dosen(nama_dosen=nama_dosen, mata_kuliah=mata_kuliah)

    db.session.add(newsDosen)
    db.session.commit()
    new = dosenSchema.dump(newsDosen)
    return jsonify({"msg": "success get all dosen", "status": 200, "data": new})


def getAlldosen():
    allDosen = Dosen.query.all()
    result = dosensSchema.dump(allDosen)
    return jsonify({"msg": "Success Get all dosen", "status": 200, "data": result})


def getDosenById(id):
    dosen = Dosen.query.get(id)
    dosenDetails = dosenSchema.dump(dosen)
    return jsonify({"msg": "Success get mitra by id", "status": 200, "data": dosenDetails})


def updateDosen(id):
    dosen = Dosen.query.get(id)
    nama_dosen = request.form['nama_dosen']
    mata_kuliah = request.form['mata_kuliah']

    dosen.nama_dosen = nama_dosen
    dosen.mata_kuliah = mata_kuliah

    db.session.commit()
    dosenUpdate = dosenSchema.dump(dosen)
    return jsonify({"msg": "Success update mitra", "status": 200, "data": dosenUpdate})


def deleteDosen(id):
    dosen = Dosen.query.get(id)
    db.session.delete(dosen)
    db.session.commit()
    dosenDelete = dosenSchema.dump(dosen)
    return jsonify({"msg": "Success Delete mitra", "status": 200, "data": dosenDelete})
