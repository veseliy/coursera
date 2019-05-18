import json
import functools


def to_json(func):
    # @functools.wraps(func)
    def wrapped(*agrs, **kwargs):
        return json.dumps(func(*agrs, **kwargs))
    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


get_data()  # вернёт '{"data": 42}'