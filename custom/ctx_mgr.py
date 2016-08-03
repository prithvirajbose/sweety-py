"""
Demostrates how to use the context manager as a
decorator and as a class in the context of a client socket.
"""

import socket
from contextlib import contextmanager

@contextmanager
def socket_client_ctx(socketclient):
      """
      Demostrates how to use the context manager decorator
      to create a generator based context manager.
      """
      try:
            socketclient.connect()
            yield socketclient
      except:
            raise
      finally:
            socketclient.close()

class SocketClient(object):
      """
      A simple socket client to send data to a server socket.
      On Unix, use 'nc -l port_number' or  'nc -lk port_number' to send data
      to the client.
      
      For the unfortunate ones stuck with Windows OS, I've
      written a Java socket server class named ServerSocket.java.
      Run that class to receive message from this client.
      """
      def __init__(self, hostname = 'localhost', port = 2016):
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._hostname = hostname
            self._port = port
            
      def connect(self):
            print '> inside {0}, connecting to {1}/{2}'.format(self.__class__, self._hostname, self._port)
            self._socket.connect((self._hostname, self._port))

      def close(self):
            self._socket.close()
            
      def send(self, data):
            print '> inside {0}, sending data: \'{1}\' to server...'.format(self.__class__, data)
            self._socket.send(data)

class SocketClientContext(object):
      """
      Demostrates how to use the context manager as a class.
      """
      def __init__(self, socket_client):
            self._socket_client = socket_client

      def __enter__(self):
            print '> inside {0}.__enter__...'.format(self.__class__)
            self._socket_client.connect()
            return self._socket_client

      def __exit__(self, exception, value, traceback):
            print '> inside {0}.__exit__...'.format(self.__class__)
            self._socket_client.close()
            return False

if __name__ == '__main__':
      '''
      This has the same effect:
            with SocketClientContext(SocketClient())as s:
      '''
      try:
            with socket_client_ctx(SocketClient())as s:
                  s.send('test data')
      except Exception as e:
            print e
