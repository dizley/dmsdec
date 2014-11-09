'''
Created on Nov 6, 2014

@author: James Disley
'''

import re

def dms2dec(location):
    lon, lat = location[0], location[1]
    
    numbers = re.compile(r"(\d+\.?\d*)")
    letter = re.compile(r"([A-Z])$")
    
    lon_deg, lon_min, lon_sec = numbers.findall(lon)
    lon_direction = letter.search(lon).group(0)
    lat_deg, lat_min, lat_sec = numbers.findall(lat)
    lat_direction = letter.search(lat).group(0)
    
    #print(lon_direction, lat_direction)
    
    lon_dec = float(lon_deg) + float(lon_min)/60 + float(lon_sec)/3600
    lat_dec = float(lat_deg) + float(lat_min)/60 + float(lat_sec)/3600
    
    if(lon_direction == 'S'):
        lon_dec = lon_dec*-1
    if(lat_direction == 'W'):
        lat_dec = lat_dec*-1
    
    return (lon_dec, lat_dec)

def dec2dms():
    pass