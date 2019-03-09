import pandas as pd
import tensorflow as tf
tf.enable_eager_execution()

import numpy as np
import os
import sys
import time
from os.path import basename

EPOCHS=10

filename = sys.argv[1]
if (len(sys.argv) >= 3):
  EPOCHS = int(sys.argv[2])

input = pd.read_csv(filename)
text = input.sum()['name'].lower()
vocab = sorted(set(text + " "))
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

def text_to_array(text):
    return np.array([char2idx[c] for c in text.lower() + " "]) 

input_data = input.applymap(text_to_array)['name'].values

dataset = tf.data.Dataset.from_generator(lambda: input_data, 
                                         tf.int64)

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

train_set = dataset.map(split_input_target)

BATCH_SIZE = 1
examples_per_epoch = input_data.size
steps_per_epoch = examples_per_epoch//BATCH_SIZE
BUFFER_SIZE = 10000

batched_trainset = train_set.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# Length of the vocabulary in chars
vocab_size = len(vocab)

# The embedding dimension 
embedding_dim = 64

# Number of RNN units
rnn_units = 256

import functools
rnn = functools.partial(tf.keras.layers.GRU, recurrent_activation='sigmoid')

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, 
                              batch_input_shape=[batch_size, None]),
    rnn(rnn_units,
        return_sequences=True, 
        recurrent_initializer='glorot_uniform',
        stateful=True),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model

model = build_model(
  vocab_size = len(vocab), 
  embedding_dim=embedding_dim, 
  rnn_units=rnn_units, 
  batch_size=BATCH_SIZE)

def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

model.compile(
    optimizer = tf.train.AdamOptimizer(),
    loss = loss)

# Directory where the checkpoints will be saved
checkpoint_dir = './models/' + basename(filename) + "_model"
# Name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

history = model.fit(batched_trainset.repeat(), epochs=EPOCHS, steps_per_epoch=steps_per_epoch, callbacks=[checkpoint_callback])

model.summary()
