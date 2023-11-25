def find_divisors(number: int):
    '''
    Function returns list of entered number divisors
    '''
    return [i for i in range(1, number+1) if number % i == 0]
