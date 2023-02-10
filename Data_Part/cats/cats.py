"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> choose(ps, s, 0)
    'hi'
    >>> choose(ps, s, 1)
    'fine'
    >>> choose(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i = 0
    select_list = []
    for i in range(len(paragraphs)):
        if select(paragraphs[i]) == True:
            select_list.append(paragraphs[i])
            # print(select_list)
        i += 1
    return select_list[k] if k <= (len(select_list)-1) else ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether
    a paragraph contains one of the words in TOPIC.

    Arguments:
        topic: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def helper(p):
        if bool(topic) == False:
            return False
        else:
            i = 0
            for i in range(len(topic)):
                if topic[i] in split(lower(remove_punctuation(p))):
                    return True
                i += 1
        return False
    return helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    Arguments:
        typed: a string that may contain typos
        reference: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')#accuracy("cats.", "cats")-->0.0
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')#区分大小写，一个单词只有大小写不一致也是错
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')#任意一方为空，另一方未非空，都是0.0
    0.0
    >>> accuracy('', '')
    100.0
    >>> accuracy("a b c d", "a d")
    25.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if bool(typed) == False :
        if bool(reference) == False:
            return 100.0
        else:
            return 0.0
    else:
        counter,i = 0,0
        for i in range(len(typed_words)):
            if i < len(reference_words):
                if typed_words[i] == reference_words[i]:
                    counter += 1
                i += 1
    return counter *100 / len(typed_words)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)# (type / 5)/(elapsed / 60)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return (len(typed)/5)/(elapsed / 60)
    # END PROBLEM 4


###########
# Phase 2 #
###########

def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. Instead returns TYPED_WORD if that difference is greater
    than LIMIT.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing reference words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    #autocorrect("inside", ["idea", "insider"], first_diff, 0.5)-->'idea'不是很懂、
    # "wor", ["worry", "car", "part"] 选car 不是很懂 不用懂……
    #         2/5=0.4，2/3=0.67,3/4=0.75 
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list:
        return typed_word
    else:
        result = [diff_function(typed_word, word,limit) for word in word_list]#这样iterate就不用写for来遍历了
        #上面这一句省了不知道多少代码
        min_diff = min(result)
        if min_diff > limit:
            return typed_word
        else:
            return word_list[result.index(min_diff)]
    """我的傻鸟代码，还做不出来
    pre_counter = 1000000000000
    lst_diff = []
    len_diff = []
    for i in range(len(word_list)):    
        if typed_word == word_list[i]:#一样
            return typed_word    
        lst_diff.append(diff_function(typed_word,word_list[i],limit))#构建个体差异值list        
        lst_type , lst_pre = list(typed_word),list(word_list[i])#[拆分单词成一个个字母，是list]
        len_diff.append(abs(len(lst_type)-len(lst_pre)))#长度差异构建
        counter = abs(len(lst_pre)-len(lst_type))
        for j in range(min(len(lst_pre),len(lst_type))):
            if lst_type[j] != lst_pre[j]:
                counter += 1
        #以上计算出到底相差多少位        
        if counter < pre_counter:#位数少，则替换
            pre_counter = counter
            pre_len = len(lst_pre)
            index = i 
        if pre_counter == counter :#刚好位数相等，要看pre的长度，越短越好，也体现为比例
           if len(lst_pre) < pre_len:
                index = i
        #以上确定 index的值
    lst_diff2 = []#构建所有差异值组成的数列
    for i in range(len(lst_diff)):
        lst_diff2.append(lst_diff[i]-limit)
        #以上构建所有差异值组成的数列 完成
    if counter ==0 :
        return word_list[lst_diff.index(min(lst_diff))]
    for j in range(len(lst_diff2)):
        if lst_diff2[j] < 0:#diff< limit
            for i in range(len(lst_diff)):#这个for是为了遍历替换
                if lst_diff[i] == lst_diff[index]:
                    index = i#如果相同差异，则第一个出现的
                    return word_list[index]
        #以上是按错误率算的，并且是如果相同差异，则第一个出现的
        elif all(lst_diff2) == False:#diff = limit
            # return(len_diff.index((min(len_diff))))
            return (word_list[(len_diff.index((min(len_diff))))])
        else:#就是diff > limit
            return typed_word
        #以上所有差异值>0，则输出typed_word；有一个<0，即满足其他可能   """    
    # END PROBLEM 5


def sphinx_swaps(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> sphinx_swaps("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> sphinx_swaps("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> sphinx_swaps("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> sphinx_swaps("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> sphinx_swaps("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """   
    #Important: You may not use while, for, or list comprehensions in your implementation. Use recursion.
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    """我的傻鸟代码，还做不出来
    if starct =='' and goal=='':
        return 0
    elif start =='' or goal == '':
        return 1 
    else:
        if start[0] == goal[0]:
            lst_l =list(start)
            lst_r =list(goal)
            lst_l.pop(0)
            lst_r.pop(0)
            start = ''.join(lst_l)
            goal = ''.join(lst_r)
            return 0 + sphinx_swaps(start, goal, limit)
        else:
            lst_l =list(start)
            lst_r =list(goal)
            lst_l.pop(0)
            lst_r.pop(0)
            start = ''.join(lst_l)
            goal = ''.join(lst_r)
            return 1 + sphinx_swaps(start, goal, limit)
    #     return
    # return sum(list(start)[i] != list(goal)[i] for i in range(min(len(start),len(goal))) ) + abs(len(start)-len(goal))
    """
    def helper(changed,typed,referenced,limit):
        if changed > limit:
            return changed
        elif len(typed) == 0:
            return changed + len(referenced)
        elif len(referenced) == 0:
            return changed + len(typed)
        elif referenced[0] == typed[0]:
            return helper(changed,typed[1:],referenced[1:],limit)
        else:
            return helper(changed+1,typed[1:],referenced[1:],limit)
    return helper(0,start,goal,limit)
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):#完全想不出来，我是傻逼
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    def myfunc(s, g, ans):#s-->select g-->given 
            if ans > limit:
                return ans + 1
            if s == '':
                return ans + len(g)
            if g == '':
                return ans + len(s)
            if s[0] == g[0]:
                return myfunc(s[1:], g[1:], ans)
            else:
                return min(myfunc(s[1:], g, ans + 1), myfunc(g[0] + s[0:], g, ans + 1), myfunc(s[1:], g[1:], ans + 1))
    return myfunc(start, goal, 0)


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'


FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(sofar, prompt, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        sofar: a list of the words input so far
        prompt: a list of the words in the typing prompt
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> sofar = ['how', 'are', 'you']
    >>> prompt = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(sofar, prompt, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], prompt, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # counter = sum(sofar[i] != prompt[i] for i in range(min(len(sofar),len(prompt)))) + abs(len(sofar)-len(prompt))
    # rate = round((1 - counter / len(prompt)),1)
    counter = 0 
    for i in range(min(len(sofar),len(prompt))):
        if sofar[i] == prompt[i]:
            counter += 1
        else:
            break
    rate = counter / len(prompt)
    upload ({'id':user_id,'progress':rate})
    return rate
    # END PROBLEM 8


def time_per_word(words, times_per_player):
    """Given timing data, return a match dictionary, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> match["words"]
    ['collar', 'plush', 'blush', 'repute']
    >>> match["times"]
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # times_diff constructor
    times_diff = []
    for i in range(len(times_per_player)):
        j = 0
        new =[]
        for j in range(0,(len(times_per_player[j]))-1):
            diff = times_per_player[i][j+1] - times_per_player[i][j]
            new.append(diff)
        times_diff.append(new)
    # times_diff constructor end
    match = {"words":words,"times":times_diff}
    return match
    # return dictionary
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.
    #calling fastest_words on [player_0, player_1] should not mutate player_0 or player_1.
    Arguments:
        match: a match dictionary as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """#match是一个dictionary，是上面部分函数写传递出来的
    player_indices = range(len(match["times"]))  # contains an *index* for each player
    word_indices = range(len(match["words"]))    # contains an *index* for each word
    #以上是在调用dict的关键字
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    r = []
    for p in player_indices:
        r.append([])#([[],[],[]]) 内有i个分组
    # print('玩家有',r,'个')     
    for w in word_indices:
        # print('词语第',w,'个是',match["words"][w])
        min = 10000000000       
        for p in player_indices:
            store = match["times"][p]
            # print(store)
            compare = store[w]
            # print(compare)             
            if min > compare:
                min = compare
                winplayerindex = p
        # print('index',winplayerindex)
        r[winplayerindex].insert(w,match["words"][w])
    return r
    # return r
    # a < b ,a 的 标签存入
    # END PROBLEM 10

def match(words, times):
    """A dictionary containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def word_at(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(match["words"]), "word_index out of range of words"
    return match["words"][word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(match["words"]), "word_index out of range of words"
    assert player_num < len(match["times"]), "player_num out of range of players"
    return match["times"][player_num][word_index]


def match_string(match):
    """A helper function that takes in a match dictionary and returns a string representation of it"""
    return f"match({match['words']}, {match['times']})"


enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
