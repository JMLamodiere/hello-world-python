import time

def hello(event, context):
    print("before sleep")
    time.sleep(4)
    print("after sleep")
    return "hello-world"
