import sys
import os

file_name = sys.argv[1]

def token_line_mapping(file_name):
    key_file = file_name + '.kidx'
    trie_file = file_name + '.trie'
    
    if os.path.exists(trie_file):
        os.remove(trie_file)
    #with open(file_name) as f ,open(key_file,'a') as t:
    #    for index, line in enumerate(f):
    #        token = line.split('\t')
    #        t.write(token[0] + ';' + str(index) + "\n")
    print "Done Writing to a File"
    os.system('marisa-build {key_file} > {trie_file}'.format(**locals()))
    print "Done Writing to Trie"
    
token_line_mapping(file_name)            
            
