import random
import argparse

# a list of common signals
sig_set = set([
    ',','.','!','#',':','\'','"','(',')','@','<','>','~','，','。','《','》','！','、','「','」','[',']','-','+','*','/','&','$','%',' ',
    '0','1','2','3','4','5','6','7','8','9','的',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
])

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
    if len(word_arr) == 2:
        return word_arr[1]+word_arr[0]
    
    random.shuffle(word_arr)
    # print(word_arr)
    return ''.join(word_arr)
        

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