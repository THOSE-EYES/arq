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

from arq.data.idatasource import IDataSource
from arq.controllers.abstractcontroller import AbstractController
from arq.codec import Codec
from arq.package import Package
from arq.transceiver import Transceiver


class SenderController(AbstractController):
    '''
    The controller which handes data sending process

    Attributes
    ----------
    source : IDataSource
        The source of data

    Methods
    -------
    start()
        Starts the controller
    '''

    def __init__(self, transceiver: Transceiver,  codec: Codec, source: IDataSource) -> None:
        '''
        Parameters
        ----------
        transceiver : Transceiver
            The transceiver, which sends or receives data
        codec : Codec
            The class which handles data encoding/decoding
        source : IDataSource
            The source of data to send
        '''
        super(SenderController, self).__init__(transceiver, codec)

        self.source = source

        # Let it be just here
        self.tag = "SenderController"

    def start(self) -> None:
        '''Starts the controller'''

        data = self.source.getData()
        packages = self.codec.pack(data)

        self.transceiver.transmit(packages)

        # Print the result of the transmission check
        if self.logger != None:
            message = "Sent : {}, length : {}".format(data, len(data))
            self.logger.log(self.tag, message)


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
