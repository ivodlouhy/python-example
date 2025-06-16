import json
import os
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_xray_sdk.core import patch_all as xray_patch_all

tracer = Tracer()
logger = Logger(
    level="DEBUG"
)
xray_patch_all()

def lambda_handler(event, context: LambdaContext):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'hello': 'world',
            'message': os.getenv('EXAMPLE_PARAMETER'),
            'event': event
        })
    }




