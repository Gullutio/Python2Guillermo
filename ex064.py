print('hello I am your friendly neighbourhood discount amongus bot! aai will show you my sussy offers!')

percent = 0.6  # This contains 60% for the 60% off discount
# This is the leftover of 60%, aka 40% to make 100. It is used for the discount value
dis_amount = 0.4
val = 4.95  # this is the initial value.
print('Here is my discount table!!!')
print('-------------------------------------------------------------------------------------')
for i in range(5):  # repeats the code below 5 times to get the 5 values
    print(
        f'Value before discount: {val:<7.2f} | New price: {val*percent:<7.2f} | Discount value: {(val*dis_amount):<7.2f}')  # prints the value of the discount the new price and the dicount value
    val = val + 5  # every time it adds 5 to the initial value until it reaches 24.95. Can you see the pattern? Every number is 5 more than the last one

 # {sus: 10.3f}
