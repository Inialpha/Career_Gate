from models.views import app_views
from flask import render_template, redirect, flash, url_for, request, jsonify
import requests
from flask_login import current_user, login_required
import models

@app_views.route('/calendly', methods=['GET', 'POST'], strict_slashes=True)
def calendly():
    """Every users homepage"""

    data = request.json
    payload = data.get('payload', {})
    email = payload.get('email')
    scheduled_event = payload.get('scheduled_event', {})
    """get event location details"""
    location = scheduled_event.get('location', {})
    meeting_link = location.get('join_url')
    password = location.get('data').get('password')
    
    """ rettieve the time the meeting was created """
    created_at = scheduled_event.get('created_at', "").rstrip('Z')
    
    """ get the user base on email """
    user = models.storage.get_by_email(email)
    if user is None:
        return jsonify({'status': 'Failed'})

    """ retrieve other fields in the form """
    questions_and_answers = payload.get('questions_and_answers', [])
    resume_link = questions_and_answers[0].get('answer')
    application_link = questions_and_answers[1].get('answer')

    """ retrieve meeting uuid from its uri """
    interview_id = scheduled_event.get("uri", "").split('/')[-1]
    user_id = user.id

    """ construct the meeting detaials """
    params = {'user_id': user_id,
            'created_at': created_at,
            'updated_at': created_at,
            'id': interview_id,
            'resume_link': resume_link,
            'application_link': application_link,
            'meeting_link': meeting_link,
            'meeting_password': password
            }

    """ create an Interview instance """
    from models.interview import Interview

    interview = Interview(**params)
    interview.save()

    return jsonify({'status': 'Ok'})

@app_views.route('/calendly-success', methods=['GET', 'POST'], strict_slashes=True)
def calendly_success():
    """ the route to follow when a meeting is scheduled successfully """


    return render_template('calendly_success.html')
