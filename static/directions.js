
var directionsService = new google.maps.DirectionsService();
var directionsDisplay = new google.maps.DirectionsRenderer();
var map;

// locations[i] corresponds to markers[i]
// var snapData stores the map returned from snap service
// with origin, market obj, stores array of objs
var markers = [];
var locations = [];
var listItems = [];

var snapData = {};
var myLocation = {};

bDisplayDirections = false;
// Notes about locations
// 1 "market" and X "stores"
// market has name and fulltext
// store has store_name

// Initialize the map, add in the location markers
// and add listeners for hover events
function initialize() {

	// Initialize map
	var options = {
		zoom: 13,	// ??
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		center: new google.maps.LatLng(39.952377, -75.16362) // Arbitrary center
	};

	map = new google.maps.Map(
		document.getElementById("map"),
		options
	);
	
	// Setup "back to locations" button
	$('#locationsButton').attr('disabled','disabled');
     $('#locationsButton').click(function(){
        reInit();
     });
	
	snapData = jQuery.parseJSON(snapDataString);
	myLocation = jQuery.parseJSON(myOrigin).origin;
	
	var center = new google.maps.LatLng(myLocation.latitude, myLocation.longitude);		
	map.setCenter(center);
	/*var marker = new google.maps.Marker({
		map: map,
		position: center,
		title: "My Location",
		icon: "http://image.spreadshirt.com/image-server/v1/designs/12108165,width=190,height=190/Google-Map-marker.png"
	});*/
	
	var list = document.getElementById('snaplist');
	
	var li = document.createElement('li');
	var text = document.createTextNode(snapData.market.fulltext);
	li.innerHTML = '<a href="#"/>'+snapData.market.fulltext;
	//li.appendChild(text);
	list.appendChild(li);
	
	li.onclick = function() {
		var location = locations[0];
		getDirections(myLocation.latitude, myLocation.longitude, snapData.market.latitude, snapData.market.longitude);
	};
	
	li.onmouseover = function() {
		// Add bounce animation
		animateLocationMarker(0);
	};
	
	li.onmouseout = function() {
		// Remove the bounce animation
		removeAnimation(0);
	};
	
	listItems.push(li);
	
	// Cache the list items + set up event listeners
	$.each(snapData.stores, function(index, store) {
	
		var item = document.createElement('li');
		item.innerHTML = '<a href="#"/>'+store.store_name;
		item.appendChild(text);
	
		item.onclick = function() {
				return (function(index, store) {
				// Load up the directions
				var location = locations[index+1];
				getDirections(myLocation.latitude, myLocation.longitude, store.latitude, store.longitude);
			})(index, store);
		};

		item.onmouseover = function() {
			// Add bounce animation
			(function(index) {
				animateLocationMarker(index+1);
			})(index);
		};
		
		item.onmouseout = function() {
			// Remove the bounce animation
			(function(index) {
				removeAnimation(index+1);
			})(index);
		};
		
		list.appendChild(item);
		listItems.push(item);
	
	});

	// Get our locations to create markers
	locations = []; 

	var stores = snapData.stores;
	
	if (snapData.market != null) locations.push(snapData.market);
	locations = locations.concat(stores);

	$.each(locations, function(index, location) {
	
		(function(index, location) {
			var marker = new google.maps.Marker({
				map: map,
				position: new google.maps.LatLng(location.latitude, location.longitude),
				title: location.store_name || location.fulltext || location.name
			});

			google.maps.event.addListener(marker, "mouseover", function() {
				// Highlight one of the listings below the map
				$(listItems[index]).addClass("highlight");
			});
	
			google.maps.event.addListener(marker, "mouseout", function() {
				// Un-highlight the listing
				$(listItems[index]).removeClass("highlight");
			});
			
			google.maps.event.addListener(marker, "click", function() {
				var location = locations[index];
				getDirections(myLocation.latitude, myLocation.longitude, location.latitude, location.longitude);
			});

			markers.push(marker);
		}) (index, location);
	});
}

// Called when user moves from directions back to locations map
// Removes the current directions from the map and adds back the
// location markers.
function reInit() {
	
	// Remove any directions
	directionsDisplay.setMap(null);
	
	// Add back all of the markers
	addMarkers();
	
	// Center back on my location
	var center = new google.maps.LatLng(myLocation.latitude, myLocation.longitude);		
	map.setCenter(center);
	map.setZoom(13);
}

// When user clicks on map or location item, centers the map 
// and fetches/displays the directions on a clean map 
function getDirections(oLat, oLon, dLat, dLon) {

	var origin = new google.maps.LatLng(oLat, oLon);
	var destination = new google.maps.LatLng(dLat, dLon);

	var seconds = new Date().getTime() / 1000;

	var request = {
		origin: origin,
		destination: destination,
		travelMode: google.maps.DirectionsTravelMode.TRANSIT,
		transitOptions : { departureTime : new Date() }
	};

	directionsService.route(request, function(response, status) {
		
		if (status == google.maps.DirectionsStatus.OK) {
			
			// Remove current markers
			removeMarkers();
			
			// Modify the map to center it and display the directions
			// * Approximating the center by just taking the average
			// of the two locations *
			var newLat =  (oLat+dLon)/2.0;
			var newLon =  (dLat+dLon)/2.0;
			var center = new google.maps.LatLng(newLat, newLon);
			
			// Remove any previous directions
			directionsDisplay.setMap(null);
			
			map.setCenter(center);
			directionsDisplay.setMap(map);
			directionsDisplay.setDirections(response);

			// Enable the "back to locations" button
			bDisplayDirections = true;
			$('#locationsButton').removeAttr('disabled');
		}
		else {
			// TODO Display error or something?
		}
	});
}

// When the user hovers over a location item, 
// animate the map marker
function animateLocationMarker(locationIndex) {

	// Get the marker
	var marker = markers[locationIndex];
	animateMarker(marker);
}

function animateMarker(marker) {
	marker.setAnimation(google.maps.Animation.BOUNCE);
}

function removeAnimation(index) {
	markers[index].setAnimation(null);
}

// Removes markers from the map,
// but saves them to add back on later
function removeMarkers() {
	$.each(markers, function(index, marker) {
		marker.setMap(null);
	});
}

// Add all of the markers to the map (if not already added)
function addMarkers() {
	$.each(markers, function(index, marker) {
		marker.setMap(map);
	});
}

google.maps.event.addDomListener(window, 'load', initialize);

