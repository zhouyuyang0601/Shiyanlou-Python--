salary= input()
#
taxinc=int(salary-3500)
if taxinc <=0:
	tax=0
elif taxinc<=1500:
	tax=taxinc*0.3
elif taxinc>1500 and taxinc<=4500:
	tax=taxinc*0.1-105
elif taxinc>4500 and taxinc<=9000:
	tax=taxinc*0.20-555
elif taxinc>9000 and taxinc<=35000:
	tax=taxinc*0.25-1005
elif taxinc>35000 and taxinc<=55000:
	tax=taxinc*0.3-2755
elif taxinc>55000 and taxinc<80000:
	tax=taxinc*0.35-5505
elif taxinc>=80000:
	tax=taxinc*0.45-13505
print(tax)
	
