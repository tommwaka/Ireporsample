from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import UsersModel

def _validator(user):
	error = False
	for key, value in user.items():
		if not value:
			error =  make_response(jsonify({
					"Error" : "Bad Request, {} is lacking".format(key)
					}), 403)
			return error

		if key == "username" or key =="password":
			if len(value) < 5:
				error =  make_response(jsonify({
					"Error" : "Bad Request, {} value is too short".format(key)
					}), 403)
			else:
				if len(value) > 20:
					error =  make_response(jsonify({
						"Error" : "Bad Request, {} value is too long".format(key)
						}), 403)
			return error
			

			
class UserSignup(Resource, UsersModel):
	

	def __init__(self):
		self.db = UsersModel()

	def post(self):
		data=request.get_json()

		user = dict(
			firstname=data['firstname'],
			lastname=data['lastname'],
			email=data['email'],
			username=data['username'],
			password=data['password']
		)

		valid = _validator(user)

		if valid == False:
			
			resp = self.db.save(user['firstname'], user['lastname'], user['email'], user['username'], user['password'])

			return make_response(jsonify(
				{
				"Message" : "New User has been created",
				"status" : 201
				}), 201)
		else:
			return valid

class UserSignin(Resource, UsersModel):
	

	def __init__(self):
		self.db = UsersModel()

	def post(self):
		data=request.get_json()
		username=data['username']
		password=data['password']
		
		record = self.db.user_exists(username)
		if not record:
			return "No such user"
		username, passworddb = record
		if password == passworddb:
			return "Logged in successfully"
		else:
			return "username/password does not match"
