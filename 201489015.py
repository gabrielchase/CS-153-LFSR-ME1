def get_binary(val):
    return '{:b}'.format(int(val))

def get_max_runs(m):
    return (2**int(m))-1

# Si+m = Si+(m-1) * Pm-1 + Si+(m-2) * Pm-2 + Si+(m-3) * Pm-3 ... + Si+(m-n) * P0 % 2
def get_output_val(clock, m, p, output):
    val = 0
    i = clock - m
    for idx in range(1, m+1):
        s_index = i + m - idx
        s_val = output[s_index]
        
        p_index = m - idx
        p_val = p[p_index]

        val += int(s_val) * int(p_val)
    
    return str(val % 2)


if __name__ == '__main__':
    output = ''
    clock = 0
    runs = 0
    
    test_cases = int(input())

    while(runs < test_cases):
        print('case {}:'.format(runs+1))
        m, s_input, p_input = input().split()
        m = int(m)
        max_runs = get_max_runs(m)
        
        s = get_binary(s_input).zfill(m)
        p = get_binary(p_input).zfill(m)[::-1]
        
        output += s[::-1]
        
        for idx, o in enumerate(output):
            print('clock: {}, value: {}'.format(idx, o))
        
        clock += len(s)
            
            
        while(clock < max_runs+1):
            new_val = get_output_val(clock, int(m), p, output)
            output += new_val
            s = new_val + s
            print('clock: {}, value: {}'.format(clock, new_val))
            

            clock += 1 

        output = ''
        clock = 0
        s = ''
        p = ''
            
        print()
        runs += 1
