def string_equals(str1, str2):

    if len(str1) != len(str2):
        return False

    else:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
    return True



a = "abcd "
b = "abcd"

print(string_equals(a, b))