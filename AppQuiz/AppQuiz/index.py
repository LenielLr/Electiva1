from flask import Flask, render_template, request
#from flask_mysqldb import MySQL

#app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'password'
#app.config['MYSQL_DB'] = 'gestionquiz'

#mysql = MySQL(app)


@#app.route('/')
def inicio():
    return render_template('inicio.html')


#@app.route('/Crear-Quiz', methods=['GET', 'POST'])
def crearQuiz():
    return render_template('crear_quiz.html')


#@app.route('/Gestionar-Quizzes', methods=['GET', 'POST'])
def GestionarQuizzes():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '')
        descripcion = request.form.get('descripcion', '')
        mezclar = 'shuffle' in request.form
        print(titulo, descripcion, mezclar)
    return render_template('gestionar_quizzes.html')



#@app.route('/Ayuda')
def ayuda():
    return render_template('ayuda.html')


if __name__ == "__main__":
    #app.run(port=3000, debug=True)
