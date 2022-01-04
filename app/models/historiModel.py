from datetime import datetime
from app import db


class Histori(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kelas = db.Column(db.String(100))
    tanggal = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hasilSenang = db.Column(db.String(100))
    hasilBiasa = db.Column(db.String(100))
    id_user = db.Column(db.String(50))

    def __init__(self, kelas, tanggal, hasilSenang, id_user, hasilBiasa):
        self.kelas = kelas
        self.tanggal = tanggal
        self.hasilSenang = hasilSenang
        self.hasilBiasa = hasilBiasa
        self.id_user = id_user