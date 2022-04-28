import requests
from requests.exceptions import RequestException
from typing import Tuple, Union, Dict
import json


def generate_random_fact(output_format: str, language: str) -> Union[Dict, str]:
    """
    queries uselessfacts api for random fact; returns JSON if available - else string
    Args:
        output_format: json or str
        language: "en" or "de" (English/German)

    Returns: json or str

    """

    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}")

    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}.")
    # api returns dict with single quotes; convert to double-quote match json standard
    return json.dumps(fact)
