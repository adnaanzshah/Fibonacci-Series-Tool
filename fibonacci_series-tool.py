# f_2=f_0+f_1
# f_n=f_n_1+f_n_2

l_i=int(input("Enter the last index for Fibonacci Series : "))
def create_fibonacci_series(l_i):
    fb_series=[0,1]
    # fb_series[1]=0
    # fb_series[2]=1

    i=2
    while i<l_i:
        x=fb_series[i-1]+fb_series[i-2]
        # print("Iteration Number : ",i)
        # print()
        fb_series.append(x)
        # print("Element : ",fb_series[i])
        # print()
        i+=1
    print(fb_series)
    return fb_series

fibonacci_series=create_fibonacci_series(l_i)
y=int(input("Enter the iteration for the fibonacci series you want : "))
def get_fb_num_at_index(fb_series,y):
    print(fb_series[y])
    return y

get_fb_num_at_index(fibonacci_series,y)