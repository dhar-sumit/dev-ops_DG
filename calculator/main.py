# main.py
import json

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def lambda_handler(event, context):
    query = event.get("queryStringParameters") or {}

    action = query.get("action")
    a = query.get("a")
    b = query.get("b")

    if action is None or a is None or b is None:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing parameters"})
        }

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Parameters a and b must be integers"})
        }

    result = None
    if action == "add":
        result = a + b
    elif action == "subtract":
        result = a - b
    elif action == "multiply":
        result = a * b
    elif action == "divide":
        if b == 0:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Division by zero"})
            }
        result = a / b
    else:
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Invalid action"})
        }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"result": result})
    }