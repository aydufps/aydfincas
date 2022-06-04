from flask import jsonify


def parsemodel(items):
    temp = []
    for item in items:
        temp.append(item.toJSON())
    return jsonify(temp)


def hasRequiredFields(form, requiredFields):
    for item in requiredFields:
        if form[item] == None:
            return False
    return True
