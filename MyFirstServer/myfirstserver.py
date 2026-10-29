# This is my first attempt of a HTTP server using python's HTTP.server module

from http.server import HTTPServer, BaseHTTPRequestHandler # Imports what we need

# Request Handler main() requires
class RequestHandler(BaseHTTPRequestHandler):
    # The following method is called when a GET request is made by a client
    def do_GET(self):
        self.send_response(200) # This sends the client a response saying that the server has recieved the request successfully.
        self.send_header("content-type", "text/html") # In the header specifies that the payload is HTML. Use "application/json for JSON"
        self.end_headers() # Required to finish off the header

        dictionary = {"1": "That is the smallest positive integer",
                      "2": "Looks like a little duck",
                      "3": "The magic number",
                      "4": "Oscar's favourite number",
                      "5": "Half way!",
                      "6": "Upside down 9",
                      "7": "SEVEN",
                      "8": "A little fat lady",
                      "9": "Upside down 10",
                      "10": "The only two digit number you could've chosen"}

        payload = dictionary[self.path[1:]]
        self.wfile.write(payload.encode()) # Writes packet payload to send back to packet

# Called when server starts
def main():
    PORT = 8000 # Port we are using. 8000 is a HTTP port. Constant so in full caps.
    server = HTTPServer(("", PORT), RequestHandler) # Creates the appropriate server object
    server.serve_forever() # Keeps server running until it is manually turned off

# Starts server via calling "main()" when the python file is directly run
if __name__ == "__main__":
    main()

# Run this server by finding the folder in terminal, and writing "python3 myfirstserver.py"
# Stop the server with CTRL C in terminal.
