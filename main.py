def calculate_hits(ans, word):
  required = []
  for i, (ans_ltr, word_ltr) in enumerate(zip(ans, word)):
    if ans_ltr == word_ltr:
      required.append(i)

  moving = []
  for i, word_ltr in enumerate(word):
    idx = ans.find(word_ltr)
    if idx != -1:
      ans = ans[:idx] + ans[idx + 1:]
      moving.append(i)

  return required, moving