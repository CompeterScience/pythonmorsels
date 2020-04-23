def add(m1, m2):
    m3 = []
    for r in range(len(m1)):
        m3.append([])
        for c in range(len(m1[0])):
            m3[r].append(m1[r][c] + m2[r][c])    
    return m3
