from flask import Blueprint

alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/getalu',methods=['GET'])
def getalu():
    return {'key':'Alumnos'}

