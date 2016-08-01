
import socket

class SocketClient(object):
      def __init__(self, hostname = 'localhost', port = 2016):
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._hostname = hostname
            self._port = port

      def __enter__(self):
            print '> inside __enter__, connecting to {0}/{1}'\
                  .format(self._hostname, self._port)
            
            self._socket.connect((self._hostname, self._port))
            return self

      def __exit__(self, exception, value, traceback):
            print '> inside __exit__, closing socket...'
            self._socket.close()
            return False

      def send(self, data):
            print '> sending data: \'{0}\' to server...'.format(data)
            self._socket.send(data)

if __name__ == '__main__':
      with SocketClient() as s:
            s.send('test data')
      
