# name-generator
Generate random plausible names. The names generated are not present in the training data

Tested with python 3.7
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

Some example outputs:

Russian last names:

гзин
дабутов
ежсёнов
ётов
ванзомионов
жпов
имин
коробов
луиниконов
минирюдов
нипонов
пархомин
ремьёв
стров
тобонов
завромков
улёбин
хагин
улывинов
семсипов
ивазапов
кузков

German first names:

inge
mars
ludo
heramd
polvin
ard
bermias
cölvemin
exim
halpo
jonall
phillars
terick
vonher
bert
dvilcaster
elbeld
frald
guodo
hjolanis
icheige
jaunliacer
kurrich
lyus
ngüswil
osvin
swonian
utrich
valvin
wogergaur

English first names:

louenie
miltbi
mielle
smarke
sting
bronkema
powerdnette
lauriane
lizetause
cheont
maryessrick
cyndylyn
thilpaldinza
tieson
frewinetta

Russian first names:

матиан
валав
рофор
додлав
семёсей
гадофий
олий
алевегграт
кокаланазий
микар
летифо

