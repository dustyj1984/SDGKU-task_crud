import requests

BASE_URL = "http://127.0.0.1:5000/tasks"

def update_task(pk, title, subtitle, body):
    task_dictionary = {
        "title": title,
        "subtitle": subtitle,
        "body": body
    }
    

    url = "%s/%s" % (BASE_URL, pk)
    response = requests.put(url, json=task_dictionary)
    if response.status_code == 204:
        print("Operation successful")
    else:
        print("Operation failed")

if __name__ == "__main__":
    task_id input("Target task id: ")
    title = input("New Title: ")
    subtitle = input("New Subtitle: ")
    body = input("New task body: ")
    update_task(task_id, title, subtitle, body)