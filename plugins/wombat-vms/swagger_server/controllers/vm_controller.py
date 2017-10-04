import connexion
from swagger_server.models.vm import VM
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def add_pet(vm=None):
    """
    Creates a new VM
    
    :param vm: 
    :type vm: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        vm = VM.from_dict(connexion.request.get_json())
    return 'sucessaasssoo'
