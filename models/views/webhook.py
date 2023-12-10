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
    location = scheduled_event.get('location', {})
    created_at = scheduled_event.get('created_at', "").rstrip('Z')
    meeting_link = location.get('join_url')
    password = location.get('data').get('password')
    
    user = models.storage.get_by_email(email)
    if user is None:
        return jsonify({'status': 'Failed'})

    questions_and_answers = payload.get('questions_and_answers', [])
    #print(questions_and_answers)
    resume_link = questions_and_answers[0].get('answer')
    application_link = questions_and_answers[1].get('answer')
    interview_id = scheduled_event.get("uri", "").split('/')[-1]
    print(interview_id)
    #print(resume_link)
    #print(application_link)
    user_id = user.id
    params = {'user_id': user_id,
            'created_at': created_at,
            'updated_at': created_at,
            'id': interview_id,
            'resume_link': resume_link,
            'application_link': application_link,
            'meeting_link': meeting_link,
            'meeting_password': password
            }
    from models.interview import Interview

    interview = Interview(**params)
    print(interview)
    interview.save()
    #print('payload:', payload)
    #print('email:', email)
    #print('scheduled_event:', scheduled_event)
    #print('location:', location)
    print('meeting_link:', meeting_link)
    print('password:', password)
    print('created_at:', created_at)

    return jsonify({'status': 'Ok'})
    #user = current_user
    #return render_template('userdashboard.html', user=user);
