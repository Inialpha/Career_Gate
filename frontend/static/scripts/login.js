$(function () {

	$('form').submit(function (event) {
		event.preventDefault()
		let email = $('.form input[name="email"]').val()
		let password = $('.form input[name="password"]').val()
		const data = { "email": email, "password": password};

		$.ajax({
			url: "http://0.0.0.0:5001/api/v1/login",
			data: JSON.stringify(data),
			contentType: "application/json",
			type: "POST",
			success: function (response) {
				if (response.status === "OK") {
					window.location = "http://0.0.0.0:5000/homepage";
				} else if (response.status === "emailerror") {
					$('p.error').html("<h3>Email already in use</h3>");
				}

			},
			error: function (response) {
				alert("fail");
			}
		});



	});
});
