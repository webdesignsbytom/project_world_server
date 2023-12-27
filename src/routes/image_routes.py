import os
import uuid
from flask import Blueprint, request
from controllers.image_controller import save_image_metadata
from utilities.response_util import sendDataResponse, sendMessageResponse

image_blueprint = Blueprint('image_blueprint', __name__)

# Image upload route
@image_blueprint.route('/upload-image/<user_id>', methods=['POST'])
def upload_image_route(user_id):
    try:
        if 'file' not in request.files:
            return sendMessageResponse('No file part', 400)
        
        file = request.files['file']
        if file.filename == '':
            return sendMessageResponse('No selected file', 400)

        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            if save_image_metadata(user_id, file_path):
                return sendDataResponse({'message': 'Image uploaded successfully'}, 200)
            else:
                return sendMessageResponse('Failed to save image metadata', 500)
    except Exception as e:
        return sendMessageResponse(str(e), 500)
