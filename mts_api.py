import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def get_token() -> dict:
    """Returns a token in the format: {'token_type': ..., 'access_token': ..., }"""

    token_url = 'https://api.mts.ru/token/'
    token_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    token_data = {
        'grant_type': 'client_credentials',
    }
    token_response = requests.post(
        url=token_url,
        headers=token_headers,
        auth=(os.getenv('MTS_API_LOGIN'), os.getenv('MTS_API_PASSWORD')),
        data=token_data
    )
    token = json.loads(token_response.content)

    return token


def get_status_call_forwarding():
    token = get_token()

    url = 'https://api.mts.ru/b2b/v1/Product/CallForwardingInfo'
    headers = {
        'Authorization': f'{token["token_type"]} {token["access_token"]}',
    }
    params = {
        'productCharacteristic.name': 'MSISDN',
        'productCharacteristic.value': os.getenv('WORK_PHONE'),
        'productLine.name': 'CallForwarding'
    }
    response = requests.get(url, headers=headers, params=params)

    return json.loads(response.content)


def create_call_forwarding(forwarding_address: str) -> dict:
    """ forwarding_address in the format: 7XXXXXXXXXX """
    c_token = get_token()

    c_url = 'https://api.mts.ru/b2b/v1/Product/ChangeCallForwarding/'
    c_headers = {
        'Authorization': f'{c_token["token_type"]} {c_token["access_token"]}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',

    }
    data_raw = {
        'characteristic': [
            {
                'name': 'MSISDN',
                'value': os.getenv('WORK_PHONE')
            }
        ],
        'item': [
            {
                'action': 'create',
                'product': {
                    'productLine': {
                        'name': 'CallForwarding'
                    },
                    'productCharacteristic': [
                        {
                            'name': 'ForwardingAddress',
                            'value': forwarding_address
                        },
                        {
                            'name': 'ForwardingType',
                            'value': 'CFU'
                        },
                        {
                            'name': 'NoReplyTimer',
                            'value': '0'
                        },
                        {
                            'name': 'NumType',
                            'value': 'Regular'
                        }
                    ]
                }
            }
        ],
        'relatedParty': {
            'type': 'Individual',
            'location': {
                'id': '000000000',
                'role': 'point-of-sale'
            }
        }
    }
    call_response = requests.post(url=c_url, headers=c_headers, json=data_raw)

    response = {
        'status_code': call_response.status_code,
        'content': json.loads(call_response.content)
    }

    return response
