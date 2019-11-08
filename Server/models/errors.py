from flask import jsonify


class Errors():
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def toJson(self):
        return jsonify({
            'success': False,
            'msg': self.message
        }), self.code
