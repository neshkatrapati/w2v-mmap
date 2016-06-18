# What ?
Gensim has a word2vec interface which can access and train word2vec models. But, this cannot work with rather huge models such as GoogleNewsVectors.
This is an interface to deal with such large models. This does not read the whole file into RAM but indexes the model file and does random access. It cannot train w2v models.

# How ? 
## Convert binary into txt
If you get pre-trained vectors in binary format or you have stored them into binary format, You must convert it into txt format.
convert.c does exactly this.


```bash
 gcc convert.c  -lm -pthread -O3 -march=native -Wall -funroll-loops -Wno-unused-result -o convert -g3
```