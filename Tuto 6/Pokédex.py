# Data for the in-game "Pokedex" of NPC quotes.
# You can add more quotes here.
#
# Key format:
#   world_id (0..4) -> list of entries
# Entry format:
#   {
#       "id": "unique_string",
#       "source": "PNJ3",      # optional label
#       "text": "quote to show when unlocked"
#   }

POKEDEX_QUOTES = {
    0: [
        {
            "id": "Essai",
            "source": "Impression du jour :",
            "text": "Beau temps aujourd'hui. Rien à signaler. J'ai faim."
        },
    ],
    1: [
        {
            "id": "Panneau2",
            "source": "",
            "text": "Si on est 'perduis', on peut aller voir Gandalf au Nord de la ville. Allons-y... "
        },
        {
            "id": "PNJ6",
            "source": "",
            "text": "Une personne m'a dit : 'Passez le bonjour à vi niecis.' Trop bizarre..."
        },
        {
            "id": "Panneau1",
            "source": "",
            "text": "Lu sur un panneau : un 'cheffi' qui recrute 'uni coiffeusi'"
        },
        {
            "id": "PNJ5.1",
            "source": "",
            "text": "Une personne m'a dit : 'Quelqu'uni a vu quelque chose'"
        },
        {
            "id": "PNJ5.2",
            "source": "",
            "text": "J'ai aussi entendu 'li humani peut m'aider'..."
        },
        {
            "id": "PNJ4",
            "source": "",
            "text": "D'autres mots bizarres : On m'a parlé de mes 'niècis', et que ça fait longtemps qu'on les a pas 'vuis'. Et est-ce que je suis 'suri de ne pas être tombéi sur la tête'"
        },
        {
            "id": "Panneau3",
            "source": "",
            "text": "Les toilettes sont 'pour touttis'"
        },
    ],
    2: [
        {
            "id": "Gandalf1",
            "source": "",
            "text": "Comme il y a beaucoup de mots étranges, je vais noter les bizareries à chaque fois dans ce carnet."
        },
        {
            "id": "PNJ10.0",
            "source": "",
            "text": "'An nouval' = un nouveau ou une nouvelle"
        },
        {
            "id": "PNJ9.0",
            "source": "",
            "text": "'Perdux' = perdu ou perdue"
        },
        {
            "id": "Panneau5",
            "source": "",
            "text": "'Perdux' = perdu ou perdue ; 'retrouvæ' = retrouvé ou retrouvée ; 'al' = il ou elle"
        },
        {
            "id": "PNJ10.1",
            "source": "",
            "text": "'Lu' = le ou la"
        },
        {
            "id": "PNJ10.2",
            "source": "",
            "text": "'Mu tancle' = mon oncle ou ma tante"
        },
        {
            "id": "PNJ9.1",
            "source": "",
            "text": "'biauz froeur' = beau-frère ou belle-soeur ; 'mu' = mon ou ma ; 'al' = il ou elle ; partix = parti ou partie ; 'an granx comédian' = un grand comédien ou une grande comédienne"
        },
        {
            "id": "PNJ8.0",
            "source": "",
            "text": "'Desolæ' = désolé ou désolée"
        },
        {
            "id": "PNJ8.1",
            "source": "",
            "text": "'Mu cousaine' = mon cousain ou ma cousine ; 'su filx' = son fils ou sa fille"
        },
        {
            "id": "PNJ8.2",
            "source": "",
            "text": "'Al est passæ' = il est passé ou elle est passée ; 'Al m'a harcelæ' = Il m'a harcelé ou elle m'a harcelée"
        },
        {
            "id": "PNJ8.3",
            "source": "",
            "text": "'Partix' = parti ou partie ; 'actaire' = Acteur ou actrice ; 'Héroæs Grecx' = héros grecs ou heroines grecques"
        },
        {
            "id": "PNJ8.4",
            "source": "",
            "text": "'Lu bourgeoix human distinguæ' = le bourgeois gentillhomme"
        },
        {
            "id": "PNJ7.0",
            "source": "",
            "text": "'Lu portiær' = le portier ou la portière ; 'je suis certan' = je suis certain ou je suis certaine"
        },
        {
            "id": "cinq",
            "source": "",
            "text": "'Merlin l'enchantaire' = Merlin l'enchanteur"
        },
        {
            "id": "huit",
            "source": "",
            "text": "Des titres de film : '12 human en colère', le conte de lu humæn Kaguya', 'Humæn mononoké', 'lu géanx de fer'"
        },
        {
            "id": "Maison_papier",
            "source": "",
            "text": "'Voisan' = voisin ou voisine ; 'venux' = venu ou venue"
        },
        {
            "id": "neuf",
            "source": "",
            "text": "Titres de livres : 'le cercle des poètes disparux', Lu seigneurx des anneaux', 'Lu dernær elfe'"
        },
        {
            "id": "sept",
            "source": "",
            "text": "Quelques oeuvres : 'l'étrangær', 'le diner de conx', 'gladiateurx','zora lea rouxe'"
        },
        {
            "id": "Panneau6_2_toilettes",
            "source": "",
            "text": "Sur un panneau : 'toilettes pour toutx'"
        },
    ],
    3: [
        {
            "id": "portier3.exemple1",
            "source": "",
            "text": "La fusion, exemple avec 'Actif/Active' : Je garde ce qui ne bouge pas ('act') et je fusionne ce qui change ('if' et 'ive') : actIF + actIVE = Actifive"
        },
        {
            "id": "Panneau10",
            "source": "",
            "text": "Sur un panneau : 'Toilettes pour toustes'"
        },
        {
            "id": "PNJ11",
            "source": "",
            "text": "'Comprisse' = compris ou comprise , 'acteurice' = acteur ou actrice , 'agriculteurice' = agriculteur ou agricultrice"
        },
        {
            "id": "PNJ12.0",
            "source": "",
            "text": "'Ellui' = elle ou lui , 'iels' = ils ou elles"
        },
        {
            "id": "portier3.exemple2",
            "source": "________________________________________________",
            "text": "Le changement de voyelle, exemple avec 'Gamin/Gamine' : J'ajoute une voyelle pour créer un nouveau mot. Gamin + GaminE + A = Gamaine."
        },
        {
            "id": "portier3.1",
            "source": "",
            "text": "'tan pote' = ton pote ou ta pote"
        }, 
        {
            "id": "PNJ12.2",
            "source": "",
            "text": "'lea sorcièle' = le sorcier ou la sorcière , 'copaines' = copains ou copines , 'toude seulë' = tout seul ou toute seule , 'eune fantassaine' = un fantassin ou une fantassine"
        },
        {
            "id": "Panneau7.1",
            "source": "",
            "text": "Sur un panneau : 'al vous ramènera'"
        },
        {
            "id": "portier3.exemple3",
            "source": "________________________________________________",
            "text": "Le glissement de consonne, exemple avec 'Cadet/Cadette' : Je remplace la consonne par une autre. Ici je replace les T par des D. cadeT + cadeTTe - T = CadèDe"
        },
        {
            "id": "PNJ13.2",
            "source": "",
            "text": "'toudes les habitandes' = tous les habitants ou toutes les habitantes"
        },
        {
            "id": "portier3.0",
            "source": "",
            "text": "'étrangèle' = étranger ou étrangère , 'habitandes' = habitants ou habitantes, 'lea prof remplacande' = le prof remplacant ou la prof remplacante'"
        },
        {
            "id": "PNJ11.2",
            "source": "",
            "text": "'contende' = content ou contente"
        },
        {
            "id": "PNJ13.1",
            "source": "",
            "text": "'nouveaulle' = nouvelle ou nouveau , 'jardinièle' = jardinier ou jardinière , 'patiende' = patient ou patiente , 'prêde' = prêt ou prête"
        },
        {
            "id": "portier3.exemple4",
            "source": "________________________________________________",
            "text": "Mettre un 'ë' à la fin des mots qui ne se différencient qu'à l'écrit : exploitéë, ravië, intellectuellë "
        },
        {
            "id": "portier3.2",
            "source": "",
            "text": "'rapportéë' = rapporté ou rapportée"
        },
        {
            "id": "Panneau7",
            "source": "",
            "text": "Sur un panneau : 'Vous êtes perduë' , 'vous vous êtes retrouvéë'"
        },
        {
            "id": "PNJ11.1",
            "source": "",
            "text": "'lea seigneurë des anneaux' = le seigneur des anneaux, 'échapéë' = échapé ou échapée"
        },
        {
            "id": "PNJ12.1",
            "source": "",
            "text": "'amiës' = amis ou amies"
        },
        {
            "id": "PNJ12.1",
            "source": "",
            "text": "'enfant' = fils ou fille , 'adelphe' = frères ou soeurs"
        },
        {
            "id": "PNJ13.0",
            "source": "",
            "text": "'eune inconnuë' = un inconnu ou une inconnue"
        },
    ],
    4: [
        {
            "id": "bibliothèque.1",
            "source": "",
            "text": "'Pour savoir quels sont les classificateurs à utiliser, il suffit de comprendre la forme de l’objet.'"
        },


        
        {
            "id": "bibliothèque.0",
            "source": "________________________________________________",
            "text": "'iawa' = objets en forme de barque : cuiller iawa, pelure de fruits iawa, barque iawa"
        },
        {
            "id": "bibliothèque.0",
            "source": "________________________________________________",
            "text": "'isi' = objets ronds : grenouille isi, araignée isi, graine d'avocat isi"
        },
        {
            "id": "bibliothèque.3",
            "source": "________________________________________________",
            "text": "'serpents amoka', 'lézards amoka', mille-pattes amoka'. 'Ces animaux sont long et flexibles.'"
        },
        {
            "id": "PNJ19",
            "source": "",
            "text": "mille-pattes amoka'"
        },
        {
            "id": "panneau16",
            "source": "",
            "text": "larves amoka'"
        },
        {
            "id": "panneau16.1",
            "source": "________________________________________________",
            "text": "'mousse inun'"
        },
        {
            "id": "PNJ18",
            "source": "",
            "text": "'poussière inun'"
        },
        {
            "id": "PNJ17",
            "source": "",
            "text": "'poudre inun'"
        },
        {
            "id": "PNJ19",
            "source": "________________________________________________",
            "text": "'sceau anon'"
        },
        {
            "id": "panneau14",
            "source": "",
            "text": "'voiture anon'"
        },
        {
            "id": "panneau13",
            "source": "",
            "text": "'maison anon'"
        },
        {
            "id": "panneau11",
            "source": "",
            "text": "'bibliothèque anon'"
        },
    ],
    5 : [
        {
            "id": "Gandalf4",
            "source": "",
            "text": "J'ai plus trop d'encre dans mon stylo. Je vais essayer de l'économiser pour les fois suivantes. Je vais peut-être trouver quelque chose pour remplacer mon carnet..."
        },
    ],
    6 : [
        {
            "id": "TV6",
            "source": "",
            "text": "gabidoum = tempête ou ouragan"
        },
        {
            "id": "PNJ27",
            "source": "",
            "text": "pim ouragan"
        },
        {
            "id": "TV6.1",
            "source": "_________",
            "text": "choubidou-wa = voiture"
        },
        {
            "id": "panneau19",
            "source": "",
            "text": "pim voiture"
        },
        {
            "id": "PNJ26",
            "source": "_________",
            "text": "waaaaaaaa = lune"
        },
        {
            "id": "PNJ26.1",
            "source": "",
            "text": "pim lune"
        },
        {
            "id": "PNJ25.1",
            "source": "___________________________",
            "text": "wazabibou = arbre"
        },
        {
            "id": "PNJ27.1",
            "source": "",
            "text": "poum arbre"
        },
        {
            "id": "panneau20",
            "source": "_________",
            "text": "papouille = orange"
        },
        {
            "id": "panneau20.1",
            "source": "",
            "text": "poum orange"
        },
        {
            "id": "PNJ25",
            "source": "___________________________",
            "text": "bibbou = enfant"
        },
        {
            "id": "PNJ24",
            "source": "",
            "text": "pam enfant"
        },
        
    ]
}
