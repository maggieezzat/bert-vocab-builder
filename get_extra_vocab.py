# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import codecs
import fnmatch
import os
from os import listdir, remove
from os.path import isfile, join
import sys
import unicodedata
from absl import app as absl_app
import tensorflow as tf

import string
import collections

import spacy
import csv


#vocab = "/home/maggie/twitter-data/twitter_vocab_1.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_20.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_30.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_40.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_50.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_100.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_150.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_200.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_250.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_300.txt"
#vocab = "/home/maggie/twitter-data/twitter_vocab_500.txt"

#vocab = "/home/maggie/german-articles-data/articles_vocab_1.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_50.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_100.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_150.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_200.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_250.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_300.txt"
#vocab = "/home/maggie/german-articles-data/articles_vocab_500.txt"

bert_vocab = "/home/maggie/bert-vocab-builder/vocab/vocab_uncased_1000.txt"

#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_1.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_50.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_100.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_150.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_200.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_250.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_300.txt"
#out_file = "/home/maggie/german-articles-data/articles_extra_vocab_500.txt"

#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_1.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_20.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_30.txt"
out_file = "/home/maggie/twitter-data/tweets_extra_vocab_40.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_50.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_100.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_150.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_200.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_250.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_300.txt"
#out_file = "/home/maggie/twitter-data/tweets_extra_vocab_500.txt"

def extra_vocab(bert_vocab_file=bert_vocab, app_vocab_file=vocab, out_file=out_file):


    with tf.gfile.Open(bert_vocab_file, "r") as bert_vocab:
        with tf.gfile.Open(app_vocab_file, "r") as app_vocab:
            with open(out_file, 'w', encoding='utf-8') as new_file:
                bert = bert_vocab.readlines()
                app = app_vocab.readlines()

                bert_set = set(bert)
                app_set = set(app)

                extra_set = set(app)
                for item in app_set:
                    if item in bert_set:
                        extra_set.remove(item)

                extra = list(extra_set)

                for line in extra:
                    new_file.write(line)
                
                            

def main(_):
    extra_vocab()


if __name__ == "__main__":
    absl_app.run(main)