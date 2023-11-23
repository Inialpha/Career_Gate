$(function () {
	$('.startbutton').on('click', function (item) {
		item.preventDefault();
		window.location = 'http://0.0.0.0:5000/signup';
	});
});
