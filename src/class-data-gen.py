import pandas as pd
!pip install git+git://github.com/clintval/gender_predictor.git
from gender_predictor import GenderPredictor

col1 = []
col1.append('Alexis Chau')
col1.append('Owen Koh Lee')
col1.append('Julia Mason')
col1.append('Jeremiah-David Addai')
col1.append('Melissa Shun')
col1.append('Sarah Ali')
col1.append('Ethan Chen')
col1.append('Braxton Hoang')
col1.append('Kyle Lee')
col1.append('Bill Cheng')
col1.append('Winston Li')
col1.append('Michael Tovmasyan')
col1.append('Jolene Huey')
col1.append('Timothy Sujo')
col1.append('Axel Galicia Lona')
col1.append('Anthony Ge')
col1.append('Eric Yang')
col1.append('Julia Wong')
col1.append('Andrew Sung')
col1.append('Jeffrey Chou')
print(len(col1))
data_dict = {}
data_dict['Name'] = col1
print(len(data_dict['Name']))

col2 = []
col2.append('Arcadia High School')
col2.append('Arcadia High School')
col2.append('None')
col2.append('Sage Oak Charter High School')
col2.append('Ramona Convent Secondary School')
col2.append('Granada Hills Charter High School')
col2.append('Chaminade College Prep')
col2.append('Arcadia High School')
col2.append('Temple City High School')
col2.append('Arcadia High School')
col2.append('Arcadia High School')
col2.append('Arcadia High School')
col2.append('None')
col2.append('Arcadia High School')
col2.append('Ontario High School')
col2.append('None')
col2.append('Irvine High School')
col2.append('Arnold O Beckman High School')
col2.append('Troy High School')
col2.append('Temple City High School')

data_dict['High School'] = col2
print(len(data_dict['High School']))

col3 = []
col3.append(9)
col3.append(9)
col3.append(10)
col3.append(9)
col3.append(10)
col3.append(10)
col3.append(9)
col3.append(9)
col3.append(9)
col3.append(10)
col3.append(10)
col3.append(12)
col3.append(10)
col3.append(11)
col3.append(12)
col3.append(10)
col3.append(10)
col3.append(9)
col3.append(9)
col3.append(9)
print(len(col3))

data_dict['Grade'] = col3
print(len(data_dict['Grade']))

# Getting the gender

gen = GenderPredictor()
gen.train_and_test()

col4 = [gen.classify(i.split(" ")[0]) for i in col1]
print(col4)
data_dict['Gender'] = col4

df = pd.DataFrame.from_dict(data_dict)
df.head()
df.replace('M', 'male', inplace=True)
df.replace('F', 'female', inplace=True)
df.to_csv("data/m132-student-data.csv")
