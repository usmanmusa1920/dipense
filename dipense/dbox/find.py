# -*- coding: utf-8 -*-
import os
from time import ctime
from pathlib import Path
import folium
import geocoder
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dbox.models import IpPayloadRec
from .default import default


BASE_DIR = Path(__file__).resolve().parent.parent


class ICHECKP:
	@login_required
	def icheckp(request):
		i_num = request.GET.get('ip_num')
		amp = '&amp;'
		
		try:
			g = geocoder.ip(i_num)
			cty = g.city # ip address city
			stt = g.state # ip address state
			ctry = g.country # ip address country
			
			json_raw = g.raw
			time_zone = list(list(json_raw.items())[6])[1] # ip address timezone area
			d_longitude = list(list(json_raw.items())[4])[1].split(',')[1] # ip address longitude
			d_latitude = list(list(json_raw.items())[4])[1].split(',')[0] # ip address latitude
			d_location = list(list(json_raw.items())[4])[1] # ip address coordinate
			
			location = g.latlng # a list which include latitude and longitude
			
			"""
				>>> import geocoder
				>>> g = geocoder.ip('197.210.52.244')
				>>> cty = g.city
				>>> cty
				'Abuja'
				>>> stt = g.state
				>>> stt
				'FCT'
				>>> ctry = g.country
				>>> ctry
				'NG'
				
				>>> json_raw = g.raw
				>>> json_raw
				{'ip': '197.210.52.244', 'city': 'Abuja', 'region': 'FCT', 'country': 'NG', 'loc': '9.0579,7.4951', 'org': 'AS29465 MTN NIGERIA Communication limited', 'timezone': 'Africa/Lagos', 'readme': 'https://ipinfo.io/missingauth'}
				
				>>> time_zone = list(list(json_raw.items())[6])[1]
				>>> time_zone
				'Africa/Lagos'
				
				>>> d_longitude = list(list(json_raw.items())[4])[1].split(',')[1]
				>>> d_longitude
				'7.4951'
				>>> d_latitude = list(list(json_raw.items())[4])[1].split(',')[0]
				>>> d_latitude
				'9.0579'
				>>> d_location = list(list(json_raw.items())[4])[1]
				>>> d_location
				'9.0579,7.4951'
				
				>>> location = g.latlng
				>>> location
				[9.0579, 7.4951]
			"""
			
			# creating a base map, making the `min_zoom=0`,
			# overide the `zoom_start=13` from default which is `10` to `13`, and
			# overide the `max_zoom=70` from default which is `18` to `70`
			Tmap = folium.Map(location=location, max_zoom=70, min_zoom=0, zoom_start=13)
			
			# A circle of a fixed size with radius specified in pixels.
			folium.CircleMarker(location=location, radius=50, color='#3186cc', fill=True, fill_color='#3186cc').add_to(Tmap)
			
			folium.Circle(radius=100, location=location, popup='The Waterfront', color='crimson', fill=False).add_to(Tmap)
			
			# making the icon to be `cloud`
			folium.Marker(location, icon=folium.Icon(icon='cloud')).add_to(Tmap)
			
			"""
				We replace the dot '.' in an ip address with underscore '_'
				We also replace the spaces ' ' of the ctime with underscore '_', and
				also the colon ':' is replaced with underscore '_' too!
				
				ip address format: '255.255.255.255'
				ctime() format: 'Sun Jul 17 18:40:22 2022'
				
				`r1` look like this at the end:
					192_255_255_255_@_Wed_Nov__2_16:28:16_2022
			"""
			r1 = str(i_num.replace('.', '_')) + '_@_' + ctime().replace(' ', '_')
			
			"""
				`r2` look like this at the end:
					192_255_255_255_@_Wed_Nov__2_16_28_16_2022
			"""
			r2 = r1.replace(':', '_')

			# the map file name
			map_file = 'map_' + str(r2) + '.html'
			
			map_dir = str(BASE_DIR) + '/templates/maps' # OR:
			# map_dir = os.path.join(BASE_DIR, 'templates/maps')
			
			# absolute map file path
			map_path = os.path.join(map_dir, map_file)
			Tmap.save(map_path)
			
			"""
				here making a for loop in the given path directory,
				to find if a `map_file` didn't match our pattern
				it will delete it to avoid many duplicate of files.
				
				This means once a file is created, after one minute
				once new ip address is payloaded it will remove
				all others which are older than one minute
			"""
			for i in os.listdir(path=str(map_dir)):
				# if the file name contains ['map_', '_@_', '.html']
				if 'map_' in i and '_@_' in i and '.html' in i:
					"""
						assuming the file name is:
							`map_192_255_255_255_@_Wed_Nov__2_16_28_16_2022.html`
							
						and the current time is:
							`Sun Jul 17 18:40:22 2022`
							
							a = 'map_192_255_255_255_@_Wed_Nov__2_16_28_16_2022.html'
							>>> a[-15:-13]
							'28'
							>>> a[-12:-10]
							'16'
							
							b = 'Sun Jul 17 18:40:22 2022'
							>>> b[-10:-8]
							'40'
							>>> b[-7:-5]
							'22'
							
						it will only delete the file if:
							b[-10:-8] != a[-15:-13] and b[-7:-5] != a[-12:-10]  
						that mean after 1 minute
					"""
					if ctime()[-10:-8] != i[-15:-13] and ctime()[-7:-5] != i[-12:-10]:
						os.remove(os.path.join(map_dir, i))

			# saving the payloaded ip address into database
			history = IpPayloadRec(payload_ip=i_num)
			history.save()

			context = {
				'amp': amp,
				'r2': r2,
				'cty': cty,
				'stt': stt,
				'ctry': ctry,
				'time_zone': time_zone,
				'd_longitude': d_longitude,
				'd_latitude': d_latitude,
				'd_location': d_location,
				'default': default(),
			}
			# import webbrowser
			# webbrowser.get().open(os.path.realpath(map_path))
		except:
			context = {
				'i_num': i_num, # raw ip address
				'default': default(),
			}
		return render(request, 'pages/icheckp.html', context)
		
	@staticmethod
	@login_required
	def open_map(request, r2):
		map_file = 'map_' + str(r2) + '.html'
		return render(request, f'maps/{map_file}')
