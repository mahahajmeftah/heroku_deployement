# import Flask
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl','rb'))
@app.route("/") #home
def home():
    return render_template('index.html')

    
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendring results in HTML GUI
    '''
    #save our features(that we get it from the form) in a list and convert them from a string to a int
    int_features =[int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0],2)
    return render_template('index.html', prediction_text='Price of car should be $ {}'.format(output))
    
if __name__=='__main__':
    app.run(port=5000,debug=True)