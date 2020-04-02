import requests
import json

def getCoordinates(postCode):

    ## If the postcode is empty, return an empty string
    if postCode == '':
        return ''

    key = 'AuJ09npEnmthbBSxKu6teNImwt-6ZIn83affPp-nyUTAfXypqFl12jmF_SFV0IO6'

    url = 'http://dev.virtualearth.net/REST/v1/Locations?countryRegion=UK&postalCode={}&addressLine={}&maxResults=1&key={}'.format(
        postCode, '-', key
    )

    ## Get the location
    response = requests.get(url)
    results = response.json()

    ## If the location lookup has failed, return an empty location
    try:
        location = str(results['resourceSets'][0]['resources'][0]['point']['coordinates'][0]) + ', ' + \
            str(results['resourceSets'][0]['resources'][0]['point']['coordinates'][1])
    except:
        location = ''

    return location
