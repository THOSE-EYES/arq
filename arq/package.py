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


class Package:
    '''
    This class is used only to store packed data

    Attributes
    ----------
    value : bytearray
        The binary data to use
    parity : int
        Parity bits
    pbits : int
        Amount of the parity bits
    size : int
        Size of the data

    Methods
    -------
    start()
        Starts the controller
    '''

    def __init__(self, size: int, pbits: int) -> None:
        '''
        Parameters
        ----------
        pbits : int
            Amount of the parity bits
        size : int
            Size of the data
        '''
        # Check if the size of parity bits is correct
        if pbits >= size / 2 or size not in range(5, 8):
            raise ValueError(
                "Parity bits number should be less than the half of the package")

        self.value = None
        self.parity = None

        self.pbits = pbits
        self.size = size

    def setValue(self, value: bytearray) -> None:
        ''' Set the data

        Parameters
        ----------
        value : bytearray
            The binary data to use
        '''
        # Check if the size of the package is correct
        if len(value) * 8 != self.size + self.pbits:
            raise ValueError("The package has incorrect size")

        self.value = value

    def getValue(self) -> bytearray:
        ''' Get the data

        Returns
        ----------
        bytearray
            The binary data to use
        '''
        return self.value

    def setParityBits(self, value: int) -> None:
        ''' Set the data

        Parameters
        ----------
        parity : int
            Parity bits
        '''
        self.parity = value

    def getParityBits(self) -> int:
        ''' Get the data

        Returns
        ----------
        int
            Parity bits
        '''
        return self.parity

    def getSize(self) -> int:
        ''' Get the size of the data

        Returns
        ----------
        int
            Size of the data
        '''
        return self.size

    def getParityBitsNumber(self) -> int:
        ''' Get the amount of the parity bits

        Returns
        ----------
        int
            Amount of the parity bits
        '''
        return self.pbits


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
