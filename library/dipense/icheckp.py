# -*- coding: utf-8 -*-
import os
import csv
import subprocess as sp
from termcolor import cprint
from termcolor import colored

from .structure import Filing
from .structure import tracer
from .structure import geoip


class ICHECKP(Filing):
    """This class handle ip address payloads"""
    def icheckp(self, i_num):
        try:
            g = geoip.ip(i_num)
            cty = g.city # ip address city
            stt = g.state # ip address state
            ctry = g.country # ip address country
            
            json_raw = g.raw
            time_zone = list(list(json_raw.items())[6])[1] # ip address timezone area
            d_longitude = list(list(json_raw.items())[4])[1].split(',')[1] # ip address longitude
            d_latitude = list(list(json_raw.items())[4])[1].split(',')[0] # ip address latitude
            d_location = list(list(json_raw.items())[4])[1] # ip address coordinate
            
            location = g.latlng # a list which include latitude and longitude
            
            # creating a base map, making the `min_zoom=0`,
            # overide the `zoom_start=13` from default which is `10` to `13`, and
            # overide the `max_zoom=70` from default which is `18` to `70`
            Tmap = tracer.Map(location=location, max_zoom=70, min_zoom=0, zoom_start=13)
            
            # A circle of a fixed size with radius specified in pixels.
            tracer.CircleMarker(
                location=location, radius=50, color='#3186cc', fill=True, fill_color='#3186cc').add_to(Tmap)
            tracer.Circle(
                radius=100, location=location, popup='The Waterfront', color='crimson', fill=False).add_to(Tmap)
            # making the icon to be `cloud`
            tracer.Marker(location, icon=tracer.Icon(icon='cloud')).add_to(Tmap)
            
            self.dir_tree() # make the dir tree
            sp.run('cd .dipense/maps && sudo touch map.html', shell=True)
            cwd = os.getcwd()

            os.chdir(os.path.join(cwd, '.dipense/maps'))
            os.system('sudo touch test.py')
            
            map_file_method = self.mapName(i_num)
            mapF = map_file_method[0]
            csv_from_mapF = map_file_method[1]
            
            html_map_file_cmd = 'sudo touch {}'.format(mapF)
            csv_map_file_cmd = 'sudo touch {}'.format(csv_from_mapF)
            
            os.system(html_map_file_cmd)
            os.system(csv_map_file_cmd)
            
            for i in os.listdir():
                sp.run(['sudo', 'chmod', '777', i])

            Tmap.save(mapF)
            cprint(os.getcwd(), 'magenta')
            
            dummy = """# this is a test module

# write with focus
"""

            with open('test.py', 'w') as f:
                f.write(dummy)
            fieldnames = [
                'City', 'State', 'Country', 'time_zone', 'd_longitude', 'd_latitude', 'd_location', 'location', 'Map']
            
            with open(csv_from_mapF, 'w') as csv_f:
                csv_writer = csv.writer(csv_f)
                csv_writer.writerow(fieldnames)
                csv_writer.writerow(
                    [cty, stt, ctry, time_zone, d_longitude, d_latitude, d_location, location, mapF])
                
            csv_loc = 'csv file is located in ' + os.path.realpath(csv_from_mapF)
            cprint(csv_loc, 'green')
            # cprint(csv_loc, 'green', attrs=['bold'])
            
            if self.autoOpenMap:
                import webbrowser
                webbrowser.get().open(os.path.realpath(mapF))
                openInfo = 'Soon to open ' + os.path.realpath(mapF)
                print(colored(openInfo, 'magenta', attrs=['reverse', 'blink']))
                
            context = {
                'cty': cty,
                'stt': stt,
                'ctry': ctry,
                'json_raw': json_raw,
                'time_zone': time_zone,
                'd_longitude': d_longitude,
                'd_latitude': d_latitude,
                'd_location': d_location,
                'location coordinate': location,
            }
        except:
            context = {
                'i_num': i_num,
            }

        from . import getout
        if g.raw == None:
            getout(colored(' => ', 'cyan'), colored('domain:', 'green'), i_num)
            getout(
                colored(' => ', 'cyan', attrs=['blink']), colored('status:', 'green'), colored('unauthorized', 'red', attrs=['blink']))
        else:
            for k, v in context.items():
                # if the value of the result is None the color should be red
                if v == None:
                    r = k + ':'
                    getout(
                        colored(' => ', 'cyan'), colored(r, 'green'), colored(v, 'red', attrs=['blink']))
                else:
                    # if the key is json_raw, it will print different and do for loof over the result list
                    if k == 'json_raw':
                        getout('\n', colored('=> ', 'cyan'), colored('json_raw', 'yellow'), ':')
                        for s in v.items():
                            getout('\t\t', colored(' --- ', 'green'), colored(s, 'yellow'))
                        getout()
                    else:
                        r = k + ':'
                        getout(colored(' => ', 'cyan'), colored(r, 'green'), v)
