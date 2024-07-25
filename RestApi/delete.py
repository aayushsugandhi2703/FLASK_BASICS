from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

vid_list = {}

video_parser = reqparse.RequestParser()
video_parser.add_argument('name', type=str, help='Name of the video', required=True)
video_parser.add_argument('views', type=int, help='Views on the video', required=True)

def cancel(id):
    if id not in vid_list:
        abort(404, message="Video doesn't exist")
def exist(id):
    if id in vid_list:
        abort(409, message="Video already exists")

class Video(Resource):
    def get(self, id):
        cancel(id)
        return vid_list[id]
    
    def put(self, id):
        exist(id)
        args = video_parser.parse_args()
        vid_list[id] = {
            'id': id,
            'name': args['name'],
            'views': args['views']
        }
        return vid_list[id], 201
    
    def delete(self, id):
        cancel(id)
        del vid_list[id]
        return '', 204

api.add_resource(Video, '/video/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
