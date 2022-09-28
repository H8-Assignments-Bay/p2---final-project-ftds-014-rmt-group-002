from flask import Flask, jsonify, request
import pickle
import pandas as pd

# init app
app = Flask(__name__)

# Open model
def open_model(model_path):
    '''helper function to load model'''

    with open(model_path,'rb') as model_file:
        model = pickle.load(model_file)

    return model

def cust_segment_inference(data, model):
    """
    input : list dengan lenght 9 --> ['Recency', 'Frequency', 'Monetary']
    outout : predict class : (idx)
    """

    # LABEL = ["Not Survived", "Survived"]
    columns = ['Recency', 'Frequency', 'Monetary']
    data = pd.DataFrame([data])
    data.columns = columns
    res = model.predict(data)
    return res[0]
    # LABEL[res[0]]

model_cust_segment = open_model('model_kmeans_pipe.pkl')

@app.route("/predict", methods=['POST'])
def diamonds_predict():
    args = request.json

    Recency = args.get("Recency")
    Frequency = args.get("Frequency")
    Monetary = args.get("Monetary")    

    new_data = [Recency, Frequency, Monetary]
    idx = cust_segment_inference(new_data, model_cust_segment)
    response = jsonify(result=str(idx))
    return response

# jika deploy ke heroku, komen baris di bawah
# app.run(debug=True)