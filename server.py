import socket

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:

    client_socket, client_address = s.accept()

    print(f"Connected by {client_address}")

    try:
        # Receive the HTTP request
        request = client_socket.recv(1024)

        # Convert bytes into text
        request_text = request.decode()

        print("\nRaw request:")
        print(request_text)

        # -------------------------
        # Parse HTTP request
        # -------------------------

        # Separate headers from body
        parts = request_text.split("\r\n\r\n", 1)

        header_section = parts[0]
        body = parts[1] if len(parts) > 1 else ''

        # Split the header section into individual lines
        header_lines = header_section.splitlines()

        # First line is the request line
        request_line = header_lines[0]

        # Extract method, path and HTTP version
        method, path, version = request_line.split(" ", 2)

        print("\nParsed request:")
        print(f"Method: {method}")
        print(f"Path: {path}")
        print(f"Version: {version}")

        # Parse headers
        headers = {}

        for header_line in header_lines[1:]:
            key, value = header_line.split(":", 1)
            headers[key.strip()] = value.strip()

        print(f"Headers: {headers}")
        print(f"Body: {body}")

        # -------------------------
        # Build HTTP response
        # -------------------------

        response_body = "Hello from my HTTP server!"

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(response_body.encode())}\r\n"
            "\r\n"
            f"{response_body}"
        )

        # HTTP is sent over the socket as bytes
        client_socket.sendall(response.encode())

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        client_socket.close()