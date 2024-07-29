from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

videos ={}

video_parser = reqparse.RequestParser()
video_parser.add_argument('name', type=str, help ="name of hte video", required=True)

class Video(Resource):
    def get(self, id):
        return videos[id]

    def put(self, id):
        args = video_parser.parse_args()
        videos[id] = {
            'id': id,
            'name': args['name'] 
            }
        return videos[id], 201

api.add_resource(Video, '/video/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
