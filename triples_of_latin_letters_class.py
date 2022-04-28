from string import ascii_lowercase


class Triple:
    def __init__(self, num):
        counter_i = 0
        counter_j = 0
        counter_k = 0
        for i in ascii_lowercase:
            counter_i += 1
            if counter_i > num:
                break
            for j in ascii_lowercase:
                counter_j += 1
                if counter_j > num:
                    counter_j = 0
                    break
                for k in ascii_lowercase:
                    counter_k += 1
                    if counter_k > num:
                        counter_k = 0
                        break
                    print(f"{i}{j}{k}")


obj = Triple(num=int(input()))
