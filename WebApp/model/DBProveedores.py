from WebApp import db
class DBProveedor(db.Model):
    __tablename__="proveedor"
    id_proveedor = db.Column(db.Integer,primary_key=True,autoincrement=True)
    proveedor = db.Column(db.String(255))
    def __init__(self,proveedor):
        self.proveedor = proveedor
    def __repr__(self) -> str:
        return "<DBProveedor %r>" % self.proveedor