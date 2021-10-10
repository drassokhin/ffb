#!/usr/bin/env python3
import sys
import random

# prepare character substitution table
homoglyphs = 'AАΑ,BВΒ,CС,EЕΕ,HНΗ,IΙ,KКΚ,MМΜ,NΝ,OОΟ,PРΡ,TТΤ,XХΧ,YΥ,ZΖ,ПΠ,ФΦ,ЛΛ,ГΓ,' \
             'aаα,cсς,eе,kкκҝ,oоο,pрρ,vν,xхχ,yу,вβ,пπ,тτ,фφ,лλ,ёӗ,йӣ'

homoglyph_list = homoglyphs.split(',')

# create dictionary that looks like this: {'A': 'АΑ', ..., 'й': 'ӣ', ...}
# and contains all possible homoglyph character substitutions
substitution_table = {}
for h in homoglyph_list:
    for c in h:
        subst = h.replace(c, '')
        substitution_table[c] = subst


def should_subst(probability: float) -> bool:
    assert 0.0 <= probability <= 1.0
    r = random.random()  # remember, this returns a pseudo-random float in the semi-open range [0.0, 1.0)
    return r < probability


def translate(ch: str) -> str:
    assert len(ch) == 1
    if ch not in substitution_table:
        return ch
    # replace 3 out of 4 characters for which replacements exist
    if not should_subst(0.75):
        return ch
    subst_string = substitution_table[ch]
    # choose a random homoglyph substitution
    return random.choice(subst_string)


def run():
    inp = sys.stdin.read()
    for ch in inp:
        sys.stdout.write(translate(ch))
    sys.stdout.flush()


if __name__ == '__main__':
    run()

# Example:
# Input
"""
Однажды, в студеную зимнюю пору
Я из лесу вышел; был сильный мороз.
Гляжу, поднимается медленно в гору
Лошадка, везущая хворосту воз.
И шествуя важно, в спокойствии чинном,
Лошадку ведет под уздцы мужичок
В больших сапогах, в полушубке овчинном,
В больших рукавицах… а сам с ноготок!

Should you ask me, whence these stories? 
Whence these legends and traditions, 
With the odors of the forest 
With the dew and damp of meadows,
With the curling smoke of wigwams,
With the rushing of great rivers,
With their frequent repetitions,
And their wild reverberations
As of thunder in the mountains?
"""

# Output
"""
Oднαжды, β cтyдeнyю зимнюю ποру
Я из λecy βышел; быλ сиλьныӣ мoрοз.
Γλяжy, пοднимαeтςя мeдлeннο в гoρy
Λoшадкa, βeзyщaя χвoрοcτy βοз.
И шeстβуя βажнo, в ςπoҝоӣςтβии чиннοм,
Λошaдкy βeдeτ πод yздцы мyжичоҝ
Β боλьшиχ caπoгαx, β πoλyшубҝе οвчинном,
B бoλьшиχ ρуҝаβицαχ… α cαм с нoгoτоҝ!

Shοuld yοu аsк me, whеncе these storiеs? 
Whеnςе thesе lеgends αnd trаditiοns, 
With thе οdors оf thе fоrеst 
With thе dеw and dаmp οf mеаdоws,
With thе сurling smοκe οf wigwams,
With thе rushing of grеαt rivеrs,
With thеir frеquеnt rереtitiοns,
Αnd thеir wild rеνerbеrαtiоns
Аs оf thunder in thе mоuntains?
"""