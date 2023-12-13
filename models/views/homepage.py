from models.views import app_views
from flask import render_template, redirect, flash, url_for
import requests
from flask_login import current_user, login_required
import models

@app_views.route('/homepage', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def homepage():
    """Every users homepage"""
    user = current_user
    if user.user_type == "admin":
        from models.interview import Interview
        from models.resume import Resume

        resumes = models.storage.all(Resume).values()
        interviews = models.storage.all(Interview).values()
        graduate_resume = []
        student_resume = []

        for resume in resumes:
            if resume.resume_type == "graduate":
                graduate_resume.append(resume)
            elif resume.resume_type == "student":
                student_resume.append(resume)

        return render_template('admindashboard.html', user=user, graduate_resume=graduate_resume, student_resume=student_resume, interviews=interviews)
    return render_template('userdashboard.html', user=user);
