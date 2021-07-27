def solution_my(N, stages):
    dict_a = {}
    answer = []
    for stage in range(N):
        stage = stage + 1
        pass_p = 0
        fail_p = 0
        for person in stages:
            if person >= stage:
                pass_p += 1
            if person == stage:
                fail_p += 1
        if (fail_p != 0) and (pass_p != 0):
            dict_a[stage] = fail_p/pass_p
        else:
            dict_a[stage] = 0
    list_of_key = list(dict_a.keys())
    list_of_value = list(dict_a.values())
    for value in range(len(list_of_key)):
        max_value = max(list_of_value)
        position = list_of_value.index(max_value)
        answer.append(list_of_key[position])

        list_of_value.remove(max_value)
        del list_of_key[position]

    return answer


def solution_a(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)

#sorted(result.items())

#sorted(result.items(), reverse=True)

#sorted(result.items(), key=lambda x : x[1])

#sorted(result.items(), key=lambda x : x[1], reverse=True)

#sorted(result)

#sorted(result, reverse=True)

#sorted(result, key=lambda x : result[x], reverse=True)


