from flask import Flask
import requests,json
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/<string:input>/',methods=['GET', 'POST'])
def weather(input):
    '''
    used for temperature and humidity forecast graph plot using matplotlib
    '''

    # defining lists for storing data
    date = list()
    max_temp = list()
    min_temp = list()
    hum_max = list()
    hum_min = list()

    # read config file for api key and id
    f = open("C:\\Users\\shivi\\Desktop\\weather\\config.txt", "r")
    data = json.loads(f.read())

    # read data from file and store them into variables
    app_id = data['app_id']
    app_key = data['app_key']

    # base url used for getting weather forecast report
    url = "http://api.weatherunlocked.com/api/forecast/" + input + "?app_id="+ app_id +"&app_key="+ app_key +""

    # send request with headers for response
    response = requests.get(url,headers={'Content-Type':'application/json'})

    # convert response object into json
    data  = json.loads(response.text)['Days']

    for value in data:
        date.append(['date'])
        min_temp.append(value['temp_min_c'])
        max_temp.append(value['temp_max_c'])
        hum_max.append(value['humid_max_pct'])
        hum_min.append(value['humid_min_pct'])

    # define plot label and colour
    plt.plot(date, max_temp, 'b--', label='max temperature')
    plt.plot(date, min_temp, 'r--', label='min temperature')
    plt.plot(date, hum_max, 'g--', label='max humidity')
    plt.plot(date, hum_min, 'y--', label='min humidity')

    # used for show labels on graph
    plt.legend()

    # defining x-axis and y-axis label
    plt.xlabel('date')
    plt.ylabel('temperature in c and humidity')

    # graph title
    plt.title('Line graph!')

    plt.show()

    return 'success'

if __name__ == '__main__':
    app.run()
