name_list=[]
sum_list=[]
highest_name=[]
highest_ems=[]
lowest_name=[]
lowest_ems=[]
for name,income_group in test:
    name_list.append(name)
    sum_list.append(income_group['CO2 sum emission'].sum())
    highest_name.append(income_group['CO2 sum emission'].idxmax())
    highest_ems.append(income_group['CO2 sum emission'].max())
    lowest_name.append(income_group['CO2 sum emission'].idxmin())
    lowest_ems.append(income_group['CO2 sum emission'].min())
column_name=['Sum emissions','Highest emission country','Highest emissions','Lowest emission country','Lowest emissions']
results=DataFrame(list(ip(sum_list,highest_name,highest_ems,lowest_ems,lowest_name)),columns=column_name,index=name_list)