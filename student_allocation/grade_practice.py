grade = input('請輸入年級: ')
grade = int(grade)
if grade >= 1 and grade <= 5:
	print('屬於PYP')
elif grade >= 6 and grade <= 10:
	print('屬於MYP')
elif grade >= 11 and grade <= 12:
	print('屬於DP')
else:
	print('不適用IB') 