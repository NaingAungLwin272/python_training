from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/<name>')
def success(name):
    return 'Welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        if user.lower() == 'mth':
            return redirect(url_for('success', name=user))
        else:
            return "Unauthorized User"
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
