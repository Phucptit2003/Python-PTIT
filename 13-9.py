def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

hours = float(input())
rate = float(input())
gross_pay = computepay(hours, rate)
print("Pay:","{:.2f}".format(gross_pay))

