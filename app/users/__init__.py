from flask import Blueprint

from app.utils import update_user_status

users_bp = Blueprint('users', __name__)


@users_bp.before_request
def update_status():
    update_user_status()


from app.users import routes, models
