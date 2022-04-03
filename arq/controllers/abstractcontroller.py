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

from arq.controllers.icontroller import IController
from arq.data.idatasource import IDataSource
from arq.codec import Codec
from utils.logger import Logger
from arq.transceiver import Transceiver


class AbstractController(IController):
    '''
    Abstract controller class

    Attributes
    ----------
    transceiver : Transceiver
        The transceiver, which sends or receives data
    codec : Codec
        The class which handles data encoding/decoding
    tag :
        The tag of the class
    logger : Logger
        The logger class

    Methods
    -------
    start()
        Starts the controller
    '''

    def __init__(self, transceiver: Transceiver, codec: Codec) -> None:
        '''
        Parameters
        ----------
        transceiver : Transceiver
            The transceiver, which sends or receives data
        codec : Codec
            The class which handles data encoding/decoding
        '''
        self.transceiver = transceiver
        self.codec = codec
        self.tag = "Controller"

    def setLogger(self, logger: Logger) -> None:
        '''Sets the new logger object

        Parameters
        ----------
        logger : Logger
            The logger object to use
        '''
        if logger != None:
            self.logger = logger


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
