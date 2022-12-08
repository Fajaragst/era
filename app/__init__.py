from flask import Blueprint, jsonify

from app.api.product.routes import product_blueprint

from app.api.error.http import BadRequest, InternalServerError

api_v1 = Blueprint("api_v1", __name__)


#Handle HTTP Error
@api_v1.errorhandler(BadRequest)
def handle_bad_request(e):
  
    data = {
        "error" : "MISSING_PARAMETER",
        "message" : e.message,
        "data" : e.details
    }
    return jsonify(data), 400

#register blueprint
api_v1.register_blueprint(product_blueprint)

