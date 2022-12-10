import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model_gender = pickle.load(open('model_gender_scenario1_XGBoost.pkl', 'rb')) 
model_age = pickle.load(open('model_age_scenario1_XGBoost.pkl','rb'))

test_data1 = pd.read_csv('test_data_scenario_1.csv')

campaign_gender = {'F':'Campaign 1, Campaign 2','M':'Campaign 3'}
campaing_age = {'0-24':'Campaign 4','24-32': 'Campaign 5','32+':'Campaign 6'}
## For age prediction Classification model was used and following are the encoded values
## 0-24 - 1, 25-32 -2, 32+ -3
def age_grouping(age):
    if age ==1:
        return '0-24'
    elif age ==2:
        return '24-32'
    else :
        return '32+'

@app.route('/gender')
def home_gender():
    return render_template('index_gender.html')

@app.route('/age')
def home_age():
    return render_template('index_age.html')

@app.route('/gender_getData')
def predict_gender():
    chosen_idx = np.random.choice(len(test_data1), replace = True, size = 50)   
    test_data = test_data1.iloc[chosen_idx].reset_index(drop= True)  
    x_test = test_data.drop(columns=['Device_id','Gender'])
    res = model_gender.predict(x_test)
    df_gender_res = pd.DataFrame(res)
    df_gender_res.columns= ['gender_predicted']
    df_gender_res = pd.concat([test_data[['Device_id']],df_gender_res], axis=1)
    df_gender_res['gender_predicted'] = df_gender_res['gender_predicted'].apply(lambda x: 'M' if x == 1 else 'F')
    df_gender_res['action_campaign'] = df_gender_res['gender_predicted'].apply(lambda x: campaign_gender[x])
    df_gender_res= df_gender_res.to_json()
    return df_gender_res

@app.route('/age_getData')
def predict_age(): 
    chosen_idx = np.random.choice(len(test_data1), replace = True, size = 50)   
    test_data = test_data1.iloc[chosen_idx].reset_index(drop= True)  
    x_test = test_data.drop(columns=['Device_id','Age_Group'])
    res = model_age.predict(x_test)
    df_age_res = pd.DataFrame(res)
    df_age_res.columns= ['age_group_predicted']
    df_age_res['age_group_predicted'] = df_age_res['age_group_predicted'].apply(lambda x : age_grouping(x))
    df_age_res = pd.concat([test_data[['Device_id']],df_age_res], axis=1)
    df_age_res['action_campaign'] = df_age_res['age_group_predicted'].apply(lambda x:campaing_age[x] )
    df_age_res= df_age_res.to_json()
    return df_age_res



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
