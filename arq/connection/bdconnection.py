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

import arq
from arq.connection import iconnection
from arq.package import Package
from arq.transceiver import Transceiver


class BidirectionalConnection(iconnection.IConnection):
    '''
    Bi-directional connection implementation

    Attributes
    ----------
    nodes: list
        List of transceivers used in the connection

    Methods
    -------
    send(data, id)
        Send the data over the connection
    connect(transceiver)
        Connect the transceiver
    '''

    def __init__(self, a: Transceiver, b: Transceiver) -> None:
        '''
        Parameters
        ----------
        a : Transceiver
            One of the transceivers to be connected
        b : Transceiver
            One of the transceivers to be connected
        '''

        self.nodes = list()

        # Connect the transceivers
        self.connect(a)
        self.connect(b)

    def send(self, data: list, id: int) -> None:
        '''Send the data over the connection

        Parameters
        ----------
        data: list
            The data to send
        id : int
            Transceiver ID in the connection
        '''

        # Get the right receiver
        receiver = self.nodes[0 if id == 1 else 1]

        # Pass the signal
        receiver.receive(data)

    def connect(self, transceiver: Transceiver) -> None:
        '''Connect the transceiver

        Parameters
        ----------
        transceiver: Transceiver
            The transceiver to use in the connection
        '''

        # Add the transceiver to the list
        self.nodes.append(transceiver)

        # Notify the transceiver about the connection
        transceiver.establishConnection(self, len(self.nodes) - 1)


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script")
