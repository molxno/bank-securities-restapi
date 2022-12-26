# Constructor y catch de api
import logging
import traceback
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def build_error_response(e):
    logger.info('#START build_error_response')
    
    logger.error(f'Ocurrió un error: {str(e)}')
    dict_error = {
        'message': str(e).replace('\'',''),
        "traceback": str(traceback.format_exc())
    }

    logger.info('#EXIT build_error_response')
    return {

        "statusCode":400,
        "body": json.dumps(dict_error),
        "headers": {
            "content-type":"application/json"
        },
        "isBase64Encoded": False
    }