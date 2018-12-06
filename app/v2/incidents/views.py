from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import IncidentsModel



class RedFlags(Resource, IncidentsModel):
	

	def __init__(self):
		self.db = IncidentsModel()

	def post(self):
		data=request.get_json()
		createdBy=data['createdBy']
		typee=data['type']
		location=data['location']
		status=data['status']
		images=data['images']
		videos=data['videos']
		
		

		resp = self.db.save(createdBy, typee, location, status, images, videos)

		return make_response(jsonify(
			{
			"Message" : "RedFlag has been created",
			"status" : 201
			}), 201)

	def get(self):
		resp = self.db.getallincidents()

		return make_response(jsonify(
			{
			"RedFlag" : resp,
			"status" : 200
			}), 200)

	

class RedFlag(Resource, IncidentsModel):
	"""docstring for RedFlag"""
	def __init__(self):
		self.db = IncidentsModel()

	def get(self, num):
		resp = self.db.getspecificincident(num)

		return make_response(jsonify(
			{
			"RedFlag" : resp,
			"status" : 201
			}), 201)


		
	def put(self, num):

		req_data = request.get_json()

		update = req_data.items()

		for field, data in update:
			resp = self.db.update_item(field, data, num)
			msg = "{} updated successfully".format(resp)

			return make_response(jsonify(
				{
				"Message" : msg,
				"status" : 200
				}), 200)

	def delete(self, num):
			resp = self.db.destroy(num)
			msg = "Id {} deleted successfully".format(resp)

			return make_response(jsonify(
				{
				"Message" : msg,
				"status" : 200
				}), 200)

		
