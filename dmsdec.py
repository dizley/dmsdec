'''
Created on Nov 6, 2014

@author: James Disley
'''

import re
import math

def dms2dec(location, ndecimals=6):
    lon, lat = location[0], location[1]
    
    numbers = re.compile(r"(\d+\.?\d*)")
    letter = re.compile(r"([A-Z])$")
    
    lon_deg, lon_min, lon_sec = numbers.findall(lon)
    lon_direction = letter.search(lon).group(0)
    lat_deg, lat_min, lat_sec = numbers.findall(lat)
    lat_direction = letter.search(lat).group(0)
    
    #print(lon_direction, lat_direction)
    
    lon_dec = round(float(lon_deg) + float(lon_min)/60 + float(lon_sec)/3600, ndecimals)
    lat_dec = round(float(lat_deg) + float(lat_min)/60 + float(lat_sec)/3600, ndecimals)
    
    if(lon_direction == 'S'):
        lon_dec = lon_dec*-1
    if(lat_direction == 'W'):
        lat_dec = lat_dec*-1
    
    return (lon_dec, lat_dec)

def dec2dms(location, seperator=' '):
    lon, lat = location[0], location[1]
    
    south = False
    west = False
    
    if(lon < 0): 
        lon=lon*-1
        south = True
    if(lat < 0): 
        lat=lat*-1
        west = True
    
    lon_deg = math.floor(lon)
    lon_min = math.floor((lon - lon_deg) * 60)
    lon_sec = round((lon*3600 - lon_deg*3600 - lon_min*60), 2)
    
    lat_deg = math.floor(lat)
    lat_min= math.floor((lat - lat_deg) * 60)
    lat_sec = round((lat*3600 - lat_deg*3600 - lat_min*60), 2)
    
    lon_str = seperator.join([str(x) for x in [lon_deg, lon_min, lon_sec]])
    if south: lon_str += 'S'
    else: lon_str += 'N'
    lat_str = seperator.join([str(x) for x in [lat_deg, lat_min, lat_sec]])
    if west: lat_str += 'W'
    else: lat_str += 'E'
    
    return (lon_str, lat_str)