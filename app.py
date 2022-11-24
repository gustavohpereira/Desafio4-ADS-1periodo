from distutils.log import debug
from flask import Flask, render_template , url_for, request
from flask_mysqldb import MySQL



def create_app():
    from app import routes
    routes.init_app(app)

    return app
app = Flask(__name__)


# conexão com o banco de dados
app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL(app)



@app.route('/')
def home():
    return render_template("index.html")





@app.route('/quemSomos')
def quemSomos():
    return render_template("quem_somos.html")


@app.route('/contatos', methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, nome, assunto) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contato.html')

if __name__ == "__main__":
    app.run(debug=True)



