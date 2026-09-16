# Raw HTTP Server

A minimal HTTP server built from scratch using Python sockets.

## What it does

• Accepts TCP connections
• Parses HTTP requests
• Parses request headers and body
• Routes requests by path and method
• Returns HTTP status codes
• Handles GET and POST requests
• Returns 404 for unknown paths
• Returns 405 for unsupported methods

## Example

```bash
curl -i http://127.0.0.1:65432/hello
```
