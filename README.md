# name-generator
Generate random plausible names

There are trained models for Russian first and last names as
well as for English, German and Hindi first names

Example usage:
`cat example_input.txt | python predict.py russian_first_names > out_file`

other models:
russian_first_names
russian_last_names
russian_english_names
russian_indian_names
russian_german_names

Disclaimer: code is bad, hard to customize without ugly hacking. It is a project for fun in the end, right?

To train one can currently use something like this:
`python train.py data/russian_first_names.csv 10`
where 10 is the number of epochs (default 10)
