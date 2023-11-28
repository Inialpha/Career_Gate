from models.views import app_views
from flask import render_template, request
from flask_login import current_user, login_required
import models

@app_views.route('/bookinterview', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def bookinterview():
    """create a resume"""
    user = current_user
    if request.method == 'POST':
        resume_link = request.form['resume_link']
        application_link = request.form['application_link']
        user_id = current_user.id
        data = {'resume_link': resume_link, 'application_link': application_link, 'user_id': user_id}
        from models.interview import Interview
        interview = Interview(**data)
        interview.save()
        return ("Booking successful")
    return render_template('bookinterview.html', user=user)

@app_views.route('/interviews', methods=['GET'], strict_slashes=True)
@login_required
def interviews():
    """route for viewing previous interview request"""
    user = current_user
    if user is None:
        return redirect("/")
    interview_list = []
    if user.user_type == 'client':
        for interview in user.interviews:
            interview_list.append(interview)
            return render_template('interviews.html', interviews=interview_list)
    else:
        from models.interview import Interview
        interviews = models.storage.all(Interview).values()
        return render_template('interviews.html', interviews=interviews)

@app_views.route('/interview_details<id>', methods=['GET'], strict_slashes=True)
def interview_details(id):
    """ get details of interview """
    from models.interview import Interview
    interview = models.storage.get(Interview, id).values()
    return render_template('interview_details.html', interview=interview)
