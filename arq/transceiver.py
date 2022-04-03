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

from arq.connection import iconnection as IConnection


class Transceiver:
    '''
    The class which handles data transmission using the connection

    Attributes
    ----------
    id : int
        Transceiver ID in the connection
    data : list
        The received data
    connection : IConnection
        The established connection to use

    Methods
    -------
    start()
        Starts the controller
    '''

    def __init__(self) -> None:
        self.id = -1
        self.data = None

    def establishConnection(self, connection: IConnection, id: int) -> None:
        '''Establishes the connection between transceivers

        Parameters
        ----------
        connection: IConnection
            The established connection to use
        id : int
            Transceiver ID in the connection
        '''
        self.connection = connection
        self.id = id

    def transmit(self, data: list) -> None:
        '''Transmit the data to another transceiver

        Parameters
        ----------
        data : list
            The data to transmit
        '''
        # Check if a connection exists
        if id == -1:
            return

        self.connection.send(data, self.id)

    def receive(self, data: list) -> None:
        '''Receive the data from another transceiver

        Parameters
        ----------
        data : list
            The received data
        '''
        self.data = data

    def getReceived(self) -> dict:
        '''Get the received data

        Returns
        -------
        list
            The received data
        '''
        # Remove the data from the transceiver instance
        data = self.data
        self.data = None

        # Return the local copy
        return data

    def isDataReceived(self) -> bool:
        '''Check if the data is received

        Returns
        -------
        bool
            true, if the data is present, false otherwise
        '''
        return self.data != None


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
