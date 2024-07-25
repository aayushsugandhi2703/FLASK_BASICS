from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

'''
# basics Defining a class for the example resource
class example(Resource):
    def get(self):
        return {'hello': 'world'} 
api.add_resource(example, '/example')

'''
'''videos = {
    10: { "video_id": 10, "name": "Lion King", "views": 10000 }
}
class video(Resource):
    def get(self, video_id):
        return videos[video_id]

api.add_resource(video, '/video/<int:video_id>')
'''

movie = reqparse.RequestParser()
movie.add_argument('name', type=str, help='Name of the video', required=True)
movie.add_argument('likes', type=int, help='likes on video', required=True)

movies = {}

class Movie(Resource):
    def get(self, movie_id):
        if movie_id in movies:
            return movies[movie_id]
        else:
            return {'message': 'Movie not found'}, 404
    
    def put(self, movie_id):
        args = movie.parse_args()
        movies[movie_id] = {
            'movie_id': movie_id,
            'name': args['name'],   
            'likes': args['likes']
        }
        return movies[movie_id], 201  # Status code 201 for creation

# Register the resource with the API
api.add_resource(Movie, '/movie/<int:movie_id>')

if __name__ == '__main__':
    app.run(debug=True) 