# Reusable way to post errors
from flask import jsonify


class Errors():
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def to_json(self):
        return jsonify({
            'success': False,
            'msg': self.message
        }), self.code
