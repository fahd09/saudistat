from flask import Flask, render_template
import json
import pandas as pd
#import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():

    dat = [[['value', 30], ['name', 'Males']],[['value', 70], ['name', 'Females']]]
    js = json.dumps([dict(d) for d in dat])
    return render_template('index.html', entries = js)

    
@app.route("/cities")
def cities():
    work_force = pd.read_csv('./data/work_force_status_by_gender_by_city.csv', index_col=0)
    
#    work_force[ (work_force['status'] == 'Labor Force') & (work_force['sex'] == 'Male')]
#    work_force[ (work_force['status'] == 'Labor Force') & (work_force['sex'] == 'Female')]
#    work_force[ (work_force['status'] == 'Outside Labor Force') & (work_force['sex'] == 'Male')]
#    work_force[ (work_force['status'] == 'Outside Labor Force') & (work_force['sex'] == 'Female')]

    
    # Three kinds of tables we can extract;
    # first, 
    # sum of those inside Labor Force vs. outside labor force
    inside = work_force['value'][(work_force['status'] == 'Labor Force')].sum()
    outside= work_force['value'][(work_force['status'] == 'Outside Labor Force')].sum()
               
    dat = [
           [['value', inside], ['name', 'Labor Force']],
           [['value', outside], ['name', 'Outside Labor Force']]
           ]
    js = json.dumps([dict(d) for d in dat])
    return render_template('cities.html', entries = js)
    
if __name__ == "__main__":
    app.run()