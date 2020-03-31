
function GetMap(){

    var pinData; // = {'centre':[55.8554403, -4.3024976], 'posts':[ {'location':[55.8554403, -4.3024976], 'title':'Glasgow'}, ]}

    var postIDs = $('#map').attr('data-postids');
    var centre = $('#map').attr('data-centre');
    var zoom = $('#map').attr('data-zoom');

    $.get('/traffic/map', { 'postIDs':postIDs, 'centre':centre}, function(data) {
        pinData = JSON.parse(data);
        var map = new Microsoft.Maps.Map('#map', { 
            credentials: 'AuJ09npEnmthbBSxKu6teNImwt-6ZIn83affPp-nyUTAfXypqFl12jmF_SFV0IO6',
            center: new Microsoft.Maps.Location(pinData['centre'][0], pinData['centre'][1]),
            mapTypeId: Microsoft.Maps.MapTypeId.road,
            zoom: zoom,
        });

        for (var i = 0; i < pinData['posts'].length; i++) {
            var location = new Microsoft.Maps.Location( pinData['posts'][i]['location'][0], pinData['posts'][i]['location'][1] );
            var pin = new Microsoft.Maps.Pushpin( location, {
                title: pinData['posts'][i]['title'],
                });

            map.entities.push(pin);
        }

    });

}
