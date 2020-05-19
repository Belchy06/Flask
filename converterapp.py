from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1>Welcome to the main page</h1>'


@app.route('/c/<fahrenheit>')
def convert_fahrenheit_to_celsius(fahrenheit=""):
    try:
        fahrenheit = float(fahrenheit)
    except ValueError:
        return 'You need to enter a float value'
    return '{} Fahrenheit is: {:.2f} Celsius'.format(fahrenheit, (5 / 9 * (fahrenheit - 32)))


@app.route('/f/<celsius>')
def convert_celsius_to_farenheit(celsius=""):
    try:
        celsius = float(celsius)
    except ValueError:
        return 'You need to enter a float value'
    return '{} Celsius is: {:.2f} Fahrenheit'.format(celsius, (celsius * 9.0 / 5 + 32))


if __name__ == '__main__':
    app.run()
