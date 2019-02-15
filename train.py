from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
tf.enable_eager_execution()

import io

TRAIN_FILE = "sample_train_input.txt"
VOCABULARY = "out/vocabulary"


def train():
    lines = read_train()
    vocab = vocabulary(lines)
    save_vocabulary(vocab)


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
