from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    apikey = "438c13480cc2c4820de888d5cff19a6c"
    city = request.form['city']
    lang = "ja"
    
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    try:
        result = requests.get(api)
        data = json.loads(result.text)

        weather_data = {
            "city": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_deg": data["wind"]["deg"],
            "wind_speed": data["wind"]["speed"],
            "image_url": get_weather_image(data["weather"][0]["description"])
        }

        return render_template('weather.html', weather=weather_data)
    
    except Exception as e:
        error_message = "都市名を英語で入力してください。"
        return render_template('index.html', error=error_message)

def get_weather_image(description):
    if "晴天" in description:  # Clear
        return "/static/images/clear.png"
    elif "雲" in description:  # Clouds
        return "/static/images/cloudy.png"
    elif "雨" in description:  # Rain
        return "/static/images/rain.png"
    elif "雪" in description:  # Snow
        return "/static/images/snow.png"
    elif "雷雨" in description:  # Thunderstorm
        return "/static/images/Thunderstorm.png"
    elif "霧雨" in description:  # Drizzle
        return "/static/images/Drizzle.png"
    elif "霧" in description:  # Mist, Fog
        return "/static/images/Mist.png"
    elif "煙霧" in description:  # Haze 
        return "/static/images/Haze.png"
    elif "砂" in description:  # sand
        return "/static/images/sand.png"
    elif "竜巻" in description:  # Tornado 
        return "/static/images/Tornado.png"
    elif "灰" in description:  # Ash 
        return "/static/images/Ash.png"
    elif "突風" in description:  # Squall
        return "/static/images/Squall.png"
    elif "曇りがち" in description:  # very cloud
        return "/static/images/verycloudy.png"
    elif "厚い雲" in description:  # very cloud
        return "/static/images/Squall.png"
    
    else:
        return "/static/images/default.png"


if __name__ == "__main__":
    app.run(debug=True)
