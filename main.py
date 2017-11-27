from flask import Flask, request, redirect, url_for, render_template
import pdb, sys
import runner
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # pdb.set_trace()
        headline_to_check = request.form['text']
        result = runner.scoring(headline_to_check)
    else:
        result = ''
        headline_to_check = ''
    # return "hello"
    print("headline = " + headline_to_check, file=sys.stderr)
    print("\n")
    print("result = " + str(result), file=sys.stderr)
    return render_template('index.html',  messages={'result':result, 'sentence':headline_to_check})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8083, debug=True)