from models.views import app_views
from flask import render_template, redirect, request, flash, url_for
from flask_login import current_user, login_required
import models


@app_views.route('/createresume', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def createresume():
    """create a resume"""
    user = current_user
    if request.method == 'POST':
        resume_link = request.form['link']
        user_id = current_user.id
        data = {'resume_link': resume_link, 'user_id': user_id}
        from models.resume import Resume
        resume = Resume(**data)
        resume.save()
        return ("Request Successful")

    return render_template('createresume.html', user=user);

@app_views.route('/resumes', methods=['GET'], strict_slashes=True)
@login_required
def viewresumes():
    """route for viewing previous interview request"""
    user = current_user
    if user is None:
        return redirect("/")
    resume_list = []
    if user.user_type == 'client':
        for resume in user.resumes:
            resume_list.append(resume)
        return render_template('viewresume.html', resumes=resume_list)
    else:
        from models.resume import Resume
        resumes = models.storage.all(Resume).values()
        return render_template('viewresume.html', resumes=resumes)

        


    return render_template('viewresume.html', user=user)

@app_views.route('/resume/<id>', methods=['GET'], strict_slashes=True)
@login_required
def resumes(id):
    """view a resume"""
    from models.resume import Resume
    resume = models.storage.get(Resume, id)
    return render_template('resume_details.html', resume=resume)


@app_views.route('/resumes/<id>', methods=['POST', 'PUT'], strict_slashes=True)
@login_required
def update_resume(id):
    """ update a resume """
    from models.resume import Resume
    resume = models.storage.get(Resume, id)
    review = request.form['content']
    resume.review = str(review)
    resume.status = "Reviewed"
    models.storage.save()
    print("\n\n\n thos")
    flash("Review is successfully added", category="success")
    return redirect(url_for('app_views.homepage'))

