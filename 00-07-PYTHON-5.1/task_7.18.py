#!/usr/bin/python3

def exchange(usd=None, rub=None, rate=None):
    try:
        two_args = lambda arg1, arg2: True if (arg1 is not None and arg2 is not None) else False
        if usd is None:
            if two_args(rub, rate):
                return rub / rate
            else:
                raise ValueError('Not enough arguments')
        elif rub is None:
            if two_args(usd, rate):
                return usd * rate
            else:
                raise ValueError('Not enough arguments')
        elif rate is None:
            if two_args(usd, rub):
                return rub / usd
            else:
                raise ValueError('Not enough arguments')
        else:
            raise ValueError('Too many arguments')
    except ValueError as e:
        return e


def exchange_optimized(usd=None, rub=None, rate=None):
    """ Optimized ethalon solving """
    check_cnt = [usd, rub, rate].count(None)
    check_list = ['Too many arguments', None, 'Not enough arguments']
    if check_cnt != 1:
        raise ValueError(check_list[check_cnt])
    
    if usd is None:
        return rub / rate
    if rub is None:
        return usd * rate
    if rate is None:
        return rub / usd
