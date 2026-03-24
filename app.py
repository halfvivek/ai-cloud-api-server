from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import requests
import datetime

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        # Logging (important for debugging)
        print(f"Received request: {self.path}")

        if parsed_url.path == "/ask":
            question = query_params.get("question", [""])[0].lower()

            try:
                # Routing logic
                if "joke" in question:
                    response_api = requests.get("https://api.chucknorris.io/jokes/random")
                    data = response_api.json()
                    response_text = data.get("value", "No joke found")

                elif "time" in question:
                    response_text = f"Current server time is {datetime.datetime.now()}"

                elif "name" in question:
                    response_text = "My name is Vivek's AI Server!"

                elif "weather" in question:
                    response_text = "Weather feature coming soon!"

                else:
                    response_text = f"You asked: '{question}'. I am still learning but I understood your request!"

            except Exception as e:
                response_text = f"Error: {str(e)}"

        elif parsed_url.path == "/status":
            response_text = "Server is running successfully!"

        else:
            response_text = "Welcome to Vivek's AI API server!"

        # Send response
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response_text.encode())


# Start server
server = HTTPServer(("0.0.0.0", 5000), MyServer)
print("AI Server running on port 5000")
server.serve_forever()
