if __name__ == '__main__':
    colors = ['red', 'pink', 'yellow', 'purple', 'green']
    clothes = ['shirt', 'pant', 'jacket', 'hoodie']

    my_clothes = ['{0} {1}'.format(co, cl) for co in colors for cl in clothes]
    print my_clothes
