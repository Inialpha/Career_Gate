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
});
