import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# print(census.head())

# print(census.dtypes)

# print(census.birth_year.unique())

census.birth_year = census.birth_year.replace('missing', '1967')
# print(census.birth_year.unique())

census.birth_year = census.birth_year.astype('int64')
# print(census.dtypes)

# print(census.birth_year.mean())

order= ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree']

census.higher_tax = pd.Categorical(
  census.higher_tax,
  order,
  ordered=True
)
# print(census.higher_tax.unique())

census.higher_tax = census.higher_tax.cat.codes
# print(census.higher_tax.median())

ohe_marital_status= pd.get_dummies(
  data=census,
  columns=['marital_status']
)
# print(ohe_marital_status.head())

order= census.marital_status.unique()
census.marital_status = pd.Categorical(
  census.marital_status,
  order,
  ordered=False
)
marital_codes= census.marital_status.cat.codes
# print(marital_codes)

def get_age_groups(max_age):
  age_groups= []
  init_age= 0
  while init_age < max_age:
    format_str= '{}-{}'.format(init_age, init_age + 4)
    age_groups.append(format_str)
    init_age+= 5
  return age_groups
# age_groups= get_age_groups(max_age=100)
# print(age_groups)

def filter_by_age_group(row, max_age=100, current_year=2022):
  age_groups= get_age_groups(max_age)
  age= current_year-row
  index= int(age/5)
  return age_groups[index]

census['age_group']= census.birth_year.apply(filter_by_age_group)
# print(census.head())
