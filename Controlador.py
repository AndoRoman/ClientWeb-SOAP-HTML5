import base64
import filetype
from flask import *
import os

# STARTING WEB SERVER
import ClientSoap

app = Flask(__name__)

# Set the secret key to 'secret' session
app.secret_key = os.urandom(8)


# CLASS FOTO
class Foto:
    def __init__(self, base64, mimetype, filename):
        self.base64 = base64
        self.mimetype = mimetype
        self.filename = filename


# RENDERING INDEX
@app.route('/dashboard')
def index():
    if 'username' in session:
        usuario = session['username']

        ##BUSCAR FORM DE USUARIO

        return render_template('index.html', forms=ClientSoap.getForms(usuario), username=usuario)
    else:
        return redirect('/')


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
    if 'username' in session:
        return render_template('register.html')
    else:
        return redirect('/')


# SIGN IN
@app.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']

        if ClientSoap.authentication(user, password):
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
        nivelEscolar = request.form['nivelEscolar']
        latitud = request.form['lati']
        longitud = request.form['longi']
        pictureUpload = request.files['thefiles']
        usuario = session['username']

        # BASE64 BYTES OF PICTURE
        pictureUpload.save(pictureUpload.filename)
        with open(pictureUpload.filename, "rb") as f:
            data = f.read()

        encodedBytes = base64.b64encode(str(data[0]).encode("utf-8"))
        filename = encodedBytes.title()
        mimetype = filetype.guess(pictureUpload)

        # Create a Object Foto
        img = Foto(base64=encodedBytes, mimetype=mimetype, filename=filename)

        # SAVE ON SERVER -> ERROR USUARIO object
        if ClientSoap.NewForm(name, sector, nivelEscolar, usuario, latitud, longitud, img):
            print('New Form Created Succes!')
            return redirect('/dashboard')
        else:
            print('ERROR! During process to created new form')


if __name__ == '__main__':
    app.run(debug=True)
