from flask import Blueprint

core_bp = Blueprint('main', __name__)

from app.core import routes
