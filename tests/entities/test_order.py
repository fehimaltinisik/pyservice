from datetime import datetime
from datetime import timedelta
from typing import Dict

import pytest

from src.entities import Order


class TestIsReturnEligible:
    @pytest.fixture(scope='function')
    def order_attrs(self) -> Dict:
        return {'customer_name': "Jane Smith", 'total_amount': 800.0}

    def test_order_within_eligibility_period(self, order_attrs):
        created_at_within_the_14_day_period = datetime.utcnow() - timedelta(days=7)
        order_within_eligibility_period = Order(**order_attrs, created_at=created_at_within_the_14_day_period)

        assert order_within_eligibility_period.is_return_eligible is True

    def test_order_outside_eligibility_period(self, order_attrs):
        created_at_outside_the_14_day_period = datetime.utcnow() - timedelta(days=15)
        order_outside_eligibility_period = Order(**order_attrs, created_at=created_at_outside_the_14_day_period)

        assert order_outside_eligibility_period.is_return_eligible is False
