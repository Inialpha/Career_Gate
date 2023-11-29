#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models.interview import Interview
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/interviews', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_interview():
    """
    Retrieves the list of all resume objects

    """
    all_resume = storage.all(Resume).values()
    list_review = []
    for review in all_review:
        list_review.append(review.to_dict())
    return jsonify(list_review)


@app_views.route('/interviews/<interview_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_interviews(interview_id):
    """ Retrieves an interviews """
    interview = storage.get(Interview, interview_id)
    if not interview:
        abort(404)

    return jsonify(interview.to_dict())


@app_views.route('/interviews/<interview_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_interview(interview_id):
    """
    Deletes a interview Object
    """

    interview = storage.get(Interview, interview_id)

    if not interview:
        abort(404)

    storage.delete(interview)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/interviews', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_interview():
    """
    Creates a interview
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    if 'resume' not in data:
        abort(400, description="Missing content")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")

    instance = Resume(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/resume/<resume_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_interview(resume_id):
    """
    Updates a resume
    """
    resume = storage.get(Resume, resume_id)

    if not resume:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
