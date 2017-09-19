digit_value = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}
for t in xrange(input()):
    n = input()
    nums = raw_input().split()
    min_sum = 42,'888888'
    for digits in nums:
        digits_sum = 0
        for ch in digits:
            digits_sum += digit_value[ch]
            if digits_sum > min_sum[0]:
                break
        if digits_sum < min_sum[0]:
            min_sum = digits_sum,digits
    print min_sum[1]
