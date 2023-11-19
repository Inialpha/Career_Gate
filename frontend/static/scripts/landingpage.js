$(function () {
	$('.startbutton').on('click', function (item) {
		alert('click');
		item.preventDefault();
		window.location = 'http://0.0.0.0:5000/signup';
	});
});
