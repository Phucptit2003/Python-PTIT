#bai 1
def check_a(a):
    return a % 3 == 0 and 50 <= a <= 100

#bai 2
def check_integer(a):
    return int(a) == a

#bai 3
def calculate_and_check_d(a, b, c):
    d = (a + b) ** c
    return 100 <= d <= 200

#bai 4
def solve(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return x
    else:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            return x1, x2
        elif delta == 0:
            x = -b / (2 * a)
            return x
        else:
            return "Phương trình vô nghiệm"

#bai 5
def days_in_month(month, year):
    if 1 <= month <= 12:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return 30

#bai 6
def Count_score(math_score, literature_score, english_score):
    if math_score >=0 and math_score<=10 and literature_score>=0 and literature_score<=10 and english_score>=0 and english_score<=10:
        average_score = (math_score + literature_score + english_score) / 3
        if (
            average_score >= 8
            and (math_score >= 8
            or literature_score >= 8)
            and english_score >= 6.5
            and math_score>=6.5
            and literature_score>=6.5
        ):
            return "Học sinh giỏi"
        elif (
            average_score >= 6.5
            and( math_score >= 6.5
            or literature_score >= 6.5)
            and english_score >= 5
            and math_score>=5
            and literature_score>=5
        ):
            return "Học sinh khá"
        elif (
            average_score >= 5
            and (math_score >= 5
            or literature_score >= 5)
            and english_score >= 3.5
            and math_score>=3.5
            and literature_score>=3.5
        ):
            return "Học sinh trung bình"
        elif (
            average_score >= 3.5
            and( math_score >= 3.5
            or literature_score >= 3.5)
            and english_score >= 2
            and math_score>=2
            and literature_score>=2
        ):
            return "Học sinh yếu"
        else:
            return "Học sinh kém"

#bai 7
def calculate_sum(n):
    return n*(n+1)//2

#bai 8
def print_factors(a):
    factors = []
    for i in range(1, a + 1):
        if a % i == 0:
            factors.append(i)
    return factors

#bai 9
def print_common_factors(a, b):
    common_factors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)
    return common_factors

#bai 10
def find_largest_fibonacci(A):
    fib = [1, 1]
    while True:
        next_fib = fib[-1] + fib[-2]
        if next_fib > A:
            return fib[-1]
        fib.append(next_fib)

# bai 11
def find_max_min_numbers():
    numbers = []
    while True:
        num = int(input())
        if num == -1:
            break
        numbers.append(num)
    return max(numbers), min(numbers)

#bai 12
def assign_rooms(N, M, doankhach):
    rooms = [0] * N  
    result = []

    for guests in doankhach:
        while guests > 0:
            assigned = False
            for i in range(N):
                if rooms[i] == 0:
                    rooms[i] = 2 if guests >= 2 else 1
                    guests -= rooms[i]
                    result.append(rooms[i])
                    assigned = True
                    break
            if not assigned:
                rooms.append(1)
                result.append(1)

    return result

#bai 13
prices = {
    "Gà rán": 30000,
    "Hamburger": 25000,
    "Cocacola": 10000
}

def calculate_item_total(item, quantity):
    if item in prices:
        return prices[item] * quantity
    else:
        return 0

def calculate_subtotal(order):
    subtotal = 0
    for item, quantity in order.items():
        subtotal += calculate_item_total(item, quantity)
    return subtotal


def calculate_tax(subtotal):
    return 0.1 * subtotal

def calculate_total(subtotal, tax):
    return subtotal + tax

def main():
    
    while True:
        choices = int(input(f"Chon bai: "))
        if choices== 1:
            a = int(input())
            result = check_a(a)
            print(result)
        elif choices==2:
            a = float(input())
            result = check_integer(a)
            print(result)
        elif choices== 3:
            a = float(input())
            b = float(input())
            c = float(input())
            result = calculate_and_check_d(a, b, c)
            print(result)
        elif choices==4:
            a = float(input())
            b = float(input())
            c = float(input())
            result = solve(a, b, c)
            print(result)
        elif choices== 5:
            month = int(input())
            year = int(input())
            result = days_in_month(month, year)
            print(result)
        elif choices== 6:
            math_score = float(input())
            literature_score = float(input())
            english_score = float(input())
            result = Count_score(math_score, literature_score, english_score)
            print(result)
        elif choices== 7:
            n = int(input())
            result = calculate_sum(n)
            print(result)
        elif choices== 8:
            a = int(input())
            result = print_factors(a)
            print(result)
        elif choices==9:
            a = int(input())
            b = int(input())
            result = print_common_factors(a, b)
            print(result)
        elif choices== 10:
            A = int(input())
            result = find_largest_fibonacci(A)
            print(result)
        elif choices== 11:
            max_num, min_num = find_max_min_numbers()
            print(max_num)
            print(min_num)
        elif choices==12:   
            N,M=map(int,input().split())       
            s=input().split()
            doankhach=[int(s) for s in s]

            result = assign_rooms(N, M, doankhach)

            print()
            for i, num in enumerate(result):
                print(num,end=' ')
            
        elif choices== 13:
            order = {}
            while True:
                item = input().strip()
                if not item:
                    break
                quantity = int(input())
                order[item] = order.get(item, 0) + quantity

            subtotal = calculate_subtotal(order)
            tax = calculate_tax(subtotal)
            total = calculate_total(subtotal, tax)

            for item, quantity in order.items():
                item_total = calculate_item_total(item, quantity)
                print(f"{item}: {quantity} x {prices[item]}đ = {item_total}đ")
            
            print(subtotal)
            print(tax)
            print(total)
        
        else:
            break

if __name__ == "__main__":
    main()
