from flask import Flask, request, render_template_string

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

HTML = '''
<!doctype html>
<html>
<head><title>Calculator</title></head>
<body>
  <h2>Simple Calculator</h2>
  <form method="post">
    <input type="text" name="a" placeholder="Number 1" required>
    <input type="text" name="b" placeholder="Number 2" required>
    <select name="operation">
      <option value="add">Add</option>
      <option value="subtract">Subtract</option>
      <option value="multiply">Multiply</option>
      <option value="divide">Divide</option>
    </select>
    <input type="submit" value="Calculate">
  </form>
  <p>Result: {{result}}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = ""
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            operation = request.form['operation']
            if operation == 'add':
                result = add(a, b)
            elif operation == 'subtract':
                result = subtract(a, b)
            elif operation == 'multiply':
                result = multiply(a, b)
            elif operation == 'divide':
                result = divide(a, b)
        except ValueError:
            result = "Invalid input"
        except ZeroDivisionError:
            result = "Division by zero is not allowed."
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
