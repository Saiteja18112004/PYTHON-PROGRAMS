stname=input("enter a stname")
sno=int(input("enter a value"))
group=input("enter group")
s1=float(input("enter s1"))
s2=float(input("enter s2"))
s3=float(input("enter s3"))
total=s1+s2+s3
avg=total/3
if avg>=90:
    print("O-grade")
elif avg>=80:
    print("A-grade")
elif avg>=70:
    print("B-grade")
elif avg>=60:
    print("C-grade")
elif avg>=50:
    print("D-grade")
else:
    print("pass")
