import requests

URL = 'https://roads.googleapis.com/v1/snapToRoads'
API_KEY = 'AIzaSyAs7VqYNpKdru6FJDc8CZEsYApOEQ_zJIU'


def interpolate_road_points(path):
    params = {
        'interpolate': True,
        'path': path,
        'key': API_KEY,
    }
    response = requests.get(url=URL, params=params).json()
    data = []
    for point in response['snappedPoints']:
        data.append(point['location'])
    return data
