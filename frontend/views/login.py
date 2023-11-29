from views import app_views
from flask import render_template, request, abort, session, redirect
import requests
#from ..models import storage

@app_views.route('/login', methods=['GET', "POST"], strict_slashes=True)
def login():

    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password']
        
        url = "http://0.0.0.0:5001/api/v1/login"
        headers = {'Content-Type': 'application/json'}
        data = {'email': email, 'password': password}
        res = requests.post(url, json=data, headers=headers)
        print(res)
        if res.status_code == 201:
            print(res.json())
            session['user'] = res.json()
            return redirect("/homepage")

        

    #    requests
    #    for user in users:
    #        if user.email == email:
    #            if user.password == md5(password.encode()).hexdigest():

    return render_template('login.html')
