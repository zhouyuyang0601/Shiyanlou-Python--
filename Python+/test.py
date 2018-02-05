salary= input()
#
taxincome=salary-3500
print(taxincome)
# Decide range
range= [1500,4500,9000,35000,55000,80000]
taxrate= [3,10,20,25,30,35,45]
taxdect= [0,105,555,1005,2755,5505,13505]
#
if taxincome <0:
        tax =0
if taxincome<=1500:
        tax = taxincome*taxrate(0)*0.01-taxdect(0)
elif taxincome >=80000:
        tax = taxincome*taxrate(7)*0.01-taxdect(7)
                else taxincome <=range[i] and taxincome >range[i-1]: 
                        tax = taxincome*taxrate(i+1)*0.01-taxdect(i+1)
                
print(tax)
