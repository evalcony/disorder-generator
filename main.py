import random
import argparse

# a list of common signals
sig_set = set([
    ',','.','!','#',':','\'','"','(',')','@','<','>','~','[',']','-','+','*','/','&','$','%',' ','{','}','|','`',';',':',
    '，','。','？','《','》','！','、','「','」','：','……','；','“','”','【','】',
    '的','\n'
    '0','1','2','3','4','5','6','7','8','9',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
])

# 乱序长度
seg_len = 4


def work(args):
    if args.s != '':
        disorder(args.s)
    elif args.f != '':
        lines = read_file(args.f)
        for line in lines:
            disorder(line)

def disorder(sentence):
    res = ''
    ss = seperate(sentence)
    for w in ss:
        if w[0] not in sig_set:
            r = make_disorder(w)
            res += r
        else:
            res += w[0]
    print(res)

def seperate(sentence):
    res = []
    buf = []
    for i in range(len(sentence)):
        if (sentence[i] in sig_set):
            if len(buf) != 0:
                res.append(buf)
                buf = []
            res.append([sentence[i]])
        else:
            buf += sentence[i]
    if len(buf) != 0:
        res.append(buf)
    
    return res

def make_disorder(word_arr):
    if len(word_arr) == 1:
        return word_arr[0]
    if len(word_arr) == 2:
        return word_arr[1]+word_arr[0]
    pre = 0
    res = ''
    for i in range(len(word_arr)):
        if i != 0 and i % seg_len == 0:
            s = word_arr[pre:i+1]
            random.shuffle(s)
            res += ''.join(s)
            pre = i+1
    if pre != len(word_arr)+1:
        s = word_arr[pre:len(word_arr)]
        random.shuffle(s)
        res += ''.join(s)
    return res
        

def read_file(filename):
    lines = []
    # root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.replace("\n",""))
    return lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', type=str, default='', help='读入一个句子')
    parser.add_argument('-f', type=str, default='', help='读入一个文件')
    args = parser.parse_args()

    work(args)
