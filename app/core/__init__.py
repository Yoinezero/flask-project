from flask import Blueprint

from app.utils import update_user_status

core_bp = Blueprint('main', __name__)


@core_bp.before_request
def update_status():
    update_user_status()


from app.core import routes
