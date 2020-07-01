print("Temperatures classifier")

# Train a model of temperature/humidity comfort classifiers, and prompt for user input to test

import pandas as pd

print("Training from spreadsheet")

# Train temperature comfort classifier from XLSX file
data = pd.read_excel (r'temperatures-training.xlsx')
df = pd.DataFrame(data, columns= ['Temperature', 'Humidity', 'Comfortable'])

X = []
y = []
for index, row in df.iterrows():
    print (row["Temperature"], row["Humidity"], row["Comfortable"])
    X.append([row["Temperature"], row["Humidity"]])
    y.append(row["Comfortable"])

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X, y)

print("Training complete\n")

print("Enter a temperature and humidity to check if it is comfortable using this trained model:")
temperature = float(input("Please enter a temperature in celcius:\n"))
humidity = float(input("Please enter a humidity in celcius:\n"))

print("Checking if " + str(temperature) + "C at " + str(humidity) + ' humidity is comfortable:')
print(clf.predict([[temperature, humidity]]))

print("End of script")