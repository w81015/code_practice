driving = input('你沒有沒開過車？')
if driving != '有' and driving != '沒有':
	prin('共能輸入 有/沒有')
	raise SystemExit

age = input('你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪，你怎麼會開過車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了')
	else:
		print('很好，再過幾年就可以考駕照了')
else: 
	print('只能輸入 有/沒有')
	
