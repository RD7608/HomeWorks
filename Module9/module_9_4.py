def all_variants(s):
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            yield s[start:start+length]

a = all_variants("abc")
for i in a:
    print(i)
