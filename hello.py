from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def hello():

    dat = [[['value', 30], ['name', 'Males']],[['value', 70], ['name', 'Females']]]
    js = json.dumps([dict(d) for d in dat])
    return render_template('index.html', entries = js)

    
    
    
    
    
    
#@app.route("/cities")
#def cities():
#    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()