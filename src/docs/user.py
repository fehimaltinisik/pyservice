CREATE_USER_REQUEST = {
    'Edsger W. Dijkstra': {
        'summary': 'Edsger W. Dijkstra',
        'description': 'Edsger W. Dijkstra',
        'value': {
            'first': 'Edsger W.',
            'last': 'Dijkstra',
            'email': 'edsgerdijkstra@leiden.edu.tr',
            'password': 'edsgerdijkstra',
            'birthYear': 1930,
            'birthMonth': 5,
            'birthDay': 11
        }
    },
    'Brian Kerninghan': {
        'summary': 'Brian Kerninghan',
        'description': 'Brian Kerninghan',
        'value': {
            'first': 'Brian',
            'last': 'Kerninghan',
            'email': 'briankerninghan@princeton.edu.tr',
            'password': 'briankerninghan',
            'birthYear': 1942,
            'birthMonth': 1,
            'birthDay': 1
        }
    }
}

CREATE_USER_RESPONSE = [
    {
        'id': '1',
        'first': 'Edsger W.',
        'last': 'Dijkstra',
        'email': 'edsgerdijkstra@leiden.edu.tr',
        'birthdate': '1930-05-11'
    },
    {
        'id': '2',
        'first': 'Brian',
        'last': 'Kerninghan',
        'email': 'briankerninghan@princeton.edu.tr',
        'birthdate': '1942-01-01'
    }
]

GET_USER_BY_ID_RESPONSE = CREATE_USER_RESPONSE
