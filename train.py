from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
tf.enable_eager_execution()

import io
import os

TRAIN_FILE = "sample_train_input.txt"
VOCABULARY = "out/vocabulary"


def train():
    vocab = save_or_load_vocabulary()
    data_as_ints = get_data_as_ints(read_train()) # TODO proper code. type list[ndarray]
    dateset = create_tf_dataset(data_as_ints)
    # TODO instead of batch just use samples as in the training data
    sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

    dataset = sequences.map(split_input_target)
    # Batch size
    BATCH_SIZE = 64
    examples_per_epoch = len(text)
    steps_per_epoch = examples_per_epoch//BATCH_SIZE
    BUFFER_SIZE = 10000
    dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

    # Length of the vocabulary in chars
    vocab_size = len(vocab)

    # The embedding dimension
    embedding_dim = 256

    # Number of RNN units
    rnn_units = 1024



def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text



def save_or_load_vocabulary():
    if os.exists(VOCABULARY): # right method? TODO
        vocab = load() # need proper method. TODO not on this computer
    else:
        lines = read_train()
        vocab = vocabulary(lines)
        save_vocabulary(vocab)
    return vocab


def save_vocabulary(vocab):
    with io.open(VOCABULARY, encoding="UTF-8", mode="w") as f:
        f.write("\n".join(sorted(list(vocab))))
        f.write("\n")


def vocabulary(lines):
    return set(sum([list(set(l)) for l in lines], []))


def read_train():
    with io.open(TRAIN_FILE, encoding="UTF-8") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    train()
