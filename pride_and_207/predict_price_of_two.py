import csv
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

car_name_model = []
car_price = []

with open('2p_data.csv') as csvfile:
    data = csv.reader(csvfile)
    next(data) 
    for line in data:
        if line[0:2] and line[4]:
            car_name_model.append(' '.join(line[0:2])) 
            car_price.append(int(line[4])) 

label_encoder = LabelEncoder()
car_name_model_encoded = label_encoder.fit_transform(car_name_model).reshape(-1, 1)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(car_name_model_encoded, car_price)

    
new_data = ['پراید', '111']
new_data_combined = [' '.join(new_data)]
new_data_encoded = label_encoder.transform(new_data_combined).reshape(-1, 1)

answer = clf.predict(new_data_encoded)
print(f"{answer[0]} T")
