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

import time

from arq.controllers.abstractcontroller import AbstractController
from arq.codec import Codec
from arq.package import Package
from arq.transceiver import Transceiver


class ReceiverController(AbstractController):
    '''
    The controller which handes data receiving process

    Methods
    -------
    start()
            Starts the controller

    countFailed(data)
            Count altered packages
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

        super(ReceiverController, self).__init__(transceiver, codec)

        # Let it be just here
        self.tag = "ReceiverController"

    def start(self) -> None:
        '''Starts the controller'''

        # Wait for the data to become available
        while not self.transceiver.isDataReceived():
            time.sleep(1)

        # Print the result of the transmission check
        data = self.transceiver.getReceived()
        unpacked = self.codec.unpack(data)
        if self.logger != None:
            message = "Received : {}, failed : {}".format(
                len(data), self.countFailed(unpacked))
            self.logger.log(self.tag, message)

    def countFailed(self, data: dict) -> int:
        '''Count altered packages

        Parameters
        ----------
        data : dict
                The received data to check

        Returns
        -------
        int
                Anount of failed/altered packages
        '''
        counter = 0

        # If the value is None, then it was altered
        for key in data:
            if data[key] != None:
                continue

            counter += 1

        return counter


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
