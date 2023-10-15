from datetime import datetime
from typing import Dict

import pytest


@pytest.fixture
def example_order_attrs() -> Dict:
    return {
        'total': 99.90,
        'customer_id': 1}
