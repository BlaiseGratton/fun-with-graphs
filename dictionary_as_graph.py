simplest = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3, 5],
    5: [4]
}

with_attributes: {
    1: {
        'name': 'Frida',
        'knows': [2, 3]
    },
    2: {
        'name': 'Yianni',
        'knows': [1, 3]
    },
    3: {
        'name': 'Betsy',
        'knows': [1, 2, 4]
    },
    4: {
        'name': 'Harold',
        'knows': [3, 5]
    },
    5: {
        'name': 'Gail',
        'knows': [4]
    }
}

more_complex_attributes: {
    1: {
        'attributes': {
            'name': 'Frida',
            'age': 37,
        },
        'relationships': {
            'knows': [2, 3, 4],
            'loves': [4],
            'hates': [2]
        }
    },
    2: {
        'attributes': {
            'name': 'Yianni',
            'age': 29
        },
        'relationships': {
            'knows': [1, 3],
            'loves': [1, 4],
            'hates': []
        }
    },
    3: {
        'attributes': {
            'name': 'Betsy',
            'age': 32
        },
        'relationships': {
            'knows': [1, 2, 4],
            'loves': [],
            'hates': []
        }
    },
    4: {
        'attributes': {
            'name': 'Harold',
            'age': 32
        },
        'relationships': {
            'knows': [3, 5],
            'loves': [3],
            'hates': [4]
        }
    },
    5: {
        'attributes': {
            'name': 'Gail',
            'age': 32
        },
        'relationships': {
            'knows': [4],
            'loves': [2],
            'hates': [4]
        }
    }
}
