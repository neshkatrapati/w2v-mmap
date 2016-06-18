# What ?
Gensim has a word2vec interface which can access and train word2vec models. But, this cannot work with rather huge models such as GoogleNewsVectors.
This is an interface to deal with such large models. This does not read the whole file into RAM but indexes the model file and does random access. It cannot train w2v models.

# How ? 
## Convert binary into txt
If you get pre-trained vectors in binary format or you have stored them into binary format, You must convert it into txt format.
convert.c does exactly this.


``` bash
 # Compile
 $ gcc convert.c  -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result -o convert -g3
```

``` bash
 # Convert
 $ ./convert {filename}.bin > {filename}.txt
```

PS : This might take a while

## Prerequisites
* Install indexer_python it from https://github.com/neshkatrapati/indexer_python
* Install marisa & marisa-trie
``` bash
    $ sudo apt-get install marisa
    $ sudo pip install marisa-trie
```

## Make Key-Index and Trie
``` bash
    $ python make_index.py {filename}
```

This creates {filename}.kidx (Key-Linenumber index) and {filename}.trie (Trie of the previous file)


