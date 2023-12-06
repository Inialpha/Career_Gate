/*$(function () {
  const user_id = $('input[name="user_id"]').val()
  $.ajax({
    url: `http://0.0.0.0:5001/api/v1/users/${user_id}/resumes`,
    type: "GET",
    contentType: 'application/json',
    success: function (response) {
      response.forEach((value)  => {
	const datestring = value.created_at;
	const date = new Date(datestring);

    const options = { year: 'numeric', month: 'long', day: 'numeric'};
	const newdate = date.toLocaleDateString('en-US', options);
	$('.list').append(`
	<li data-id="${value.id}">Created: ${newdate}<br>Ststus: ${value.details}</li>`
	);

      });
    },
    error: function (error) {
      alert('fail');
    }
  });

  $('.list').on('click', 'li', function () {
	  alert('click');
    const id = $(this).data('id');
    window.location = `/resume/${id}`;
  });
});*/
