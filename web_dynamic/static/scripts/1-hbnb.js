$(document).ready(function () {
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
});

