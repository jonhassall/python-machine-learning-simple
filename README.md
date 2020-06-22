# Simple Machine Learning with Python SciKit-learn

A simple script that trains from a list of temperature/humidity classifications, and is able to assess if an environment is comfortable or uncomfortable.

## Instructions

Install SciKit and make a virtual environment:

`python3 -m venv sklearn-venv`
`sklearn-venv\Scripts\activate`
`pip install -U scikit-learn`
`pip install panda`
`pip install xlrd`

## Run the script:

`python3 temperatures-classifier.py`

## Example output:

```
Temperatures classifier
Training from spreadsheet
18.3 22 Yes
18.3 60 No 
26.7 25 Yes
26.7 50 Yes
26.7 52 No 
26.7 24 No 
26.7 30 Yes
18.3 50 Yes
18.3 20 No 
22.0 20 No 
22.0 32 Yes
22.0 70 No 
22.0 65 No 
22.0 90 No
25.0 90 No
25.0 10 No
25.0 15 No
20.0 15 No
20.0 92 No
27.0 50 No
27.0 25 No
27.0 10 No
27.0 75 No
27.0 100 No
17.0 100 No
17.0 50 No
17.0 25 No
12.0 50 No
Training complete

Enter a temperature and humidity to check if it is comfortable using this trained model:
Please enter a temperature in celcius:
20
Please enter a humidity in celcius:
44
Checking if 20.0C at 44.0 humidity is comfortable:
['Yes']
End of script
```