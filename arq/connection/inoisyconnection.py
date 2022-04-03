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
from arq.package import Package


class INoisyConnection(ABC):
    '''
    Interface of all the noisy connections

    Methods
    -------
    applyNoise(package, probability)
        Apply noise to the package
    '''

    @abstractmethod
    def applyNoise(package: Package, probability: float) -> None:
        '''Apply noise to the package

        Parameters
        ----------
        package : Package
            The package to alter
        probability : int
            The probability of a bit to be flipped
        '''
        pass
