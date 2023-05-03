from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/ask', methods=['GET'])
def run_script():
    question = request.args.get('question')
    import subprocess

    r = question
    try:
        r = subprocess.check_output(['python', 'ask.py', '--question', question], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print(f'Erro: {e.output.decode()}')
    
    result = r.decode('utf-8')   
    
    #print(result)
    return result

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
