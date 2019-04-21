from flask import request
from sklearn.externals import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score

def predict_diabetes_stuff():
    if request.method == 'POST':
        model_knn = joblib.load("models/diabetes_predictor_models/diabetes_knn_model.pkl")
        
        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose= int(request.form.get('Glucose'))
        BloodPressure= int(request.form.get('BloodPressure'))
        SkinThickness= int(request.form.get('SkinThickness'))
        Insulin= int(request.form.get('Insulin'))
        BMI= float(request.form.get('BMI'))
        DiabetesPedigreeFunction= float(request.form.get('DiabetesPedigreeFunction'))
        Age= int(request.form.get('Age'))

        
        Outcome= 0

        diabetes_data = [Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age,
        Outcome]

        df = pd.read_csv('models/diabetes_predictor_models/diabetes.csv')
        df.loc[769] = [i for i in diabetes_data]

        y = df.Outcome.values
        x_data = df.drop(['Outcome'], axis = 1)
        x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values
        #x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=0)
        ##print(x.loc[1].values)

        data_to_predict = x.loc[0].tolist()
        print(data_to_predict)
        predicted_result = model_knn.predict([data_to_predict])
        print(predicted_result)
        if predicted_result[0]==0:
        	result='The person does not have diabetes'
        else:
        	result = 'The person have diabetes'

        training_accuracy = []
        test_accuracy = []
        # try n_neighbors from 1 to 10
        """
        neighbors_settings = range(1, 11)
        for n_neighbors in neighbors_settings:
        	knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        	knn.fit(x_train, y_train)
        	training_accuracy.append(knn.score(x_train, y_train))
        	test_accuracy.append(knn.score(data_to_predict, predicted_result))
        """
        return result

		  
