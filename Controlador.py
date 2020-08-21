from flask import *
import os

# STARTING WEB SERVER
import Client

app = Flask(__name__)

# Set the secret key to 'secret' session
app.secret_key = os.urandom(8)

# RENDERING INDEX
@app.route('/dashboard')
def index():
    usuario = session['username']

    ##BUSCAR FORM DE USUARIO

    return render_template('index.html', username=usuario)


@app.route('/')
def login():
    if 'username' in session:
        return redirect('/dashboard')

    else:
        return render_template('login.html')


@app.route('/loginOUT')
def loginOUT():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect('/')


@app.route('/crear')
def form():
    return render_template('register.html')


# SIGN IN
@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']

        if Client.authentication(user, password):
            session['username'] = user
            return redirect('/dashboard')
        else:
            return redirect('/')


@app.route('/registrar', methods=['POST'])
def register():
    # create new form
    if request.method == 'POST':
        name = request.form['nombre']
        sector = request.form['sector']
        latitud = request.form['lati']
        longitud = request.form['longi']
        f = request.files['thefiles']

        # SAVE ON SERVER
        if Client.NewForm(name, sector, latitud, longitud, f):
            print('New Form Created Succes!')
            return redirect('/dashboard')
        else:
            print('ERROR! During process to created new form')


if __name__ == '__main__':
    app.run(debug=True)
