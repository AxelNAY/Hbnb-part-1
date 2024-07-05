"""
This module contains the routes for the users endpoints.
"""

from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user['email']).first()
    return jsonify(user.to_dict()), 200

@bp.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if not current_user['is_admin']:
        return jsonify({"msg": "Admin access required"}), 403
    return jsonify({"msg": "Welcome admin"}), 200
