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


class IDataSource(ABC):
    '''
    The class is an interface for concrete data source classes.

    Methods
    -------
    getData()
        Returns the data, which is used in the transmission
    '''

    @abstractmethod
    def getData(self) -> bytearray:
        '''Returns the data, which is used in the transmission

        Returns
        --------
        bytearray
            The data to use
        '''
        pass


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script")
