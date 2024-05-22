for n in range(100, 401, 2):
    if (n // 100 ) % 2  == 0 and (n % 100 // 10) %2 == 0:
        print ("{}".format(n), end= ', ' if n != 400 else "\n")