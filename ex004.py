print('yO PUt Ur farmland\'s WIDtH aND LeNGTh (in square feet) SO dA ComPUTeR CAn caLCUlaTE iT...|')
print('='*79 + ('=|'))
width = input('WhAT Is ThE widTh oF uR land? ')
length = input('WhAT Is ThE LengTh oF uR land ')
answer_square_feet = float(width) * float(length)
answer_acres = float(answer_square_feet) / 43560
print('There are '+str(answer_acres)+' acres in your land.')
