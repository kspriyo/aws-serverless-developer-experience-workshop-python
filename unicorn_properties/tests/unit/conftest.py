# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import pytest
import boto3
import os
from moto import mock_dynamodb, mock_events


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope='function')
def dynamodb(aws_credentials):
    with mock_dynamodb():
        yield boto3.resource('dynamodb', region_name='ap-southeast-2')

@pytest.fixture(scope='function')
def eventbridge(aws_credentials):
    with mock_events():
        yield boto3.client('events', region_name='ap-southeast-2')
