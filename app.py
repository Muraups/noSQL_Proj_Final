from flask import Flask, render_template
from flask_cors import CORS
from route import pessoa_bp

app = Flask(__name__)
CORS(app)  # Permite chamadas de outro domínio (opcional)

# Registro do Blueprint de pessoas
app.register_blueprint(pessoa_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/view/pessoa")
def view_pessoa():
    return render_template("pessoa.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=85)
