from views import app_views
from flask import render_template, session, redirect
import requests


@app_views.route('/createresume', methods=['GET'], strict_slashes=True)
def createresume():
    """create a resume"""
    user = session.get('user')
    if user:
        return render_template('createresume.html', user=user);
    return redirect('/login')

@app_views.route('/viewresume', methods=['GET'], strict_slashes=True)
def viewresume():
    """route for viewing previous interview request"""
    user = session.get('user')
    if user is None:
        return redirect("/")

    return render_template('viewresume.html', user=user)

@app_views.route('/resume/<id>', methods=['GET'], strict_slashes=True)
def resumes(id):
    """view a resume"""
    user = session.get('user')
    if user:
        return render_template('resume_details.html', id=id)
    return ('/')

