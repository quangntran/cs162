import requests

r = requests.get('https://adsbexchange.com/api/aircraft/json/')


def print_data(data):
    for flight in data['ac']:
        print(flight['cou'],' : ', flight['icao'], ' : ', flight['alt'])



if __name__ == "__main__":
    print('Response status code:', r.status_code)
    if r.status_code == 200:
        data = r.json()
        print_data(data)
