import requests
import threading

# Function to make a request to the server
def make_request():
    try:
        response = requests.get("http://127.0.0.1:5000/") 
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Connection failed:", e)

# Function to simulate a DDoS attack with multiple simultaneous requests
def simulate_ddos(threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=make_request)
        thread_list.append(thread)
        thread.start()

    # Waits for all threads to finish
    for thread in thread_list:
        thread.join()

# Prompts the user to enter the number of requests to simulate the DDoS attack
num_requests = int(input("Enter the number of requests to simulate the DDoS attack: "))
simulate_ddos(num_requests)
