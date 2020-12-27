 // This example displays a marker at the center of india.
 // When the user mouseover the marker, an info window opens.

 function initMap() {
     var india = { lat: 23.0201818, lng: 72.4396589 };
     var map = new google.maps.Map(document.getElementById('map'), {
         zoom: 6,
         center: india
     });

     var contentString = '<div class="info_content">' +
         '<h3 class="info_location_name">Ahmedabad</h3>' +
         '<p class="info_location_text">758, Shady Pines Drive Martinsville, Ahmedabad</p>' +
         '<p class="info_location_call"><span><i class="fa fa-phone"></i></span>(800) 123-4567</p>' +
         '<a href="#" class="btn-link">View Location</a>' +


         '</div>';

     var infowindow = new google.maps.InfoWindow({
         content: contentString
     });

     var marker = new google.maps.Marker({
         position: india,
         map: map,
         title: 'India (Ahmedabad)'
     });
     marker.addListener('mouseover', function() {
         infowindow.open(map, marker);
     });
     // show map, open infoBox 
     google.maps.event.addListenerOnce(map, 'tilesloaded', function() {
         infowindow.open(map, marker);
     });

 }