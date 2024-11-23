Academic Project: Simulating a DDoS Attack with Python and Flask
This project is an academic exercise designed to illustrate the concept of Distributed Denial of Service (DDoS) attacks and their impact on web servers. It involves setting up a simple web server using Flask and creating a Python-based load simulator to generate multiple simultaneous requests to mimic a DDoS scenario.

The project is divided into two main components:

Web Server: A basic Flask server is implemented to respond to HTTP requests. To simulate real-world processing delays, a small delay is added to each request. This server represents a typical web application that could be targeted by high traffic.

Load Simulator: A Python script is used to send a large number of requests to the Flask server in parallel using threading. The simulator allows users to input the number of requests they wish to generate, demonstrating how a high volume of traffic can overload a server.

Objectives:
To understand the behavior of a server under high traffic conditions.
To explore the concept of thread-based concurrency for generating simultaneous requests.
To analyze the impact of excessive requests on server performance.

To test, run the server script (server.py), then execute the simulator (simulador_ddos.py) and input the number of requests.

Note:
This project is for educational purposes only and aims to provide a hands-on understanding of server performance under stress. It is not intended to encourage or promote malicious activities.

