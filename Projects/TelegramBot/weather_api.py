import requests
from datetime import datetime

def convert_time(time):
    ts = int(time)
    return (datetime.utcfromtimestamp(ts).strftime('%H:%M'))

def get_weather():
    api_url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q' : 'Saint Petersburg',
        'appid':'fc387c704644cdbdec3279dc0bb0ce76',
        'lang' : 'ru',
        'units' : 'metric'
    }
    res = requests.get(api_url, params = params)
    res = res.json()
    # print(res)
    template = f"Температура за окном {res['main']['temp']}. Ощущается как {res['main']['feels_like']}.\n {res['weather'][0]['description']}. Солнце зайдет в {convert_time(res['sys']['sunset'])} "
    icon_path = 'icons/{}@2x.png'.format(res['weather'][0]['icon'])
    return([template,icon_path])


if __name__ == '__main__':
    weather , path = get_weather()
    print(weather,path)
    # 04d@2x.png


