/*$(function () {
  const resume_id = $('input[name="resume"]').val()
  $.ajax({
    url: `http://0.0.0.0:5001/api/v1/resume/${resume_id}`,
    type: "GET",
    contentType: 'application/json',
    success: function (value) {
	const datestring = value.created_at;
	const date = new Date(datestring);
	const options = { year: 'numeric', month: 'long', day: 'numeric'};
	const newdate = date.toLocaleDateString('en-US', options);
	$('.resume').append(`
	  <p>This request was made on: ${newdate}</p>
	  <h3><b>Resume</b>:   <a href="${value.content}">Link</a></h3>
	  <h3>Ststus:   ${value.details}</h3>`
  );
    }
  });
});*/
