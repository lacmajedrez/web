'''
Created on Dec 12, 2016

@author: uvilla
'''
import json
import urllib

#key = 'AIzaSyCnCjlxS5LUvP1jjXansnk1ymt-Liga2aQ'
key = 'AIzaSyBLuHKVMU8kxU5R2ykwEgGTdhuINg-3HUE'
versions = [('v1.3.0', 'https://goo.gl/NgJ887'),
            ('v1.2.0', 'https://goo.gl/OcvROZ'),
            ('v1.1.0', 'https://goo.gl/pDb10B'),
            ('v1.0.2', 'https://goo.gl/wMb18C'),
            ('v1.0.1', 'https://goo.gl/srnvsc'),
            ('v1.0.0', 'https://goo.gl/h7HUFJ')
           ]

request = 'https://www.googleapis.com/urlshortener/v1/url?shortUrl={0}&projection=FULL&key={1}'

print '{0:7} {1:9}'.format('version', 'downloads')
total_downloads = 0
for v in versions:
    filehandle = urllib.urlopen(request.format(v[1], key))
    data = json.load(filehandle)
    total_downloads += int(data['analytics']['allTime']['shortUrlClicks'])
    print '{0:7} {1:9}'.format(v[0], int(data['analytics']['allTime']['shortUrlClicks']))

print '{0:7} {1:9}'.format('all', total_downloads)
