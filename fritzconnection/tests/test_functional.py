"""
Running functional tests against a router - if present.
"""

import pytest
import requests

from ..core.fritzconnection import (
    FritzConnection,
)


TIMEOUT = 1.0
NO_ROUTER = 'no router present'


def _check_router_presence():
    try:
        requests.get('http://169.254.1.1/', timeout=TIMEOUT)
    except requests.ConnectionError:
        return True
    return False


no_router_present = _check_router_presence()


@pytest.mark.skipif(no_router_present, reason=NO_ROUTER)
def test_access_model_name():
    """
    Check whether description files are accessible.
    In this case there is some modelname available (a string).
    """
    fc = FritzConnection(timeout=TIMEOUT)
    assert isinstance(fc.modelname, str)