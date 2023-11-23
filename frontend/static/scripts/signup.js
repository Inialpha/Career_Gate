$(function () {
	$('.signupbutton').on('click', function () {
		let firstname = $('.form input[name="firstname"]').val()
		let lastname = $('.form input[name="lastname"]').val()
		let email = $('.form input[name="email"]').val()
		let password = $('.form input[name="password"]').val()
		const data = {"first_name": firstname, "last_name": lastname, "email": email, "password": password};

		$.ajax({
			url: "http://0.0.0.0:5001/api/v1/signup",
			data: JSON.stringify(data),
			contentType: "application/json",
			type: "POST",
			success: function (response) {
				if (response.status === "OK") {
					window.location = 'http://0.0.0.0:5000/login';
				} else if (response.status === "emailerror") {
					$('p.error').html("<h3>Email already in use</h3>");
				}

			},
			error: function (response) {
				alert(response.status);
			}
		});



	});
});
