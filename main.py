
from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True
py_css = '''
<style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
        '''

form = '''
<!DOCTYPE html>



<html>

    <head>

        <style>

            form {

                background-color: #eee;

                padding: 20px;

                margin: 0 auto;

                width: 540px;

                font: 16px sans-serif;

                border-radius: 10px;

            }

            textarea {

                margin: 10px 0;

                width: 540px;

                height: 120px;

            }

        </style>

    </head>

    <body>

      <form action = "/en" method = "post">
        Rotate by:<input type="text" name = "rot" />0
        <input type="textarea" name = "phrase" />
        <input type="submit" />
      </form>

    </body>

</html>
'''

@app.route("/")
def index():
    return form
    
@app.route("/en", methods=['POST'])
def encryptpage():
    print(bencrypt("ABC",1))
    rot = request.form['rot']
    phrase = request.form['phrase']

    en_form = '''
<!DOCTYPE html>



<html>

    <head>

        '''+py_css+'''

    </head>

    <body>
        <form action = "/en" method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value = "'''+rot+ ''' ">
                <p class="error"></p>
            </div>
            <textarea type="text" name="phrase">'''+bencrypt(phrase,rot) +'''</textarea>
            <br>
            <input type="submit">

    </body>

</html>
'''
    return en_form

def bencrypt(T,R):
    ST=encrypt(T,int(R))
    return ST

app.run()