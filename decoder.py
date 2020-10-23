import random
import string
import sys
from itertools import accumulate

if len(sys.argv) < 3:
    raise ValueError(
        'Please provide filename and random seed as system argument;' \
        + ' python decoder.py [filename] [random_seed]'
    )

fn_in  = sys.argv[1]
fn_out = fn_in[:fn_in.find('.')]+'_decrypted.txt'
seed = int(sys.argv[2])
max_n_random = int(1e6)

random.seed(seed)

if __name__ =='__main__':
    chars = string.punctuation + string.ascii_letters +'\n'
    
    random_n = [random.randint(1, 1e2) for x in range(max_n_random)]

    with open(fn_in, 'r') as f:
        file = f.read()
        
    decoded_file = ''
    i = 0
    for n in random_n:
        i += n
        if i > len(file):
            break
        decoded_file += file[i]
        i+=1

    with open(fn_out, 'w') as f:
        f.write(decoded_file)
