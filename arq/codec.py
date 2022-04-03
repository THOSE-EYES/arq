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

import struct

from arq.package import Package


class Codec:
    '''
    Encoder/decoder class implementation

    Attributes
    ----------
    package_size : int
        Size of the package
    pbits: int
        Amount of parity bits

    Methods
    -------
    pack(data)
        Pack the data into packages
    unpack(data)
        Unpack the packages
    calculateParity(data, bits)
        Calculate parity for the data
    checkParity(data, bits, parity)
        Check if the parity is correct
    '''

    def __init__(self, package_size: int, pbits: int) -> None:
        '''
        Parameters
        ----------
        package_size : int
            Size of the package
        pbits: int
            Amount of parity bits
        '''
        # Check if the size of package is correct
        if package_size not in range(5, 8):
            raise ValueError("Package size must be in range [5, 7]")

        self.package_size = package_size
        self.pbits = pbits

    def pack(self, data: bytearray) -> list:
        '''Pack the data into packages

        Parameters
        ----------
        data : bytearray
            The data to pack into packages

        Returns
        -------
        list
            Packages with the parts of the data
        '''
        packed = list()

        # Iterate over the bytes
        for byte in data:
            parity = self.calculateParity(byte, self.pbits)

            # Fill the package
            package = Package(self.package_size, self.pbits)
            package.setValue(struct.pack("B", byte))
            package.setParityBits(parity)

            # Append the package
            packed.append(package)

        return packed

    def unpack(self, data: list) -> dict:
        '''Unpack the packages

        Parameters
        ----------
        data : list
            A list of packages to unpack

        Returns
        -------
        dict
            The dictionary with indexes and unpacked data
        '''
        unpacked = dict()

        index = 0
        for package in data:
            value = package.getValue()
            parity = package.getParityBits()

            # If the package was altered, push the error value to the array
            if self.checkParity(struct.unpack("B", value)[0], self.pbits, parity) == True:
                unpacked[index] = value
            else:
                unpacked[index] = None

            index += 1

        return unpacked

    def calculateParity(self, data: int, bits: int) -> int:
        ''' Calculate parity for the data

        Parameters
        ----------
        data: int
            The data for calculation
        bits:
            The amount of parity bits

        Returns
        -------
        int
            Parity bit of the data
        '''
        for index in range(0, bits):
            # Calculate the parity for the whole package
            bit = data % 2

            # Set the first bit to the value of the parity bit
            data = (data << 1)
            data ^= (-bit ^ data) & 0x1

        return data & 0b00000001

    def checkParity(self, data: int, bits: int, parity: int) -> bool:
        ''' Check if the parity is correct

        Parameters
        ----------
        data: int
            The data for calculation
        bits:
            The amount of parity bits
        parity : int
            Received parity bits

        Returns
        -------
        bool
            True if the parity is correct, False otherwise
        '''
        current_parity = self.calculateParity(data, bits)

        return parity == current_parity


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
