import random
import string
from itertools import accumulate

fn_in  = 'secret.txt'
fn_out = 'revelation.txt'
seed = 
max_n_random = int(1e6)

random.seed(seed)

if __name__ =='__main__':
    chars = string.punctuation + string.ascii_letters +'\n'
    
    random_n = [random.randint(1, 1e2) for x in range(max_n_random)]

    with open(fn_in, 'r') as f:
        file = f.read()


    decoded_file = ''
    i = 0
    idxs = list(accumulate(random_n))
    for n in random_n:
        i += n
        if i > len(file):
            break
        decoded_file += file[i]
        i+=1

    with open(fn_out, 'w') as f:
        f.write(decoded_file)
