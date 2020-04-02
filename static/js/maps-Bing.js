// Function that loads the map
function GetMap(){

    var pinData; 

    // Get the data needed to display the map from the html
    var postIDs = $('#map').attr('data-postids');
    var centre = $('#map').attr('data-centre');
    var zoom = parseInt( $('#map').attr('data-zoom') );

    // Get the data from the server
    $.get('/traffic/map', { 'postIDs':postIDs, 'centre':centre}, function(data) {
        // Parse the data sent back from the server
        pinData = JSON.parse(data);

        // Display the main map
        var map = new Microsoft.Maps.Map('#map', { 
            credentials: 'AuJ09npEnmthbBSxKu6teNImwt-6ZIn83affPp-nyUTAfXypqFl12jmF_SFV0IO6',
            center: new Microsoft.Maps.Location(pinData['centre'][0], pinData['centre'][1]),
            mapTypeId: Microsoft.Maps.MapTypeId.road,
            zoom: zoom,
        });

        // Add all of the pins (if any)
        for (var i = 0; i < pinData['posts'].length; i++) {
            var location = new Microsoft.Maps.Location( pinData['posts'][i]['location'][0], pinData['posts'][i]['location'][1] );
            var pin = new Microsoft.Maps.Pushpin( location, {
                title: pinData['posts'][i]['title'],
                });

            map.entities.push(pin);
        }

    });

}
