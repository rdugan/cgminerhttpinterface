from http.server import CGIHTTPRequestHandler
import socket

from .rpcinterface import CGMinerRPCInterface

class CGMinerHTTPRequestHandler(CGIHTTPRequestHandler):
    """Handle http requests for miner monitoring"""

    def __init__(self, api_host, api_port, *args, **kwargs):
        self.api_host = api_host
        self.api_port = api_port
        super().__init__(*args, **kwargs)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        """Handler for GET requests"""
        # ignored requests
        ignored_requests = ['/favicon.ico']
        if self.path in ignored_requests:
            self.send_error(404, '')
            return

        try:
            monitor = CGMinerRPCInterface(self.api_host, self.api_port)

            # no parameter validation for now - let API do it
            command = 'summary+devs'
            parameter = None
            pathTree = self.path.split('/')
            pathFields = len(pathTree)
            if pathFields > 1 and pathTree[1]:
                command = pathTree[1]
            if pathFields > 2:
                parameter = pathTree[2]

            # issue API request
            api_response = monitor.issue_command(command, parameter)

            # return headers, followed by output of API call
            self.do_HEAD()
            self.wfile.write(bytes(api_response, 'utf-8'))

            return

        except socket.error:
            self.send_error(500, 'Internal server error: API request failed')
