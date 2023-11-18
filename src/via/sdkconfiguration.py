"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests
from dataclasses import dataclass
from typing import Dict, Tuple
from .utils.retries import RetryConfig
from .utils import utils


SERVERS = [
    'http://api.example.com/v1',
    # Optional server description, e.g. Main (production) server
    'http://staging-api.example.com',
    # Optional server description, e.g. Internal staging server for testing
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests.Session
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = '0.1.9'
    sdk_version: str = '0.7.3'
    gen_version: str = '2.194.1'
    user_agent: str = 'speakeasy-sdk/python 0.7.3 2.194.1 0.1.9 via'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
