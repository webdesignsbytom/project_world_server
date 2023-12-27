from flask import jsonify

STATUS_MESSAGES = {
  200: 'success',
  201: 'success',
  400: 'fail',
  401: 'fail',
  403: 'fail',
  404: 'fail',
  500: 'error',
}

EVENT_MESSAGES = {
    'badRequest': 'Bad Request',
    'notFound': 'Not Found',
    'missingUserIdentifier': 'Missing User identifier',
    'missingFields': 'Missing fields in request',
    'eventTag': 'Event database',
    'eventNotFound': 'Failed to find event',
    'createEventFail': 'Failed to create event',
    'messageTag': 'Message database',
    'messageNotFound': 'Failed to find message/s',
    'userMessagesNotFound': 'Failed to find user messages',
    'createMessageFail': 'Failed to create message',
    'markMessageViewedFailed': 'Failed to mark message as viewed',
    'notificationTag': 'Notification database',
    'notificationIdNotFound': 'Failed find notification/s',
    'userNotificationsNotFound': 'Failed to find user notifications',
    'createNotificationFail': 'Failed to create notification',
    'markNotificationViewedFailed': 'Failed to mark notification as viewed',
    'paletteTag': 'Palette database',
    'paletteNotFound': 'Failed to find palette/s',
    'createPaletteFail': 'Failed to create palette',
    'projectTag': 'Project database',
    'projectNotFound': 'Failed to find project/s',
    'createProjectFail': 'Failed to create project',
    'reviewsTag': 'Review database',
    'notFoundReview': 'Failed to find review/s',
    'userReviewsNotFound': 'Failed to find user reviews',
    'createReviewFail': 'Failed to create review',
    'markReviewViewedFailed': 'Failed to mark review as viewed',
    'userTag': 'User databased',
    'userNotFound': 'Failed to find user/s',
    'emailInUse': 'Email already in use',
    'emailNotFound': 'Email not found in database',
    'createUserFail': 'Failed to create new user',
    'passwordMatchError': 'Password match error for reset Password - New passwords do not match',
    'passwordResetError': 'Account record doesn\'t exist or has been reset already.',
    'verificationTag': 'Verification database',
    'verificationNotFound': 'Failed to find verification',
    'verificationNotFoundReturnMessage': 'Account record doesn\'t exist or has been verified already. Please sign up or log in.',
    'expiredLinkMessage': 'Links has expired, please sign up or log in and check your account',
    'invalidVerificationMessage': 'Invalid verification details passed. Check your inbox, or contact support',
}

RESPONSE_MESSAGES = {
  'ConfictEvent': 'Request conflicts with data on server',
  'DeactivatedUserEvent': 'The target user account has been deactivated',
  'ServerErrorEvent': 'Internal Server Error',
  'CreateEventError': 'Failed to create an event log',
  'NotFoundEvent': 'was not found',
  'NoPermissionEvent': 'You are not authorized to perform this action',
  'NoValidationEvent': 'Unable to verify user',
  'BadRequestEvent': 'Incorrect request syntax or malformed request',
  'MissingFieldEvent': 'Missing fields in body',
};

def sendDataResponse(payload, status_code):
    return jsonify({
        'status': STATUS_MESSAGES.get(status_code, 'Unknown Status'),
        'data': payload
    }), status_code

def sendMessageResponse(message, status_code):
    return jsonify({
        'status': STATUS_MESSAGES.get(status_code, 'Unknown Status'),
        'message': message
    }), status_code
