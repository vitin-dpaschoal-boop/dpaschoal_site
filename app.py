from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rastreamento', methods=['GET', 'POST'])
def rastreamento():
    status = None
    if request.method == 'POST':
        codigo = request.form['codigo']
        status = f"Código {codigo} - Em transporte 🚚"
    return render_template('rastreamento.html', status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
