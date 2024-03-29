function xe { \echo '  % '$*; echo -n '       > '; eval "$*"; } # "execute with echo"

echo pronounceable
xe ./interjackalize.py {pronounceable}

echo char: c upper lower vowel consonant
xe ./interjackalize.py {c}

echo punctuation:
xe ./interjackalize.py {punctuation}

echo punctuationIOSfirstpage:
xe ./interjackalize.py {punctuationIOSfirstpage}

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

echo a room for an RPG
xe ./interjackalize.py '{rm}'

echo multiple with spaces:
echo "  % ./interjackalize.py '{2 animal}'"
echo "      > $(./interjackalize.py '{2 animal}')"

echo multiple without spaces:
xe ./interjackalize.py '{2animal}'

echo combination:
echo "  % ./interjackalize.py '{2 adv} {adj} {animal}'"
echo "      > $(./interjackalize.py '{2 adv} {adj} {animal}')"

echo password suitable for iphone entry:
xe ./interjackalize.py '{pronounceable}{2d}{punctuationIOSfirstpage}{pronounceable}'
