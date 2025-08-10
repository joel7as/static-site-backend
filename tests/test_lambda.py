import json
import sys
import os
import pytest

# Add src folder to path to import lambdacode.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import lambdacode  # your Lambda function file without .py

def test_lambda_handler():
    # Mock event and context (empty for now)
    event = {}
    context = None

    # Call the Lambda handler
    response = lambdacode.lambda_handler(event, context)

    # Response should be a dict with statusCode and body
    assert isinstance(response, dict)
    assert "statusCode" in response
    assert response["statusCode"] == 200

    # Body should be a JSON string with visits key
    body = json.loads(response["body"])
    assert "visits" in body
    assert isinstance(body["visits"], int) or isinstance(body["visits"], float)
