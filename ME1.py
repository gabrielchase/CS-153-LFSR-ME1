def get_binary(val):
    return '{:b}'.format(int(val))

def xor(binary_string):
    # if even number of 1's, always 0
    # if odd number of 1's, always 1
    if bool(a) != bool(b):
        return 1
    else:
        return 0

def get_output_val(clock, m, p, output):
    val = 0
    i = clock - m
    for idx in range(1, m+1):
        s_index = i + m - idx
        s_val = output[s_index]
        print('s at {}: {}'.format(s_index, s_val))
        
        p_index = m - idx
        p_val = p[p_index]
        print('p at {}: {}'.format(p_index, p_val))

        val += int(s_val) * int(p_val)
        print('val at {}: {}'.format(idx, val))
        print()
    return str(val % 2)


        
        
# val = get_output_val(7, 3, '011', '0010111')
# print('FINAL: {}'.format(val))



if __name__ == '__main__':
    output = ''
    clock = 0

    # test_cases = int(input('Enter number of test cases: '))
    
    
    m, s_input, p_input = input().split()
    
    while(clock < (2**int(m)-1)):    
        s = get_binary(s_input)
        p = get_binary(p_input).zfill(4)

        output += s[::-1]
        clock += len(s)

        print(p)
        print(output)
        
        new_val = get_output_val(clock, int(m), p, output)
        output += new_val
        print('clock: {} | output: {}'.format(clock, output))

        clock += 1 