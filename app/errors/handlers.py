from flask import render_template, current_app as app
from app import db
from app.errors import errors_bp


@errors_bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.jinja2'), 404


@errors_bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.jinja2'), 500
