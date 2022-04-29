## Exercise 4

The code below is of poor quality. Improve it (you may rewrite it to R, if you find it more convenient). [Data (StudentsPerfomance.csv) is available on Kaggle.](https://www.kaggle.com/spscientist/students-performance-in-exams)

*note: the code contains comments to make you understand what you should do, even if you are not very familiar with Python. They may not be the best comments possible...*
```

import pandas as pd
import matplotlib.pyplot as plt

# read the file with data
studPerformance = pd.read_csv('StudentsPerformance.csv')

# the dataframe contains data about 5 groups
stud_a = studPerformance.loc[studPerformance['race/ethnicity'] == 'group A']
stud_b = studPerformance.loc[studPerformance['race/ethnicity'] == 'group B']
stud_c = studPerformance.loc[studPerformance['race/ethnicity'] == 'group C']
stud_d = studPerformance.loc[studPerformance['race/ethnicity'] == 'group D']
stud_e = studPerformance.loc[studPerformance['race/ethnicity'] == 'group E']

# print mean math score for each group
groupa = stud_a['math score'].mean()
groupb = stud_b['math score'].mean()
groupc = stud_c['math score'].mean()
groupd = stud_d['math score'].mean()
groupe = stud_e['math score'].mean()

# print mean math, reading, and writing scores for students who completed the test preparation course and their parent obtained a degree
degree_test = studPerformance.loc[(studPerformance['test preparation course'] == 'completed') & (studPerformance['parental level of education'].isin(["associate's degree", "bachelor's degree", "master's degree"]))]
print('math', degree_test['math score'].mean())
print('reading', degree_test['reading score'].mean())
print('writing', degree_test['writing score'].mean())

# plot the histogram of math scores divided by reading scores for each student
plt.hist(studPerformance['math score'] / studPerformance['reading score'])
plt.title('ratio')
plt.show()
plt.close()
