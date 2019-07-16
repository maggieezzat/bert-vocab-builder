#!/bin/bash

python subword_builder.py \
--corpus_filepattern "/lm_corpus/dewiki_nltk_segmented/*/*.txt" \
--output_filename "/bert/bert-vocab-builder/vocab/dewiki_limited_chars_500_30it_no_extra_chars.txt" \
--min_count 500 \
--corpus_max_lines 1000000000 \
--num_iterations 30 \
--split_on_newlines True \
--do_lower True
