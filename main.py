import random

def ich():
    ver_ich = ["haue", "ficke", "vögele", "lecke", "blase", "küsse", "knete", "packe an", "stöhne", "fingere", "beiße",
               "lecke", "drücke",  "nehme", "spreche", "umarme", "bin", "habe", "gehe", "komme", "spreche", "treffe",
               "liebe", "tue", "schlafe", "esse", "lache", "schreie", "seufze", "setze", "rieche", "fasse an", "höre",
               "öffne", "streichele", "kratze", "bumse", "verwöhne", "trinke", "schließe", "zittere"]
    verb_ich = random.choice(ver_ich)
    A = (f"ich {verb_ich}")
    return A

def du():
    ver_du = ["haust", "fickst", "vögelst", "leckst", "bläst", "Küsst", "knetest", "packst an","stöhnst", "fingerst",
               "beißt", "leckst", "drückst", "nimmst", "sprichst", "umarmst", "bist", "hast", "gehst", "kommst",
               "spricht", "triffst", "liebst","tust", "schläfst", "isst", "lachst","schreist", "seufzt", "setzt",
              "riechst",  "fasst an", "hörst", "öffnest", "streichelst", "kratzt", "bumst", "verwöhnst","trinkst",
               "schließt", "zitterst"]
    ver_du = random.choice(ver_du)
    B = (f"du {ver_du}")
    return B

def sie():
    sub = ["sie", "er", "es"]
    sub = random.choice(sub)
    ver_sie = ["haut", "fickt", "vögelt", "leckt", "bläst", "küsst", "knetet","packt an", "stöhnt", "fingert", "beißt",
               "leckt", "drückt", "nimmt", "spricht", "umarmt", "ist", "hat", "geht", "kommt", "spricht", "triffst",
               "liebt", "tut", "schläft", "isst", "lacht", "schreit", "seufzt", "setzt", "riecht", "fasst an",
               "hört", "öffnet", "streichelt", "kratzt", "bumst", "verwöhnt", "trink", "schließt", "zittert"]
    ver_sie = random.choice(ver_sie)
    C = (f"{sub} {ver_sie}")
    return C

def ihr():
    ver_ihr = ["haut", "fickt", "vögelt", "leckt", "blast", "küsst", "knetet", "packt an", "stöhnt", "fingert", "beißt",
               "leckt", "drückt", "nehmt", "sprecht", "umarmt", "seid", "habt", "geht", "kommt", "sprecht", "trefft",
               "liebt", "tut", "schlaft", "esst","lacht", "schreit", "seufzt", "setzt", "riecht", "fasst an", "hört",
               "öffnet", "streichelt", "kratzt", "bumst", "verwöhnt", "trinkt", "schließt", "zittert"]
    ver_ihr = random.choice(ver_ihr)
    D = (f"ihr {ver_ihr}")
    return D

def wir ():
    ver_wir =["hauen", "ficken", "vögeln", "lecken", "blasen", "küssen", "kneten", "anpacken", "stöhnen", "fingern",
              "beißen", "lecken", "drücken", "nehmen", "sprechen", "umarmen", "sein", "haben", "gehen", "kommen",
              "sprechen", "treffen", "lieben", "tun", "schlafen", "essen", "lachen", "schreien", "seufzen", "setzen",
              "riechen", "anfassen", "hören", "offen", "streicheln", "kratzen", "bumsen", "verwöhnen", "trinken",
              "schließen", "zittern"]
    ver_wir = random.choice(ver_wir)
    E = (f"wir {ver_wir}")
    return E

def Sie():
    ver_Sie = ["hauen", "ficken", "vögeln", "lecken", "blasen", "küssen", "kneten", "anpacken", "stöhnen", "fingern",
              "beißen", "lecken", "drücken", "nehmen", "sprechen", "umarmen", "sein", "haben", "gehen", "kommen",
              "sprechen", "treffen", "lieben", "tun", "schlafen", "essen", "lachen", "schreien", "seufzen", "setzen",
              "riechen", "anfassen", "hören", "offen", "streicheln", "kratzen", "bumsen", "verwöhnen", "trinken",
              "schließen", "zittern"]
    ver_Sie = random.choice(ver_Sie)
    F = (f"Sie {ver_Sie}")
    return F

def mix1():
    A = ich()
    B = du()
    C = sie()
    D = ihr()
    E = wir()
    F = Sie()
    frases = [A, B, C, D, E, F]
    frases = random.choice(frases)
    return frases

def mix2():
    H = mix1()
    adjektiv = ["achtsam", "alkoholisch", "fest", "knackig", "lockig", "poetisch", "scharf", "beharrlich", "bunt",
                "frei", "künstlich", "lieb", "oral", "sicher", "charmant", "fantastisch", "gefährlich", "laut",
                "musikalisch", "provokant", "soft", "dumm", "elektrisch", "imaginär", "luxuriös", "öffnen",
                "rhythmisch", "temperamentvoll", "typisch", "utopisch", "nass", "trockem", "sanft", "intensiv", "schön"]
    adjektiv = random.choice(adjektiv)
    frase_plus = (f"{H} {adjektiv}")
    return frase_plus

def mix3 ():
    I = mix1()
    J = mix2()
    resultado = [I, J]
    resultado = random.choice(resultado)
    return resultado



def name():
    name_list = ["das Bett", "die Liebe", "der Mut"," die Macht", "die Bewegung", "der Wein" , "die Sonne", "der Mund",
                 "die Vulva", "der Schwanz", "der rücken", "der Po", "die Brüste", "die Decke", "der Tisch", "das Nest",
                 "der Samen", "der Schleim"]
    name_list = random.choice(name_list)
    ver_name = ["haut", "fickt", "vögelt", "leckt", "bläst", "küsst", "knetet","packt an", "stöhnt", "fingert", "beißt",
               "leckt", "drückt", "nimmt", "spricht", "umarmt", "ist", "hat", "geht", "kommt", "spricht", "triffst",
               "liebt", "tut", "schläft", "isst", "lacht", "schreit", "seufzt", "setzt", "riecht", "fasst an",
               "hört", "öffnet", "streichelt", "kratzt", "bumst", "verwöhnt", "trink", "schließt", "zittert"]
    ver_name = random.choice(ver_name)

    name_lis_plu = ["die Armen", "die Brüste", "die Haare"]
    name_lis_plu = random.choice(name_lis_plu)
    ver_name_plu = ["hauen", "ficken", "vögeln", "lecken", "blasen", "küssen", "kneten", "anpacken", "stöhnen", "fingern",
                    "beißen", "lecken", "drücken", "nehmen", "sprechen", "umarmen", "sein", "haben", "gehen", "kommen",
                    "sprechen", "treffen", "lieben", "tun", "schlafen", "essen", "lachen", "schreien", "seufzen", "setzen",
                    "riechen", "anfassen", "hören", "offen", "streicheln", "kratzen", "bumsen", "verwöhnen", "trinken",
                     "schließen", "zittern"]
    ver_name_plu = random.choice(ver_name_plu)
    adjektiv = ["achtsam", "alkoholisch", "fest", "knackig", "lockig", "poetisch", "scharf", "beharrlich", "bunt",
                "frei", "künstlich", "lieb", "oral", "sicher", "charmant", "fantastisch", "gefährlich", "laut",
                "musikalisch", "provokant", "soft", "dumm", "elektrisch", "imaginär", "luxuriös", "öffnen",
                "rhythmisch", "temperamentvoll", "typisch", "utopisch", "nass", "trockem", "sanft", "intensiv", "schön"]
    adjektiv = random.choice(adjektiv)

    NL = (f"{name_list} {ver_name} {adjektiv} ")
    NLP = (f"{name_lis_plu} {ver_name_plu} {adjektiv}")
    name_print = [NL, NLP]
    name_print = random.choice(name_print)
    return name_print

def tag():
    tag_list = ["Heute", "gestern", "morgen", "in 5 Minuten", "immer", "manchmal", "sofort", "selten", "endlich",
                 "jetzt", "nun", "gleichzeitig"]
    tag_list = random.choice(tag_list)
    verb_tag = ["haut", "fickt", "vögelt", "leckt", "bläst", "küsst", "knetet","packt an", "stöhnt", "fingert", "beißt",
               "leckt", "drückt", "nimmt", "spricht", "umarmt", "ist", "hat", "geht", "kommt", "spricht", "triffst",
               "liebt", "tut", "schläft", "isst", "lacht", "schreit", "seufzt", "setzt", "riecht", "fasst an",
               "hört", "öffnet", "streichelt", "kratzt", "bumst", "verwöhnt", "trink", "schließt", "zittert"]
    verb_tag = random.choice(verb_tag)
    obj_dir_tag = ["mich", "dich", "sie", "ihn", "es", "ihr", "uns", "sie"]
    obj_dir_tag = random.choice(obj_dir_tag)
    tag_print = (f"{tag_list} {verb_tag} {obj_dir_tag}")
    return tag_print

def ort ():
    Z = mix1().split(" ")
    Z = ' '.join(reversed(Z))
    ort_list = ["das Bett", "die Liebe", "der Mut"," die Macht", "die Bewegung", "der Wein" , "die Sonne", "der Mund",
                "die Vulva", "der Schwanz", "der rücken", "der Po", "die Brüste", "die Decke", "der Tisch", "das Nest",
                "der Samen", "der Schleim"]
    ort_list = random.choice (ort_list)
    ort_print = (f"{ort_list} {Z} ")
    return ort_print

def satz1():
    mix1()
    frase1 = mix1()
    obj_ind = ["mir", "dir", "ihr", "ihm", "ihm", "euch", "uns", "ihren"]
    obj_ind = random.choice(obj_ind)
    G = (f"{frase1} {obj_ind}")
    return G

def satz2():
    satz1()
    ver_sie = ["haut", "fickt", "vögelt", "leckt", "bläst", "küsst", "knetet", "packt an", "stöhnt", "fingert", "beißt"]
    ver_sie = random.choice(ver_sie)
    verb = ver_sie
    zeit = ["Heute", "gestern", "morgen", "in x Minuten", "immer", "manchmal", "sofort", "selten", "endlich", "jetzt", "nun", "gleichzeitig"]
    zeit = random.choice(zeit)
    obj_dir =["mich", "dich", "sie", "ihn", "es", "ihr", "uns", "sie"]
    obj_dir = random.choice(obj_dir)
    H = (f"{zeit} {verb} {obj_dir}")
    return H


print(mix3())
print(name())
print(tag())
print(satz2())
print(ort())
