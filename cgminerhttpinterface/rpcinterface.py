import socket
import traceback
import json

BUFFER_LENGTH = 4096

class CGMinerRPCInterface(object):
    """Handle remote procedure calls for miner monitoring"""

    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.settimeout(5)
        except socket.error:
            traceback.print_exc()
            raise

    def __del__(self):
        self._close()

    def _close(self):
        """Disconnect from RPC API server if necessary"""
        try:
            if self.sock is not None:
                # TODO: figure out how to check socket status to avoid
                # exceptions from unnecessary shutdown calls
                self.sock.shutdown(socket.SHUT_RDWR)
                self.sock.close()
                self.sock = None
        except socket.error:
            traceback.print_exc()
            raise

    def _connect(self):
        """Connect to RPC API server"""
        try:
            print(f'\nConnecting to {self.host}:{self.port}')
            self.sock.connect((self.host, self.port))
        except socket.error:
            self._close()
            traceback.print_exc()
            raise

    def _send(self, message):
        """Send RPC messages to API"""
        try:
            print("Sending request", message)
            self.sock.sendall(bytes(message, 'utf-8'))
        except socket.error:
            traceback.print_exc()
            raise

    def _receive(self):
        """Receive RPC messages from API after sending request"""
        chunks = []
        chunk = 1
        try:
            # iterate over response chunks until we've received everything
            while chunk:
                chunk = self.sock.recv(BUFFER_LENGTH)
                chunks.append(chunk)
        except socket.error:
            traceback.print_exc()
            raise

        return b''.join(chunks)

    def issue_command(self, command, param = None):
        """Connect to API, send requested command w/ optional parameters,
        and return formatted response
        """
        response = ''
        message = {"command": command}
        if param is not None:
            message.update({"parameter": param})
        try:
            self._connect()
            self._send(json.dumps(message))
            response = self._receive()
        finally:
            self._close()

        return json.dumps(json.loads(response), indent = 4)
