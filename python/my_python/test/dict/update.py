

if __name__ == '__main__':
    a = {key : False for key in range(10)}
    func_list = {
        'len': len,
        'map': map,
        'sorted': sorted
    }

    b = {key : True for key in range(3)}
    bool_l = ['Yes', 'No']
    c = { key : value for key in range(3) for value in bool_l} # Can you understand that the value will
                                                               #will be overriden if their key has the same nam

    print a
    print func_list
    print func_list['len'](a)
    a.update(func_list)
    print a
    a.update(b)
    print a
    print c
