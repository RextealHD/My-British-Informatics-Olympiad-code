sentence = input("Input the digits")
words = sentence.split()
debt = 100
total_interest = 0
counter = 0
interest_percentage = int(words[0])
interest_percentage_use = (interest_percentage/100)
repayment_percentage = int(words[1])
repayment_percentage_use = (repayment_percentage/100)


while debt != 0:
	interest = round((debt * interest_percentage_use), 2)
	debt = round((debt + interest), 2)
	print(interest)
	print(debt)
	repayment = round((debt * repayment_percentage_use), 2)
	if debt < 50:
		debt = debt - debt
	elif repayment < 50:
		debt = debt - 50
	else:
		debt = debt - repayment
	total_interest = total_interest + interest
	counter = counter + 1
	print(total_interest)


print(interest_percentage, " ", repayment_percentage)
print(total_interest)
print(counter)
