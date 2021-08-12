from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='blargityblargblargblargity'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    if 'true_counter' in session:
        session['true_counter'] += 1
    else:
        session['true_counter'] = 1
    return render_template('index.html')
@app.route('/2')
def add_two():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return redirect('/')
@app.route('/destroy_session')
def reset():
    session.pop('counter')
    return redirect('/')
@app.route('/add', methods=['POST'])
def add_num():
    session['counter'] += int(request.form['num'])-1
    return redirect('/')
@app.route('/hard_reset')
def reset_all():
    session.clear()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)