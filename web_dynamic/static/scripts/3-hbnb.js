$(function () {
	let dict = {};
	$('input').on('change', function () {
		if ($(this).is(':checked')) {
			dict[$(this).data('id')] = $(this).data('name')
		} else {
			delete dict[$(this).data('id')]
		}
		let am = ''
		for (let i in dict) {
			am += dict[i];
			am += ', ';
		}
		$('div.amenities h4').text(am);

	});

	$.ajax({
	  type: 'GET',
	  url: 'http://0.0.0.0:5001/api/v1/status/',
	  dataType: 'json',
	  success: function (response) {
	    if (response.status === 'OK') {
	      $('div#api_status').addClass('available');
	    } else {
	      $('div#api_status').removeClass('available');
	    }
	  }
	});


	$.ajax({
	  type: 'POST',
	  url: 'http://0.0.0.0:5001/api/v1/places_search/',
	  dataType: 'json',
	  contentType: 'application/json',
	  data: JSON.stringify({}),
	  success: function (response) {
	    for (let i in response) {
	      let article = [
		'<article>',
		'<div class="title_box">',
		'<h2>' + response[i].name + '</h2>',
		'<div class="price_by_night">',
		response[i].price_by_night,
		'</div>',
		'</div>',
		'<div class="information">',
		'<div class="max_guest">' +  response[i].max_guest + 'Guests',
		'</div>',
		'<div class="number_rooms">' + response[i].number_rooms + 'Bedrooms',
		'</div>',
		'<div class="number_bathrooms">' + response[i].number_bathrooms + 'Bathroom',
		'</div>',
		'</div>',
		'<div class="user">',
		'<b>Owner:</b>' + response[i].user.first_name +  place.user.last_name,
		'</div>',
		'<div class="description">',
		response[i].description,
		'</div>',
		'</article>'
	      ];
	      $(article.join('')).appendTo('section.places');
	    }
	  },
	  error: function (xhr, status, error) {
	    console.log(error)
	  }

	});
});
