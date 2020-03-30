import requests
import json

def getCoordinates(postCode):

    if postCode == '':
        return ''

    

    key = 'AuJ09npEnmthbBSxKu6teNImwt-6ZIn83affPp-nyUTAfXypqFl12jmF_SFV0IO6'

    url = 'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=UK&postalCode={}&addressLine={}&maxResults=1&key={}'.format(
        postCode, '-', key
    )

    response = requests.get(url)

    results = response.json()

    try:
        location = str(results['resourceSets'][0]['resources'][0]['point']['coordinates'][0]) + ', ' + \
            str(results['resourceSets'][0]['resources'][0]['point']['coordinates'][1])
    except:
        location = ''

    return location
