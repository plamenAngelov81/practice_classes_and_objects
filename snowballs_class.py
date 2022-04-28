class Snowball:
    def __init__(self, snowball_num):

        best_snowball = 0
        best_snowball_data = ""
        for snowball in range(1, snowball_num + 1):
            weight = int(input())
            time_need = int(input())
            current_quality = int(input())
            result = int(weight / time_need) ** current_quality
            if result > best_snowball:
                best_snowball = result
                best_snowball_data = f"{weight} : {time_need} = {result} ({current_quality})"

        print(best_snowball_data)


obj = Snowball(snowball_num=int(input()))

