import geocoder
import folium
from datetime import datetime
from django.shortcuts import render
from account.models import Message
from time import ctime
import os
import webbrowser


def icheckp(request):
  the_year = datetime.today().year
  i_num = request.GET.get('ip_num')
  msg = Message.objects.filter(is_read=False)
  
  try:
    g = geocoder.ip(i_num)
    cty = g.city
    stt = g.state
    ctry = g.country
    
    json_raw = g.raw
    time_zone = list(list(json_raw.items())[6])[1]
    d_longitude = list(list(json_raw.items())[4])[1].split(',')[1]
    d_latitude = list(list(json_raw.items())[4])[1].split(',')[0]
    d_location = list(list(json_raw.items())[4])[1]
    
    location = g.latlng

    map = folium.Map(location=location, zoom_start=10)
    folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
    folium.Marker(location).add_to(map)
    
    """
      NOTE:
      We replace the dot '.' in an ip address with underscore '_'
      We also replace the spaces ' ' of the ctime with underscore '_', and also the colon ':' is replaced with underscore '_'
      
      ctime() format: 'Sun Jul 17 18:40:22 2022'
    """
    
    # r1 = str(i_num.replace('.', '_')) + '_@_' + ctime().replace(' ', '_')
    # r = r1.replace(':', '_')
    # map_file = 'map_' + str(r) + '.html'
    # map.save(map_file)
    
    # for i in os.listdir():
    #   if os.path.isfile(i):
    #     if 'map_' in i and '_@_' in i and '.html' in i:
    #       if ctime()[-10:-8] != i[-15:-13] and ctime()[-7:-5] != i[-12:-10]:
    #         os.remove(i)
    
    context = {
      'msg': msg,
      # 'map_file': map_file,
      'cty': cty,
      'stt': stt,
      'ctry': ctry,
      'time_zone': time_zone,
      'd_longitude': d_longitude,
      'd_latitude': d_latitude,
      'd_location': d_location,
      'the_year': the_year
    }
    # webbrowser.get().open(os.path.realpath(map_file))
  except:
    context = {
      'msg': msg,
      'the_year': the_year
    }
  return render(request, 'icheckp.html', context)
