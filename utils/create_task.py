import requests

URL = "http://127.0.0.1:5000/tasks"



def create_task(title, subtitle, body):
    task_data = {
        "title": title,
        "subtitle": subtitle,
        "body": body
    }
    response = requests.post(URL, json=task_data)
    if response.status_code == 201:
        print("Operation successful")
    else: 
        print("Operation failed")

if __name__ == "__main__":
    print("Creating task")
    title = input("Title: ")
    subtitle = input("Subtitle: ")
    body = input("Body: ")
    create_task(title, subtitle, body)

