from flask import Flask, request, render_template, abort


app_name = 'ChirPy'
app = Flask(app_name)


@app.route('/')
def index():
    return 'Hello, World!', 200