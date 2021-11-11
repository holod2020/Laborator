def bank(a, years):
    depsit = a
    koef = 1.1
    year = 1
    while (year <= years):
        depsit = koef * depsit
        year += 1
    return depsit