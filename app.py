from distutils.log import debug
from flask import Flask, render_template , url_for



    
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")



@app.route('/contatos')
def contatos():
    return render_template("contato.html")


@app.route('/quemSomos')
def quemSomos():
    return render_template("quem_somos.html")




if __name__ == "__main__":
    app.run()



