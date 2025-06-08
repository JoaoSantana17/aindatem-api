from flask import Flask
from flask_cors import CORS
from user import user_bp
from recursos import recursos_bp
from fontes import fontes_bp
from distancias import distancias_bp

app = Flask(__name__)
app.url_map.strict_slashes = False  
CORS(app, origins=["http://localhost:3000", "https://aindatem-api.vercel.app", "https://aindatem.vercel.app"])

app.register_blueprint(user_bp)
app.register_blueprint(recursos_bp)
app.register_blueprint(fontes_bp)
app.register_blueprint(distancias_bp)

@app.route('/')
def index():
    return {"message": "API Ainda Tem /distancias /fontes /recursos /usuario"}

if __name__ == '__main__':
    app.run(debug=True)
