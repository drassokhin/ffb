#!/usr/bin/env python3
import sys
import random

SUBSTITUTION_PROBABILITY = 0.9  # the probability a character for which a homoglyph exists will be replaced
STEALTH_SPACE_CHAR = '\u200B'
STEALTH_SPACE_PROBABILITY = 0.3

# prepare character substitution table
homoglyphs = 'AАΑ,BВΒ,CСϹ,EЕΕ,FϜ,HНΗ,IΙ,KКΚ,MМΜϺ,NΝ,OОΟ,PРΡ,QԚ,TТΤ,WԜ,XХΧ,YΥ,ZΖ,ПΠ,ФΦ,ЛΛ,БƂ,ГΓ,ИͶ,' \
             'иͷ,aаα,cсς,eе,hһ,kкκҝ,oоο,pрρ,qԛ,vν,wԝ,xхχ,yу,вβ,нӊ,пπ,тτ,фφ,лλԯ,ёӗ,йӣ'

homoglyph_list = homoglyphs.split(',')

# create dictionary that looks like this: {'A': 'АΑ', ..., 'й': 'ӣ', ...}
# and contains all possible homoglyph character substitutions
substitution_table = {}
for h in homoglyph_list:
    for c in h:
        subst = h.replace(c, '')
        # each character should occur in the homoglyphs list exactly once
        assert c not in substitution_table
        substitution_table[c] = subst


def should_subst(probability: float) -> bool:
    assert 0.0 <= probability <= 1.0
    r = random.random()  # remember, this returns a pseudo-random float in the semi-open range [0.0, 1.0)
    return r < probability


def translate(ch: str) -> str:
    assert len(ch) == 1
    if ch not in substitution_table:
        return ch
    # randomly replace characters for which replacements exist
    if not should_subst(SUBSTITUTION_PROBABILITY):
        return ch
    subst_string = substitution_table[ch]
    # choose a random homoglyph substitution
    return random.choice(subst_string)


def ins_nb_space(ch: str) -> str:
    assert len(ch) == 1
    if ch.isspace():
        return ch
    if should_subst(STEALTH_SPACE_PROBABILITY):
        return f'{ch}{STEALTH_SPACE_CHAR}'
    return ch


def run():
    inp = sys.stdin.read()
    for ch in inp:
        sys.stdout.write(ins_nb_space(translate(ch)))
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
