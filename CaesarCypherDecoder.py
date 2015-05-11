# An encoder/decoder of ROT-13.
# Note that since English has 26 characters, this ROT-13 program will be
# able to both encode and decode texts written in English.
# Once you're done, you will be able to read the following secret message:

test_msg1 = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

test_msg2 = "Gur Mra bs Clguba, ol Gvz Crgref\n\nOrnhgvshy vf orggre guna htyl.\nRkcyvpvg vf orggre guna vzcyvpvg.\nFvzcyr vf orggre guna pbzcyrk.\nPbzcyrk vf orggre guna pbzcyvpngrq.\nSyng vf orggre guna arfgrq.\nFcnefr vf orggre guna qrafr.\nErnqnovyvgl pbhagf.\nFcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.\nNygubhtu cenpgvpnyvgl orngf chevgl.\nReebef fubhyq arire cnff fvyragyl.\nHayrff rkcyvpvgyl fvyraprq.\nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.\nGurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.\nNygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.\nAbj vf orggre guna arire.\nNygubhtu arire vf bsgra orggre guna *evtug* abj.\nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\nVs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.\nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"

# ROT-13 caesar cypher dictionary
rot13cypher_encoder = dict(a='n', b='o', c='p', d='q', e='r', f='s', g='t', h='u', i='v', j='w', k='x', l='y', m='z',
                           n='a', o='b', p='c', q='d', r='e', s='f', t='g', u='h', v='i', w='j', x='k', y='l', z='m',
                           A='N', B='O', C='P', D='Q', E='R', F='S', G='T', H='U', I='V', J='W', K='X', L='Y', M='Z',
                           N='A', O='B', P='C', Q='D', R='E', S='F', T='G', U='H', V='I', W='J', X='K', Y='L', Z='M')

rot13cypher_decoder = {}


def reverse_dict():
    for k, v in rot13cypher_encoder.items():
        rot13cypher_decoder[v] = k


def encode(s):
    new_str = ""
    for char in s:
        if char.isalpha():
            new_str += rot13cypher_encoder[char]
        else:
            new_str += char
    return new_str


def encode_message(s):
    encoded_msg = ""
    lines = s.splitlines()
    for line in lines:
        if line == "":
            encoded_msg += "\n"
        else:
            encoded_msg = encoded_msg + encode(line) + "\n"
    return encoded_msg


def decode(s):
    new_str = ""
    for char in s:
        if char.isalpha():
            new_str += rot13cypher_decoder[char]
        else:
            new_str += char
    return new_str


def decode_message(msg):
    decoded_msg = ""
    lines = msg.splitlines()
    for line in lines:
        if line == "":
            decoded_msg += "\n"
        else:
            decoded_msg = decoded_msg + decode(line) + "\n"
    return decoded_msg


def main():
    reverse_dict()
    print "First decoded message: ", decode_message(test_msg1)
    print "Second decoded message: ", decode_message(test_msg2)

    str_to_encode = raw_input("Input a string to encode:")
    print encode(str_to_encode)


main()
