CREATE_ORDER_REQUEST = {
    'Empty Order': {
        'summary': 'Empty Order',
        'description': 'An empty order with no products.',
        'value': {
            'customer_id': 1
        }
    }
}

CREATE_ORDER_RESPONSE = [
    {
        'id': '1',
        'customer_id': 1,
        'total': '0.0',
        'created_at': '2021-01-01T00:00:00.000000',
        'updated_at': '2021-01-01T00:00:00.000000',
    }
]

GET_ORDER_BY_ID_RESPONSE = CREATE_ORDER_RESPONSE
