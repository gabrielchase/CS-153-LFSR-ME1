def get_binary(val):
    return '{:b}'.format(int(val))

def xor(a, b):
    return bool(a) != bool(b)
    
assert not xor(0, 0)
assert not xor(1, 1)
assert xor(0, 1)
assert xor(1, 0)


if __name__ == '__main__':
    clock = 0
    
    test_cases = int(input('Enter number of test cases: '))
    
    while(count < test_cases):
        m_input, s_input, p_input = input().split()
        
        m = get_binary(m_input)
        s = get_binary(s_input)
        p = get_binary(p_input)

        clock += 1 