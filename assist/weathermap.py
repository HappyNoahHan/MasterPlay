from assist import weather

weather_dict = {
    'W001': weather.Weather(name='大晴天',code='W001'),
    'W002': weather.Weather(name='大日照',code='W002'),
    'W003': weather.Weather(name='晴天',code='W003'),
    'W004': weather.Sandstorm(),
    'W005': weather.Weather(name='冰雹',code='W005'),
    'W006': weather.Weather(name='下雨',code='W006'),
    'W007': weather.Weather(name='大雨',code='W007'),
    'W008': weather.Weather(name='雾气',code='W008'),

}