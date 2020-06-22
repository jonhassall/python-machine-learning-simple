print("Health classifier")

# Classify healthy and unhealthy food
# Fat%, Protein%, Carbohydrates%

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[0, 0, 0],
[0, 10, 0],
[0, 10, 25],
[0, 0, 25],
[5, 0, 0],
[5, 10, 0],
[5, 10, 25],
[5, 0, 25],
[10, 0, 0],
[10, 10, 0],
[10, 10, 25],
[10, 0, 25],
[11, 0, 0],
[11, 10, 0],
[11, 10, 25],
[11, 0, 25],
[11, 0, 0],
[11, 10, 0],
[11, 10, 25],
[11, 0, 25],
[11, 0, 0],
[11, 10, 0],
[11, 10, 25],
[11, 0, 25],
[0, 0, 26],
[0, 10, 26],
[0, 10, 26],
[0, 0, 26],
[5, 0, 26],
[5, 10, 26],
[5, 10, 26],
[5, 0, 26],
[10, 0, 26],
[10, 10, 26],
[10, 10, 26],
[10, 0, 26]]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # classes of each sample
clf.fit(X, y)

# print(clf.predict(X))  # predict classes of the training data

# Test for healthy products
# 0 = healthy, 1 = unhealthy
print(clf.predict([[5, 2, 16]]))
print(clf.predict([[3, 25, 16]]))
print(clf.predict([[3, 25, 2]]))
print(clf.predict([[3, 25, 60]]))
print(clf.predict([[30, 2, 16]]))
print(clf.predict([[40, 2, 8]]))
print(clf.predict([[2, 2, 80]]))
print(clf.predict([[2, 60, 80]]))

def is_healthy(fat, protein, carbohydrates):
    print("Analyzing product with Fat: " + str(fat) + "% Protein: " + str(protein) + "% Carbohydrates: " + str(carbohydrates) + "%")
    if clf.predict([[fat, protein, carbohydrates]]) == 0:
        print("Healthy")
    else:
        print("Unhealthy")

is_healthy(5, 2, 16)
is_healthy(3, 25, 16)
is_healthy(3, 25, 2)
is_healthy(3, 25, 60)
is_healthy(30, 2, 16)
is_healthy(40, 2, 8)
is_healthy(2, 2, 80)
is_healthy(2, 60, 80)
is_healthy(6, 25, 12)
