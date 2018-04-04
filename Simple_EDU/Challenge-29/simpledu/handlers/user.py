from flask import Blueprint, render_template
from simpledu.models import User
#通过username查询数据库获得User对象，get_or_404, 获得对象后传入user.html
user = Blueprint('user', __name__, url_prefix='/user')

@user.route('/<username>')
def user_index(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

