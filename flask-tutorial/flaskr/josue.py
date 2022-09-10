from flask import (
    Blueprint, jsonify
)

bp = Blueprint('josue',__name__)

@bp.route('/aa',methods=('GET','POST'))
def aa():
    a={"asd":"ddd"}
    return jsonify(a)
