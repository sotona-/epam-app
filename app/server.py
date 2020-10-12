from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/404', methods=['POST', 'GET'])
def error_404():
    return render_template('404.html')


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
