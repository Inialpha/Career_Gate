$(function () {
  alert("enter");

  $('.admin').submit(function (event) {
    event.preventDefault();
    const email = $('form input[name="email"]').val();
    const data = {'user_type': 'admin'};
    $.ajax({
      url: `http://0.0.0.0:5001/api/v1/users/${email}`,
      type: "PUT",
      data: JSON.stringify(data),
      contentType: 'application/json',
      success: function (response) {
	alert("Admin added");
      },
    error: function (error) {
      alert('fail');
    }
  });

  });
});
