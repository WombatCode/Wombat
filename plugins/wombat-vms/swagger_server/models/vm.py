# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class VM(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: str=None, vm_id: int=None, cpu: int=None, memory: int=None, volume: int=None):
        """
        VM - a model defined in Swagger

        :param id: The id of this VM.
        :type id: str
        :param vm_id: The vm_id of this VM.
        :type vm_id: int
        :param cpu: The cpu of this VM.
        :type cpu: int
        :param memory: The memory of this VM.
        :type memory: int
        :param volume: The volume of this VM.
        :type volume: int
        """
        self.swagger_types = {
            'id': str,
            'vm_id': int,
            'cpu': int,
            'memory': int,
            'volume': int
        }

        self.attribute_map = {
            'id': 'id',
            'vm_id': 'vmId',
            'cpu': 'cpu',
            'memory': 'memory',
            'volume': 'volume'
        }

        self._id = id
        self._vm_id = vm_id
        self._cpu = cpu
        self._memory = memory
        self._volume = volume

    @classmethod
    def from_dict(cls, dikt) -> 'VM':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VM of this VM.
        :rtype: VM
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """
        Gets the id of this VM.

        :return: The id of this VM.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """
        Sets the id of this VM.

        :param id: The id of this VM.
        :type id: str
        """

        self._id = id

    @property
    def vm_id(self) -> int:
        """
        Gets the vm_id of this VM.

        :return: The vm_id of this VM.
        :rtype: int
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id: int):
        """
        Sets the vm_id of this VM.

        :param vm_id: The vm_id of this VM.
        :type vm_id: int
        """

        self._vm_id = vm_id

    @property
    def cpu(self) -> int:
        """
        Gets the cpu of this VM.

        :return: The cpu of this VM.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: int):
        """
        Sets the cpu of this VM.

        :param cpu: The cpu of this VM.
        :type cpu: int
        """

        self._cpu = cpu

    @property
    def memory(self) -> int:
        """
        Gets the memory of this VM.

        :return: The memory of this VM.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory: int):
        """
        Sets the memory of this VM.

        :param memory: The memory of this VM.
        :type memory: int
        """

        self._memory = memory

    @property
    def volume(self) -> int:
        """
        Gets the volume of this VM.

        :return: The volume of this VM.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        """
        Sets the volume of this VM.

        :param volume: The volume of this VM.
        :type volume: int
        """

        self._volume = volume

