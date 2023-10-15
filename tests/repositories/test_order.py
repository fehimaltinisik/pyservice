from typing import Dict

from sqlalchemy.future import Engine
from sqlmodel import Session
from sqlmodel import select

from src.entities import Order
from src.repositories import order_repository


class TestSaveAndRefresh:
    def test_should_save_and_refresh_new_order(self, engine: Engine, example_order_attrs: Dict):
        order = Order(**example_order_attrs)
        order_repository.save_and_refresh(order)

        with Session(engine) as session:
            query = select(Order).where(Order.id == order.id)
            expected_order_record: Order = session.exec(query).one_or_none()

        assert expected_order_record
        assert order.id == expected_order_record.id


class TestFindById:
    def test_should_find_order_by_id(self, engine, example_order_attrs: Dict):
        order = Order(**example_order_attrs)
        order_repository.save_and_refresh(order)

        expected_order_record: Order = order_repository.find_by_id(order.id)

        assert expected_order_record
        assert order.id == expected_order_record.id
