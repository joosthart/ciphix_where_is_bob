import random
import string

fn_in  = 'secret.txt'
fn_out = 'secret.txt'
seed = 
max_n_random = int(1e6)

random.seed(seed)

if __name__ == '__main__':
    chars = string.punctuation + string.ascii_letters +'\n'
    
    random_n    = [random.randint(1, 1e2) for x in range(max_n_random)]
    random_char = [random.randint(1, 1e5) for x in range(max_n_random)]

    with open(fn_in, 'r') as f:
        file = f.read()

    encoded_file = ''
    i = 0
    for idx, c in enumerate(file):
        for n in range(random_n[idx]):
            encoded_file += chars[random_char[i]%len(chars)]
            i+=1
        encoded_file +=  c
            
            
    
    with open(fn_out, 'w') as f:
        f.write(encoded_file)

        

