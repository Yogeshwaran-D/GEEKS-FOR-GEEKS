
def max_sum(arr,n):
    sum_val = 0
    prev_sum = 0
    for i in range(n):
        prev_sum += i * arr[i]
        sum_val += arr[i]
    ans = prev_sum
        
    for i in range(1, n):
        curr_sum = prev_sum - (sum_val - arr[i-1]) + arr[i-1] * (n-1)
        prev_sum = curr_sum
        if curr_sum > ans:
            ans = curr_sum
    return ans