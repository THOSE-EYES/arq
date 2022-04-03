'''
    Copyright 2022 Illia Shvarov

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from abc import ABC, abstractmethod
from arq.transceiver import Transceiver


class IConnection(ABC):
    '''
    Interface of all the connections

    Methods
    -------
    send(data, id)
        Send the data over the connection
    connect(transceiver)
        Connect the transceiver
    '''

    @abstractmethod
    def send(self, data: list, id: int) -> None:
        '''Send the data over the connection

        Parameters
        ----------
        data: list
            The data to send
        id : int
            Transceiver ID in the connection
        '''
        pass

    @abstractmethod
    def connect(self, transceiver: Transceiver) -> None:
        '''Connect the transceiver

        Parameters
        ----------
        transceiver: Transceiver
            The transceiver to use in the connection
        '''
        pass


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script")
