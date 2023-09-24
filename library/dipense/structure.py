# -*- coding: utf-8 -*-
import geocoder as geoip
import folium as tracer
import subprocess as sp

from time import ctime


class Filing:
    """filiing class"""
    def __init__(self, autoOpenMap=False):
        self.autoOpenMap = autoOpenMap

    def dir_tree(self):
        """create a directory tree where file will reserved"""
        sp.run(['sudo', 'mkdir', '-p', '.dipense/maps'])

    annot = '''
This method return a list of two files names
(html and csv)
'''

    # def mapName(self, i_num):
    def mapName(self, i_num) -> annot:
        """Filing method of assigning map files names"""
        
        # """
        # replacing the dot '.' in an ip address with underscore '_'
        # also replace the spaces ' ' of the ctime with underscore '_', and
        # also the colon ':' is replaced with underscore '_' too!
        
        # ip address format (e.g): '192.255.255.255'
        # ctime() format (e.g): 'Wed Nov 2 16:28:16 2022'
        
        
        # `r1` look like this at the end:
        # 192_255_255_255_@_Wed_Nov__2_16:28:16_2022
        # """
        r1 = str(i_num.replace('.', '_')) + '_@_' + ctime().replace(' ', '_')
        
        # """
        # `r2` look like this at the end:
        #     192_255_255_255_@_Wed_Nov__2_16_28_16_2022
        # """
        r2 = r1.replace(':', '_')
        
        # the map file names (html & csv)
        map_file_html = 'map_' + str(r2) + '.html'
        map_file_csv = 'map_' + str(r2) + '.csv'
    
        return [map_file_html, map_file_csv]
    

def helper():
    note = r"""
    Type '<module>.py <subcommand> -h' for help on a specific subcommand.

    Available subcommands:

    [domain]
        payloadwho
        [flags]
                -d / --domain

    [ip address]
        payloadip
        [flags]
                -i / --ip
                
    [phone number]
        payloadnum
        [flags]
                -n / --number
"""
    return note
