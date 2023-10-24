def rank(m):
    row_ind = 0
    for i in range(len(m[0])):
        flag = False
        for j in range(row_ind, len(m)):
            if m[j][i] != 0:
                flag = True
                m[row_ind], m[j] = m[j], m[row_ind]
                break
        if flag:
            for j in range(row_ind + 1, len(m)):
                factor = m[j][i] / m[row_ind][i]
                for k in range(i, len(m[0])):
                    m[j][k] -= m[row_ind][k] * factor
            row_ind += 1
    rang = min(len(m), len(m[0]), row_ind)
    return rang
