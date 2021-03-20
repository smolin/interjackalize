function xe { \echo '    '$*; echo -n '    '; $*; } # "execute with echo"

echo pronounceable
xe ./interjackalize.py {pronounceable}

echo char: c upper lower vowel consonant
xe ./interjackalize.py {c}

echo digit 0-9:
xe ./interjackalize.py {d}

echo float:
xe ./interjackalize.py {f}

echo dice: d4, d6, d8, d10, d12, d20, d100:
xe ./interjackalize.py {d6}

echo day:
xe ./interjackalize.py {day}

echo jabberwock:
xe ./interjackalize.py {jabberwock}

echo latlong:
xe ./interjackalize.py {latlong}

echo parts of speech: adj adv noun prep verb pref suf root
xe ./interjackalize.py {noun}

echo types: animal sport color material moods occupations role
xe ./interjackalize.py {animal}

echo 'multiple (opt leave out space):'
xe ./interjackalize.py {5 animal}

echo a room for an RPG
xe ./interjackalize.py {rm}}

echo multiple with spaces:
echo '    ./interjackalize.py {2 animal}'
echo -n '    '
./interjackalize.py '{2 animal}'
