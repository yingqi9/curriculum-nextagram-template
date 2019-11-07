from flask import Blueprint, render_template


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')

#users/new
@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')

#users/
@users_blueprint.route('/', methods=['POST'])
def create_users():
    pass

@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
