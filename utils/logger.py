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

from datetime import datetime


class Logger:
    '''
    This class encapsulates the logging feature for the console
    or file output

    Methods
    -------
    log(message)
        Writes the message to the destination
    '''

    def __init__(self):
        # TODO
        pass

    def log(self, tag: str, message: str) -> None:
        '''Writes the message to the destination

        Parameters
        ----------
        tag : str
            The tag of the class/method/function to write
        message : str
            The message to write
        '''
        if not message or not tag:
            return

        # Current implementation can only print the message to console
        timestamp = datetime.now().time()
        print("{} | [{}] {}".format(timestamp, tag, message))


if __name__ == '__main__':
    print("This file shouldn't be used as a separate script!")
