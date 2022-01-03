from app import db

class Dosen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_dosen = db.Column(db.String(100))
    mata_kuliah = db.Column(db.String(200))

    def __init__(self, nama_dosen, mata_kuliah):
        self.nama_dosen = nama_dosen
        self.mata_kuliah = mata_kuliah