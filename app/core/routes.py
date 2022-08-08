from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required

from app import db
from app.core import core_bp
from app.core.forms import PostForm
from app.users.models import Post





@core_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))

    current_page = request.args.get('page', 1, type=int)
    posts = current_user.get_actual_posts().paginate(
        current_page,
        current_app.config['POSTS_PER_PAGE'],
        False
    )

    next_url = url_for('main.index', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) if posts.has_prev else None

    return render_template('index.jinja2',
                           title='Blog',
                           form=form,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)


@core_bp.route('/explore')
@login_required
def explore():
    current_page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        current_page,
        current_app.config['POSTS_PER_PAGE'],
        False
    )

    next_url = url_for('main.explore', page=posts.next_num) if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num) if posts.has_prev else None

    return render_template('index.jinja2',
                           title='Explore',
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)
