from datetime import datetime

from flask_login import current_user

from app import db


def update_user_status():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
