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


vocab = "/home/maggie/twitter-data/twitter_vocab_1.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_50.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_100.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_150.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_200.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_250.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_300.txt"
vocab = "/home/maggie/twitter-data/twitter_vocab_500.txt"
bert_vocab = "/home/maggie/twitter-data/pretraining_tweets.txt"
#out_file = 

def extra_vocab(bert_vocab_file, app_vocab_file):

    #nlp = spacy.load('de_core_news_sm')

    with tf.gfile.Open(rootdir, "r") as f:
        with open(output_root, 'w', encoding='utf-8') as new_file:
            reader = csv.reader(f, delimiter="\t", quotechar=None)
            for line in reader:
                doc = line[1]
                #doc = nlp(doc)
                #sentences = list(doc.sents)
                #for i in range(len(sentences)):
                #    new_file.write(sentences[i].string.strip() + '\n')
                new_file.write(doc + '\n')
                new_file.write('\n')
                doc = ""
                
                            

def main(_):
    text_cleaning()


if __name__ == "__main__":
    absl_app.run(main)