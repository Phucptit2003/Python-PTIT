def sieve_of_eratosthenes(n):
    # Tạo một danh sách chứa tất cả các số từ 2 đến n
    numbers = [True] * (n + 1)
    numbers[0] = numbers[1] = False

    # Bắt đầu từ số 2, lặp qua tất cả các số từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if numbers[i] == True:
            # Đánh dấu tất cả các bội số của i từ i*i đến n là False
            for j in range(i*i, n+1, i):
                numbers[j] = False

    # Tạo một danh sách các số nguyên tố từ danh sách numbers
    primes = [num for num, is_prime in enumerate(numbers) if is_prime]

    return primes
n = 100
prime_numbers = sieve_of_eratosthenes(n)
print(prime_numbers)
