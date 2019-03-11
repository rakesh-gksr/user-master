# project/api/friends.py


from flask import Blueprint, jsonify
from project.api.models.users import User
from project.api.models.friends import friendships, bestFriends


friends_blueprint = Blueprint('friends', __name__)


@friends_blueprint.route('/friendList<int:page>', methods=['GET', 'POST'])
@friends_blueprint.route('/friends', methods=['GET', 'POST'])
def get_freinds(page=1):

    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'User does not exist'
    }
    try:
        user = None
        userList= None
        # userList = User.query.join(friendships, User.id == friendships.user_id).add_columns(User.userId, User.name,
        #                                                                                     User.email,
        #                                                                                     User).filter(
        #     User.id == friendships.friend_id).filter(friendships.user_id == 1).paginate(page, 1, False)
        # user = User.query.filter_by(id=int(1)).first()
        if not user:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                  'username': userList
                }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404