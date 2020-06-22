# Simple Machine Learning with Python SciKit-learn

A simple script that trains from a list of temperature/humidity classifications, and is able to assess if an environment is comfortable or uncomfortable.

## Instructions

Install SciKit and make a virtual environment:

`python3 -m venv sklearn-venv`\
`sklearn-venv\Scripts\activate`\
`pip install -U scikit-learn`\
`pip install panda`\
`pip install xlrd`

## Run the script:

`python3 temperatures-classifier.py`

## Example output:

```
Temperatures classifier
Training from spreadsheet
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