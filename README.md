# Client-Server Socket Application

Simple Python TCP socket programs demonstrating client-server communication. A client application requests lecture notes from a server, which processes the request and returns a response.

## Files
- `server.py`: TCP server that listens on port 5050 and responds to incoming requests.
- `client.py`: TCP client that connects to the server and sends a request string terminated by a newline.

## Requirements
- Python 3.x

## How to Run

1. Start the server:
```bash
python3 server.py
```

2. Open another terminal and run the client:

**Normal Request (Lecture notes):**
```bash
python3 client.py GET_NOTES
```
Output:
```text
Server response:
200 OK: Operating Systems Lecture 1 - Overview and Services
```

**Unknown Request:**
```bash
python3 client.py GET_HOMEWORK
```
Output:
```text
Server response:
404 ERROR: Unknown request
```
