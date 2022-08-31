def get_age_groups(max_age):
  age_groups= []
  init_age= 0
  while init_age < max_age:
    format_str= '{}-{}'.format(init_age, init_age + 4)
    age_groups.append(format_str)
    init_age+= 5
  return age_groups
age_groups= get_age_groups(max_age=100)
print(age_groups)
