import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
sales_data = pd.read_csv(r"sales_data.csv")
print(sales_data.head(10))

#Missing values
Missing_values  = sales_data.isnull().sum()
print(Missing_values)

#Duplicate values
Duplicate_Values = sales_data.duplicated().sum()
print(Duplicate_Values)

#Graph
sns.displot([0,1,2,3,4,5,6,7,8,9])
plt.show()  