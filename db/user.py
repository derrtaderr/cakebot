import datetime
from typing import List

from db.base_class import SqlAlchemyBase
from db.order import Order


class User(SqlAlchemyBase):
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_data: datetime.datetime = sa.Column(sa.DATETIME, default=datetime.datetime.now, index=True)

    name: str = sa.Column(sa.String)
    phone: str = sa.Column(sa.String, index=True)
    email: str = sa.Column(sa.String, index=True)

    # orders: List[Order]