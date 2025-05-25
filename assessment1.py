import queue
import uuid
import time

app_queue = queue.Queue()

def generate_request():
    r_guid = uuid.uuid4()
    request = {
        "id": str(r_guid),
        "type": "request",
        "data": {
            "message": f"Request with ID {r_guid} generated."
        }
    }
    app_queue.put(request)
    print(f"Generated: {request}")


def process_requests():
    while not app_queue.empty():
        request = app_queue.get()
        print(f"Processing: {request}")

        time.sleep(1)
        print(f"Processed: {request['id']}")
        app_queue.task_done()

def main():
    for _ in range(5):
        generate_request()

    process_requests()

    print("All requests processed.")


if __name__ == "__main__":
    main()