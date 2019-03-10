from functools import partial
from http.server import HTTPServer
from argparse import ArgumentParser

from .httprequesthandler import CGMinerHTTPRequestHandler

HTTP_PORT = 8080
API_PORT = 4028
API_HOST = '127.0.0.1'

def _parse_args():
    args_parser = ArgumentParser(description='Start HTTP interface to the monitoring API')

    args_parser.add_argument('-w', '--http_port', nargs = 1, type = int, default = [HTTP_PORT], help = 'Port to use for http server')
    args_parser.add_argument('-p', '--api_port', nargs = 1, type = int, default = [API_PORT], help = 'Port used by API server')
    args_parser.add_argument('-a', '--api_host', nargs = 1, default = [API_HOST], help = 'Host name/address used by API server')

    return vars(args_parser.parse_args())

def start_server():
    args = _parse_args()

    try:
        # create web server and define request handler
        handler = partial(CGMinerHTTPRequestHandler, args['api_host'][0], args['api_port'][0])
        server = HTTPServer(('', args['http_port'][0]), handler)
        print('Started web server on port', args['http_port'][0])

        # wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        # shut down server on ctrl-c
        print('Shutting down the web server')
        server.socket.close()
