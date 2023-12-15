def maximum_subsequence_count(text, pattern):
    res = 0
    cnt1 = 0
    cnt2 = 0

    for c in text:
        if c == pattern[1]:
            res += cnt1
            cnt2 += 1
        if c == pattern[0]:
            cnt1 += 1

    return res + max(cnt1, cnt2)

if __name__ == "__main__":
    text = input("Enter text: ")
    pattern = input("Enter pattern: ")

    result = maximum_subsequence_count(text, pattern)
    print(result)
