import pandas as pd

#loading dataset 
data = pd.read_csv("loan.csv")
print(data)

#Classifier function
def condition(age,creditscore,income):
    if creditscore>=70:
        return True
    elif income>=50 and age>=30:
        return True
    else:
        return False
    
predictions = []
for i in range(len(data)):
    row=data.iloc[i]
    predictions.append(condition(row["Age"],row["CreditScore"],row["Income"]))

data["Predicted"]=predictions
print(data)
