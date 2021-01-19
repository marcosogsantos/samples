import itertools
perms = []
def combos(chars, length):
  if length == 0:
    yield ''
    return
  for char in chars:
    for combo in combos(chars, length-1):
      yield char + combo

perms = list(combos('lh',18))
open('perms.txt','w').write('[\n')
for p in perms:
  open('perms.txt','a').write(str(tuple(list(p)))+',\n')
print('Done!')
open('perms.txt','a').write('\n]')
