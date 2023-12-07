/*$(function () {
  $('#resume').submit(function (event) {
    event.preventDefault();

    const link = $('#resume textarea[name="link"]').val()
    const user_id = $('#resume input[name="user_id"]').val()

    const data = {'user_id': user_id, 'content': link}

    $.ajax({
      url: "http://0.0.0.0:5001/api/v1/resume",
      type: "POST",
      data: JSON.stringify(data),
      contentType: 'application/json',
      success: function (response) {
	alert("Request successful");
	window.location = '/homepage';
      },
      error: function (error) {
	alert('fail');
      }
    });
  });
  function viewresume () {
    alert("enter");
    const user_id = $('input[name="user_id"]').val()
    $.ajax({
      url: `http://0.0.0.0:5001/api/v1/resume/${user_id}`,
      type: "GET",
      contentType: 'application/json',
      success: function (response) {
	alert("ALL Request");
      },
      error: function (error) {
	alert('fail');
      }
    });
  }



});
*/

