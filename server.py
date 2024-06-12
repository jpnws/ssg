import argparse
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from typing import Optional, Type


def run(
    server_class: Optional[Type[HTTPServer]] = None,
    handler_class: Optional[Type[SimpleHTTPRequestHandler]] = None,
    port: int = 8888,
    directory: Optional[str] = None,
):
    if server_class is None:
        server_class = HTTPServer
    if handler_class is None:
        handler_class = SimpleHTTPRequestHandler
    if directory:
        os.chdir(directory)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(
        f"Serving HTTP on http://localhost:{port} from directory '{directory or os.getcwd()}'..."
    )
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument(
        "--dir", type=str, help="Directory to serve files from", default="."
    )
    parser.add_argument("--port", type=int, help="Port to serve HTTP on", default=8888)
    args = parser.parse_args()

    run(port=args.port, directory=args.dir)
