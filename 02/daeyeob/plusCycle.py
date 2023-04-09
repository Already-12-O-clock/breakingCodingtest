n = correct_num = int(input())
cycle_length = 0

while (1):
		
		single_digit = n % 10
		tenth_digit = n//10
		sum = tenth_digit + single_digit
		sum_single_digit = sum % 10
		n = str(single_digit) + str(sum_single_digit)
		n = int(n)
		cycle_length += 1
		
		if correct_num == n:
			break
			
print(cycle_length)