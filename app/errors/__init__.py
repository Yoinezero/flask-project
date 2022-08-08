from flask import Blueprint

from app.utils import update_user_status

errors_bp = Blueprint('errors', __name__)


@errors_bp.before_request
def update_status():
    update_user_status()


from app.errors import handlers
