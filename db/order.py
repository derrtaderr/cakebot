import datetime
import sqlalchemy as sa

from db.base_class import SqlAlchemyBase


class Order(SqlAlchemyBase):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(sa.DATETIME, default=datetime.datetime.now, index=True)
    fulfilled_date: datetime.datetime = sa.Column(sa.DATETIME, index=True)

    size: str = sa.Column(sa.String)
    flavour: str = sa.Column(sa.String)
    topping: str = sa.Column(sa.String)
    frosting: str = sa.Column(sa.String)
    price: float = sa.Column(sa.Float, index=True)

    user_id: int = sa.Column(sa.Integer)
    user:"User"