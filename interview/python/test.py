import re

def solution(min_cheermote_amount, valid_cheermotes, messages):
    s = " ".join(valid_cheermotes)
    total = 0
    lst = []
    
    for msg in messages.split():
        if s in msg:
            match = re.match(r"([a-z]+)([0-9]+)", msg, re.I)
            
            if match:
                items = match.groups()
            
                if int(items[1]) <= 10000 and min_cheermote_amount: 
                    total += int(items[1])
                    
                elif int(items[1]) in range (10000, 100001) and \
                    min_cheermote_amount:
                    total += 0
                    
    
    return ["NO_CHEERS"] if s not in messages else [s + str(total)]


def test1():
	assert solution(1, ['cheer'], 'roo100 big1000') == ["NO_CHEERS"]

def test2():
	assert solution(1, ["cheer"], "this is just a normal message and also cheer100 cheer100") == ["cheer200"]

def test3():
	assert solution(1, ["cheer"], "cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer10000 cheer1, cheer4") == "cheer4"
	