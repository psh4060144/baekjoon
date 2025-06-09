bkj = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
arr = [-1] * 26

###########################################################

# 1. 덮어 쓰기를 막는다

for ab in range(len(bkj)):
    for cd in range(len(alphabet)):
        if bkj[ab] == alphabet[cd] and arr[cd] == -1:
            arr[cd] = ab

print(arr)

###########################################################

# 2-1. 덮어 쓰는 일을 만들지 않는다. 어떻게? 중복 제거 해서.
# set를 쓰면 될 것 같은데, 그러면 순서가 뒤죽박죽이 된다.
# 순서를 유지하며 중복을 제거하는 걸 어떻게 할까? 중복이 없는 새 list 를 만들어서 비교해 보자.

temp = []

for ab in range(len(bkj)):
    if bkj[ab] in temp:
        continue
    else:
        temp.append(bkj[ab])
    for cd in range(len(alphabet)):
        if bkj[ab] == alphabet[cd] and arr[cd] == -1:
            arr[cd] = ab

print(arr)

###########################################################

# 2-2. 덮어 쓰는 일을 만들지 않는다. 어떻게? target 단어와 pattern 단어를 바꿔서.
# 중복이 있는 글자를 가져와서 비교하는 건 이미 문제가 있다.
# 중복 없는 string 의 글자를 가져와서 비교하는 건 가능하다.

for ab in range(len(alphabet)):
    for cd in range(len(bkj)):
        if alphabet[ab] == bkj[cd]:
            arr[ab] = cd
            break

print(arr)