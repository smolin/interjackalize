#!/usr/bin/env python3
"""
Module Docstring

started with https://www.python-boilerplate.com/py3+executable+argparse

Thanks to https://github.com/dariusk/corpora/raw/master/data/
And https://stackoverflow.com/a/5502875
And https://sourceforge.net/projects/wordlist/
And https://organicdonut.com/2015/12/dictionaries-and-word-lists-for-programmers/

Examples

$ t-g.py '{sports} {animals}'
Composite rules shinty-hurling crocodile

$ ./t-g.py '{mood} {color} {animal}-headed {pref}{animal}'
hesitant MediumVioletRed jackal-headed eco-sloth

"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse
import random
import re
import requests
import requests_cache
import string


vowels = 'a e i o u aa ae ai ao au ea ee ei eo eu oa oe oi oo ou ua ue ui uo uu'.split(' ')

# cat /usr/share/dict/words | tr A-Z a-z | cut -c 1,2 | sort -u | grep -v '[aeiou]$' | fmt -9999
# initials='ab ac ad af ag ah aj ak al am an ap aq ar as at av aw ax ay az b bd bh bj bl br by c cc ch cl cn cr cs ct cw cy cz d dh dj dr ds dv dw dy dz eb ec ed ef eg eh ej ek el em en ep eq er es et ev ew ex ey ez f fj fl fr fy g gh gl gm gn gr gw gy h hl hr hs hw hy ib ic id if ig ih ij ik il im in ip ir is it iv iw ix iy iz j jh jw jy k kh kj kl km kn kp kr ks kv kw ky l lh ll lw ly m mb mc md mh ml mn mp mr mw my n ng nh nj nt ny ob oc od of og oh oj ok ol om on op oq or os ot ov ow ox oy oz p pf ph pl pn pr ps pt py q r rh rv ry s sb sc sd sf sg sh sj sk sl sm sn sp sq sr ss st sv sw sy sz t tc td th tj tl tm tr ts tw ty tz ub uc ud ug uh uj uk ul um un up ur us ut uv ux uz v vl vr vy w wh wl wr wy x xm xy y yc yd yg ym yn yp yq yr yt yv z zh zl zm zw zy'.split(' ')

# ? cat American/2of12.txt | while read -r in; do echo "${in: -3}"; done | head
initials='a ab ac ad af ag ah aj ak al am an ap aq ar as at av aw ax ay az b bl br by c ch cl cn cr cy cz d dh dj dr dw dy e eb ec ed ef eg eh ej ek el em en ep eq er es et ev ew ex ey f fj fl fr g gh gl gn gr gy h hy i ib ic id if ig ik il im in ip ir is it iv j k kh kl kn kr kv l ll ly m mn my n nt ny o ob oc od of og oh ok ol om on op or os ot ov ow ox oy oz p ph pj pl pn pr ps pt py q qw r rh ry s sc sh sk sl sm sn sp sq ss st sv sw sy t th tr ts tw ty tz u ub ud uf ug uh uk ul um un up ur us ut uv ux v vy w wh wr x xy y yt z zw zy'.split(' ')

# $ cat /usr/share/dict/words | while read -r in; do echo "${in: -2}"; done | tr A-Z a-z | sort -u | grep -v '^[aeiou]' | fmt -9999
finals = 'ba bb be bi bk bl bo bs bt bu by ca ce ch ci ck co cq cs ct cu cy da dd de dh di dj dl do dr ds dt du dv dy dz fa fd fe ff fh fi fo fs ft fu fy ga gd ge gg gh gi gm gn go gr gs gt gu gy ha hd he hh hi hl hm hn ho hr hs ht hu hy ja jd je ji jk jl jo ju jy ka ke kf kh ki kk ko kr ks kt ku ky la lb lc ld le lf lg lh li lk ll lm ln lo lp lr ls lt lu lx ly lz ma mb md me mh mi mk ml mm mn mo mp mr ms mt mu my na nc nd ne ng nh ni nj nk nl nn no ns nt nu nx ny nz pa pe pf ph pi pl po pp pr ps pt pu py qa qi ra rb rc rd re rf rg rh ri rk rl rm rn ro rp rr rs rt ru rv rx ry rz sa sc se sg sh si sk sl sm sn so sp ss st su sy sz ta td te th ti tl tn to tr ts tt tu ty tz va ve vi vn vo vu vy wa wd we wf wi wk wl wm wn wo wp ws wt wu wy xa xe xi xl xo xt xy ya yc yd ye yf yg yi yk yl ym yn yo yp yr ys yt yu yx yz za zd ze zi zn zo zu zy zz'.split(' ')



# https://realpython.com/caching-external-api-requests/ requests_cache.install_cache('corpora', backend='sqlite', expire_after=3600)

class corporaClass:
    #base =          'https://github.com/dariusk/corpora/raw/master/data/'
    base =          'http://corpora-api.glitch.me/'
    ext = {
            'sports':  'sports/sports',
            'animals': 'animals/common',
            'colors': 'colors/wikipedia',
        }
    def switch(self, key):
        default = f'no such key {key} in class corporaClass'
        result = getattr(self, 'case_' + str(key))()
        return result

    def case_adjs(self):
        return requests.get(self.base+'words/adjs').json()['data']['adjs']

    def case_advs(self):
        return requests.get(self.base+'words/adverbs').json()['data']['adverbs']

    def case_animals(self):
        return requests.get(self.base+'animals/common').json()['data']['animals']

    def case_colors(self):
        result = requests.get(self.base+'colors/web_colors').json()['data']['colors']
        result = [entry['color'] for entry in result]
        return result

    def case_materials(self):
        result = requests.get(self.base+'materials/layperson-metals').json()['data']['layperson metals'] \
               + requests.get(self.base+'materials/gemstones').json()['data']['gemstones'] \
               + requests.get(self.base+'materials/fabrics').json()['data']['fabrics'] \
               + requests.get(self.base+'materials/building-materials').json()['data']['building materials'] \
               + requests.get(self.base+'materials/natural-materials').json()['data']['natural materials']
        return result

    def case_moods(self):
        return requests.get(self.base+'humans/moods').json()['data']['moods']

    def case_nouns(self):
        return requests.get(self.base+'words/nouns').json()['data']['nouns']

    def case_occupations(self):
        return requests.get(self.base+'humans/occupations').json()['data']['occupations']

    def case_preps(self):
        return requests.get(self.base+'words/prepositions').json()['data']['prepositions']

    def case_prefs(self):
        result = requests.get(self.base+'words/prefix_root_suffix').json()['data']['prefixes']
        result = [entry['part'] for entry in result]
        return result

    def case_preps(self):
        return requests.get(self.base+'words/prepositions').json()['data']['prepositions']

    def case_roots(self):
        result = requests.get(self.base+'words/prefix_root_suffix').json()['data']['roots']
        result = [entry['part'] for entry in result]
        return result

    def case_roles(self):
        result = requests.get(self.base+'archetypes/character').json()['data']['characters']
        result = [[entry['name']]+entry['synonyms'] for entry in result]
        result = sum(result, []) # flatten
        return result

    def case_sports(self):
        return requests.get(self.base+'sports/sports').json()['data']['sports']

    def case_sufs(self):
        result = requests.get(self.base+'words/prefix_root_suffix').json()['data']['suffixes']
        result = [entry['part'] for entry in result]
        return result

    def case_verbs(self):
        return requests.get(self.base+'words/infinitive_verbs').json()['data']

    #def json(self, what):
    #    return random.choice(requests.get(self.base+self.ext[what]).json()['data'][what])

corpora = corporaClass()

class replaceMapClass:

    def switch(self, key):
        default = f'no such key {key} in class replaceMapClass'
        #result = getattr(self, 'case_' + str(key), lambda: default)()
        result = getattr(self, 'case_' + str(key))()
        return result

    def case_pronounceable(self):
        return random.choice(initials)+random.choice(vowels)+random.choice(finals)
        #result = random.choice(initials)+random.choice(vowels)+random.choice(finals) \
        #       + random.choice(initials)+random.choice(vowels)+random.choice(finals) \
        #       + random.choice(initials)+random.choice(vowels)+random.choice(finals) \
        #       + random.choice(initials)+random.choice(vowels)+random.choice(finals)
        #start = random.randrange(0,len(result)-8)
        #end = start + random.randrange(3,7)
        #print (start,end)
        #return result[start:end]

    def case_c(self):
        result = random.randrange(33,126)
        return chr(result)
    def case_upper(self):
        return random.choice(list(string.ascii_uppercase))
    def case_lower(self):
        return random.choice(list(string.ascii_lowercase))
    def case_vowel(self):
        return random.choice(['a','e','i','o','u','y'])
    def case_consonant(self):
        return random.choice(list(set(string.ascii_lowercase) - set('aeiou')))
    def case_punctuation(self):
        return random.choice(list(set(string.punctuation)))
    def case_punctuationIOSfirstpage(self):
        return random.choice(['-','/',':',';','(',')','$','&','@','"','.',',','?','!',"'"])

    def case_d(self):
        result = random.randrange(10)
        return str(result)
    def case_f(self):
        result = random.random()
        return str(result)
    def case_d4(self):
        result = random.randrange(4)
        return str(result)
    def case_d6(self):
        result = random.randrange(6)
        return str(result)
    def case_d8(self):
        result = random.randrange(8)
        return str(result)
    def case_d10(self):
        result = random.randrange(10)
        return str(result)
    def case_d12(self):
        result = random.randrange(12)
        return str(result)
    def case_d20(self):
        result = random.randrange(20)
        return str(result)
    def case_d100(self):
        result = random.randrange(100)
        return str(result)
    def case_d1000(self):
        result = random.randrange(1000)
        return str(result)

    def case_day(self):
        result = random.choice(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
        return result
    def case_jabberwock(self):
        return random.choice('bandersnatch beamish borogoves brillig callay callooh frabjous frumious galumphing gimble gyre jabberwock jubjub manxome mimsy mome outgrabe raths slithy snicker-snack toves tulgey tumtum uffish vorpal whiffling'.split(' '))
    def case_latlong(self):
        return str(round(random.random()*180,7))+random.choice(['W','E'])+','+str(round(random.random()*90,7))+random.choice(['N','S'])

    def case_adj(self):
        return str(random.choice(corpora.switch('adjs')))
    def case_adv(self):
        return str(random.choice(corpora.switch('advs')))
    def case_noun(self):
        return str(random.choice(corpora.switch('nouns')))
    def case_pref(self):
        return str(random.choice(corpora.switch('prefs')))
    def case_prep(self):
        return str(random.choice(corpora.switch('preps')))
    def case_root(self):
        return str(random.choice(corpora.switch('roots')))
    def case_suf(self):
        return str(random.choice(corpora.switch('sufs')))
    def case_verb(self):
        return str(random.choice(corpora.switch('verbs')))

    def case_animal(self):
        return str(random.choice(corpora.switch('animals')))
    def case_sport(self):
        return str(random.choice(corpora.switch('sports')))
    def case_color(self):
        return str(random.choice(corpora.switch('colors')))
    def case_material(self):
        return str(random.choice(corpora.switch('materials')))
    def case_mood(self):
        return str(random.choice(corpora.switch('moods')))
    def case_occupation(self):
        return str(random.choice(corpora.switch('occupations')))
    def case_role(self):
        return str(random.choice(corpora.switch('roles')))

    def case_rm_size(self):
        return random.choice(['tiny','small','medium','large','huge'])
    def case_rm_finish(self):
        return random.choice(['rock','stone','brick','wood','tile','plaster'])
    def case_rm_water(self):
        return random.choice(['parched','bone-dry','dusty','damp','wet','dripping'])
    def case_rm_temp(self):
        return random.choice(['freezing','cold','warm','hot'])
    def case_rm_use(self):
        return random.choice(['storeroom','kitchen','library','armory','closet','throneroom',\
                'bunkroom','lavatory','antechamber','shrine'])
    def case_rm(self):
        result = []
        if random.randrange(100) > 50:
            result.append(self.switch('rm_size'))
        if random.randrange(100) > 50:
            result.append(self.switch('rm_temp'))
        if random.randrange(100) > 50:
            result.append(self.switch('rm_finish'))
        if random.randrange(100) > 50:
            result.append(self.switch('rm_water'))
        result.append(self.switch('rm_use'))
        return ' '.join(result)

replaceMap = replaceMapClass()


pat = re.compile('([{]([0-9 ]*)([^{}]+)[}])') # eg "have a {2 adj} {noun} today": mg0 is "{2 adj}", mg1 is "2 " mg2 is "adj"
def main(args):
    """ Main entry point of the app """
    result = args.pattern
    match = re.search(pat, result)
    while match:
        span = match.groups()[0]
        try:
            count = int(match.groups()[1])
        except:
            count = 1
        if match.groups()[1].endswith(' '):
            sep = ' '
        else:
            sep = ''
        token = match.groups()[2]
        replacement = sep.join([replaceMap.switch(token) for i in range(count)])
        result = result.replace(span,replacement,1)
        match = re.search(pat, result)
    print(result)



if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("pattern", help="Required generator pattern")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)

