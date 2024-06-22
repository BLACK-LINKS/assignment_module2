sentence = "This is a sample sentence. This sentence contains some words."

counting = {}
words = sentence.split()

for w in words:
    if w in counting:
        counting[w] += 1
    else:
        counting[w] = 1

print(counting)
