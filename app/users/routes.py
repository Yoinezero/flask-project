from flask import render_template, flash, redirect, url_for, request, current_app as app
from flask_login import current_user, login_required

from app import db
from app.users import users_bp
from app.users.forms import EditProfileForm
from app.users.models import Post, User


@users_bp.route('/user/<string:username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )
    next_url = url_for('users.user_page', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('users.user_page', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('users/user.jinja2',
                           user=user,
                           posts=posts.items,
                           next_url=next_url,
                           prev_url=prev_url)


@users_bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Changes have been saved.')
        return redirect(url_for('users.user_page', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('users/edit_profile.jinja2', title='Edit Profile', form=form)


@users_bp.route('/follow/<string:username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(f'User {username} not found.')
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('users.user_page', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(f'You are following {username}!')
    return redirect(url_for('users.user_page', username=username))


@users_bp.route('/unfollow/<string:username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(f'User {username} not found.')
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('users.user_page', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(f'You are not following {username}.')
    return redirect(url_for('users.user_page', username=username))
