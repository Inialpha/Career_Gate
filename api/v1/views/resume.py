#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """
from models.user import User
from models.resume import Resume
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/resume', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/all_users.yml')
def get_resumes():
    """
    Retrieves the list of all resume objects

    """
    all_resume = storage.all(Resume).values()
    list_resume = []
    for resume in all_resume:
        list_resume.append(resume.to_dict())
    return jsonify(list_resume)


@app_views.route('/users/<user_id>/resumes', methods=['GET'], strict_slashes=False)
def get_user_resumes(user_id):
    """ Retrieves a user resumes """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    resumes = []
    for resume in user.resume:
        resumes.append(resume.to_dict())
    return jsonify(resumes)

@app_views.route('/resume/<resume_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_resume(resume_id):
    """ Retrieves an resume """
    resume = storage.get(Resume, resume_id)
    if not resume:
        abort(404)

    return jsonify(resume.to_dict())


@app_views.route('/resumes/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def delete_resume(user_id):
    """
    Deletes a user Object
    """

    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/resume', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_resume():
    """
    Creates a resume
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    if 'content' not in data:
        abort(400, description="Missing content")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    instance = Resume(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/resume/<resume_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_resume(resume_id):
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
