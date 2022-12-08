from app.api.base_model import Base, db

class Product(Base):
    """
        this is class that represent product table
    """
    __tablename__ = 'product'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Numeric(19,4))
    description = db.Column(db.Text())
    quantity = db.Column(db.Integer())
    is_active = db.Column(db.Boolean(), default=True)