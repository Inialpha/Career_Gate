/*$(function () {
	alert("homepage");
	$('.createresume').on('click' function (item) {
		item.preventDefault();
		window.location = 'http://0.0.0.0:5000/createresume';
	});

	$('.bookinterview').on('click' function (item) {
		item.preventDefault();
		window.location = 'http://0.0.0.0:5000/bookinterview';
	});


	$.ajax({
		url: "http://0.0.0.0:5001/api/v1/homepage",
		contentType: "application/json",
		type: "GET",
		success: function (response) {
			if (response.status === "OK") {
				window.location = 'http://0.0.0.0:5000/homepage';
			} else if (response.status === "emailerror") {
				$('p.error').html("<h3>Email already in use</h3>");
			}

		},
		error: function (response) {
			alert("failhom");
		}
	});


});*/
