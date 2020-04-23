def add(m1, m2):
    m3 = []
    for r1,r2 in zip(m1,m2):     
        m3.append([c1 + c2 
                   for c1,c2 
                   in zip(r1,r2)])
    return m3
