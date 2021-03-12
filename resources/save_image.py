
from flask_restful import Resource
from flask import request
from flask_uploads import UploadNotAllowed
from flask_jwt_extended import jwt_required, get_jwt_identity

from libs import image_helper


class ImageUpload(Resource):
    @jwt_required
    def post(self):
        data = request.files["image"]
        user_id = get_jwt_identity()
        folder = "user_%s"%(user_id)
        try:
            image_path=image_helper.save_image(data, folder, None)

            basename=image_helper.get_basename(image_path)
            return {"message":"image uploaded"}, 201
        except UploadNotAllowed:
            return "illegal extension"
