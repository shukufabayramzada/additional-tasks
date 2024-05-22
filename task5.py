def isprime(k):
	if k == 1:
		return False
	for j in range(2, int(k**0.5)+1):
		if k % j == 0:
			return False
	return True
def main():
	n = 34
	for i in range (1, n+1):
		if(isprime(i) == True):
			print(i)
if __name__ == "__main__":
	main()