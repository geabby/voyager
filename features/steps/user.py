import os
from typing import Dict, List, Optional

import requests
import ujson


class User:

    def __init__(self, token: str = None) -> None:
        self.api_token = token

    def get_headers(self) -> Dict[str, str]:
        """
        returns header required for the post api call
        """
        return {
            'Accept': 'application/vnd.github.v3+json'
        }