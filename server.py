from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        message = "%s - [%s] %s" % (
            self.client_address[0],
            self.log_date_time_string(),
            format % args
        )
        user_agent = self.headers.get('User-Agent')
        if user_agent:
            message += f" User-Agent: {user_agent}"
        print(message)

if __name__ == "__main__":
    server_address = ('', 80)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print("Starting server...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        httpd.server_close()