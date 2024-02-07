from flask import Flask, jsonify
import random

app = Flask(__name__)

full_time = {}

@app.route('/time', methods=['GET'])
def get_time():
    time = [] 
    
    for i in range(3):
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)

        time.append(f'{hours:02d}:{minutes:02d}')

    global full_time
    full_time = {'Time': {'America': time[0], 'Europe': time[1], 'Asia': time[2]}}

    return jsonify(full_time)

@app.route('/time/<region>',methods=['GET'])
def time_by_region(region):
    global full_time

    region = region.lower()
    region = region.replace('_', ' ').title().replace(' ', '')


    return jsonify({region : full_time['Time'][region]})



if __name__ == '__main__':
    app.run(debug=True)