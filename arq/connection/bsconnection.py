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

from arq.connection.bdnoisyconnection import BidirectionalNoisyConnection
from arq.package import Package
from arq.transceiver import Transceiver
import komm


class BinarySymmetricConnection(BidirectionalNoisyConnection):
    '''
    Bi-directional binary symmetric and noisy connection implementation

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
            The crossover probability
        '''

        super(BinarySymmetricConnection, self).__init__(a, b, probability)

    def applyNoise(self, package: Package, probability: float) -> Package:
        '''Apply noise to the package

        Parameters
        ----------
        package : Package
            The package to alter
        probability : int
            The crossover probability
        '''
        data = bytearray(package.getValue())

        bsc = komm.BinarySymmetricChannel(self.probability)
        # data = bsc(data).tobytes()

        converted_data = self._toList(data)
        data = bytearray()
        for index in range(0, int(len(converted_data) / 8)):
            offset = index * 8
            noisy_data = bsc(converted_data[offset:offset + 8])

            data.extend(self._fromList(noisy_data))

        # print(data, type(data), len(data))

        package.setValue(data)
        return package

    def _toList(self, data: bytearray) -> list:
        '''Helper method for the connection variables casting into list

        Parameters
        ----------
        data : bytearray
            The data to cast
        '''
        result = list()
        for byte in data:
            for index in range(0, 8):
                bit = (int(byte) >> index) & 0x1
                result.insert(0, bit)

        return result

    def _fromList(self, data: list) -> bytearray:
        '''Helper method for the connection variables casting into bytearray

        Parameters
        ----------
        data : list
            The data to cast
        '''
        result = int()
        for bit in data[0:7]:
            result = (result | bit) << 1
        result = (result | bit)

        return bytearray(int(result).to_bytes(1, 'big'))


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script")
