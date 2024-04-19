#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：weather -> weather
@IDE    ：PyCharm
@Author ：sven
@Date   ：2024/4/18 21:51
@Desc   ：
"""


def create_aqi(**kwargs):
    return {
            "air": kwargs.get("air"),
            "air_level": kwargs.get("air_level"),
            "air_tips": kwargs.get("air_tips"),
            "co": kwargs.get("co"),
            "co_desc": kwargs.get("co_esc"),
            "jinghuaqi": kwargs.get("jinghuaqi"),
            "kaichuang": kwargs.get("kaichuang"),
            "kouzhao": kwargs.get("kouzhao"),
            "no2": kwargs.get("no2"),
            "no2_desc": kwargs.get("no2_desc"),
            "o3": kwargs.get("o3"),
            "o3_desc": kwargs.get("o3_desc"),
            "pm10": kwargs.get("pm10"),
            "pm10_desc": kwargs.get("pm10_desc"),
            "pm25": kwargs.get("pm25"),
            "pm25_desc": kwargs.get("pm25_desc"),
            "so2": kwargs.get("so2"),
            "so2_desc": kwargs.get("so2_desc"),
            "update_time": kwargs.get("update_time"),
            "waichu": kwargs.get("waichu"),
            "yundong": kwargs.get("yundong")
    }


def create_hour_info(**kwargs):
    return {
            "aqi": kwargs.get("aqi"),
            "aqinum": kwargs.get("aqinum"),
            "hours": kwargs.get("hours"),
            "tem": kwargs.get("tem"),
            "vis": kwargs.get("vis"),
            "wea": kwargs.get("wea"),
            "wea_img": kwargs.get("wea_img"),
            "win": kwargs.get("win"),
            "win_speed": kwargs.get("win_speed")
        }

def handle_hours(weather_hours):
    it = (create_hour_info(**item) for item in weather_hours)
    zip_ = map(lambda x: (x['hours'], x), it)
    return sorted(dict(zip_).values(), key=lambda x: x['hours'])


def create_weather_from_tq(**kwargs):

    aqi = kwargs.get('aqi') or {}
    hours = kwargs.get('hours')

    return {
        'aqi': create_aqi(**aqi),
        "city": kwargs.get('city'),
        "city_en": kwargs.get('cityEn'),
        "country": kwargs.get('country'),
        "country_en": kwargs.get('countryEn'),
        "date": kwargs.get('date'),
        "humidity": kwargs.get('humidity'),
        "pressure": kwargs.get('pressure'),
        "rain_pcpn": kwargs.get('rain_pcpn'),
        "sunrise": kwargs.get('sunrise'),
        "sunset": kwargs.get('sunset'),
        "tem": kwargs.get('tem'),
        "tem1": kwargs.get('tem1'),
        "tem2": kwargs.get('tem2'),
        "update_time": kwargs.get('update_time'),
        "uv_description": kwargs.get('uvDescription'),
        "uv_index": kwargs.get('uvIndex'),
        "visibility": kwargs.get('visibility'),
        "wea": kwargs.get('wea'),
        "wea_day": kwargs.get('wea_day'),
        "wea_day_img": kwargs.get('wea_day_img'),
        "wea_img": kwargs.get('wea_img'),
        "wea_night": kwargs.get('wea_night'),
        "wea_night_img": kwargs.get('wea_night_img'),
        "week": kwargs.get('week'),
        "win": kwargs.get('win'),
        "win_meter": kwargs.get('win_meter'),
        "win_speed": kwargs.get('win_speed'),
        "hours": handle_hours(hours) if hours and isinstance(hours, list) else []
    }


