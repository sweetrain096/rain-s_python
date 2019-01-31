def start_end(lists):
    result = 0
    for string in lists:
        if len(string) >= 2 and string[0]==string[-1]:
            result += 1
    return result

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))