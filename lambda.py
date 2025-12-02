import json
import calc  # Import the calculator functions from calc.py

def lambda_handler(event, context):
    try:
        # Retrieve query parameters (a, b, and operation)
        a = int(event['queryStringParameters']['a'])
        b = int(event['queryStringParameters']['b'])
        operation = event['queryStringParameters']['operation']

        # Perform the operation based on the 'operation' parameter
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Invalid operation. Please choose "add", "subtract", "multiply", or "divide".')
            }

        # Return the result as a response
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }

    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing required parameters. Ensure you include "a", "b", and "operation".')
        }
    except ValueError as ve:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Error: {str(ve)}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Internal server error: {str(e)}')
        }
