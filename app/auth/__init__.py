from flask import Blueprint

from app.utils import update_user_status

auth_bp = Blueprint('auth', __name__)


@auth_bp.before_request
def update_status():
    update_user_status()


from app.auth import routes
