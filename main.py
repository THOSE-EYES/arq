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

import threading
import argparse

from arq.connection.bdnoisyconnection import BidirectionalNoisyConnection
from arq.transceiver import Transceiver
from arq.data.basicdatasource import BasicDataSource as Source
from arq.controllers.receivercontroller import ReceiverController
from arq.controllers.sendercontroller import SenderController
from arq.codec import Codec
from utils.logger import Logger


def main():
    # Obtain arguments from the call
    parser = argparse.ArgumentParser(
        description='Basic ARQ system written in Python.')
    parser.add_argument('--probability', type=float,
                        help='Probability of bit toggling')
    parser.add_argument('--data_size', type=int,
                        help='Size of the data to generate (in bytes)')
    parser.add_argument('--package_size', type=int,
                        help='Size of the package data in range [5,7] (in bits)')
    parser.add_argument('--parity_bits', type=int,
                        help='Amount of parity bits')

    # Parse the arguments
    args = parser.parse_args()

    # Establish the connection
    transmitter = Transceiver()
    receiver = Transceiver()
    connection = BidirectionalNoisyConnection(
        receiver, transmitter, args.probability)

    # Create the transmitters
    codec = Codec(args.package_size, args.parity_bits)
    r_controller = ReceiverController(receiver, codec)
    s_controller = SenderController(
        transmitter, codec, Source(args.data_size))

    # Set the logger
    logger = Logger()
    r_controller.setLogger(logger)
    s_controller.setLogger(logger)

    # Start the sender controller
    s_controller.start()

    # Start the receiver controller
    r_thread = threading.Thread(target=r_controller.start)
    r_thread.start()

    # Wait for the receiver
    r_thread.join()


if __name__ == '__main__':
    main()
