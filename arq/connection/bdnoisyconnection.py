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

import random

from arq.connection.inoisyconnection import INoisyConnection
from arq.connection.bdconnection import BidirectionalConnection
from arq.package import Package
from arq.transceiver import Transceiver


class BidirectionalNoisyConnection(BidirectionalConnection, INoisyConnection):
    '''
    Bi-directional noisy connection implementation

    Attributes
    ----------
    probability : int
        The probability of the bit to be flipped

    Methods
    -------
    send(data, id)
        Send the data over the connection
    connect(transceiver)
        Connect the transceiver
    '''

    def __init__(self, a: Transceiver, b: Transceiver, probability: float) -> None:
        '''
        Parameters
        ----------
        a : Transceiver
            One of the transceivers to be connected
        b : Transceiver
            One of the transceivers to be connected
        probability : int
            The probability of the bit to be flipped
        '''

        super(BidirectionalNoisyConnection, self).__init__(a, b)

        self.probability = probability

    def applyNoise(self, package: Package, probability: float) -> Package:
        '''Apply noise to the package

        Parameters
        ----------
        package : Package
            The package to alter
        probability : int
            The probability of a bit to be flipped
        '''
        data = bytearray(package.getValue())

        for byte in range(0, len(data)):
            # Iterate over bits
            for index in range(8):
                # Don't do anything, if the probability is not met
                if random.random() > self.probability:
                    continue

                # Flip the bit
                data[byte] = data[byte] ^ (1 << index)

        package.setValue(data)
        return package

    def send(self, data: list, id: int) -> None:
        '''Send the data over the connection

        Parameters
        ----------
        data: list
            The data to send
        id : int
            Transceiver ID in the connection
        '''

        # Apply noise to the data
        noisy_data = list()
        for package in data:
            noisy_data.append(self.applyNoise(package, self.probability))

        # Call the superclass'es method
        super(BidirectionalNoisyConnection, self).send(noisy_data, id)


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script")
