#PNJ INTRO 
from events.PNJ1 import PNJ1
from events.PNJ2 import PNJ2                                        #importe tes events sinon ça sert à rien
from events.PNJ3 import PNJ3                                        #PENSE A IMPORTER TES SCHNAPS DE FICHIERS !!!  ET A CHANGER LES NOMS QUAND TU COPIE BETEMENT
from events.TV import TV
from events.Panneau0 import Panneau0
from events.Save import Save

#PNJ MONDE1
from events.monde1.PNJ4 import PNJ4
from events.monde1.PNJ5 import PNJ5
from events.monde1.PNJ6 import PNJ6
from events.monde1.portier import portier
from events.monde1.Gandalf1 import Gandalf1
from events.monde1.Panneau1_OffreEmploi import Panneau1_OffreEmploi
from events.monde1.Panneau2_Indice import Panneau2_Indice
from events.monde1.Panneau3_Toilettes import Panneau3_Toilettes
from events.monde1.Panneau4_Scène_Errès import Panneau4_Scène_Errès
from events.monde1.Screen1 import Screen1

#PNJ MONDE 2
from events.monde2.PNJ7 import PNJ7
from events.monde2.PNJ8 import PNJ8
from events.monde2.PNJ9 import PNJ9
from events.monde2.PNJ10 import PNJ10
from events.monde2.Panneau5_Indice import Panneau5_Indice
from events.monde2.Panneau6_Scene_Erres import Panneau6_Scene_Erres
from events.monde2.Gandalf2 import Gandalf2
from events.monde2.Maison_papier import Maison_papier
from events.monde2.Fantome_du_lac import Fantome_du_lac
from events.monde2.Clef import Clef
from events.monde2.un import un 
from events.monde2.deux import deux
from events.monde2.trois import trois
from events.monde2.quatre import quatre
from events.monde2.cinq import cinq
from events.monde2.six import six
from events.monde2.sept import sept
from events.monde2.huit import huit
from events.monde2.neuf import neuf
from events.monde2.dix import dix
from events.monde2.onze import onze
from events.monde2.douze import douze
from events.monde2.treize import treize
from events.monde2.quatorze import quatorze
from events.monde2.quinze import quinze
from events.monde2.Panneau6_2_toilettes import Panneau6_2_toilettes

#PNJ MONDE 3
from events.monde3.PNJ11 import PNJ11
from events.monde3.PNJ12 import PNJ12
from events.monde3.PNJ13 import PNJ13
from events.monde3.PNJ14 import PNJ14
from events.monde3.Panneau7 import Panneau7
from events.monde3.Panneau9 import Panneau9
from events.monde3.Panneau10 import Panneau10
from events.monde3.portier3 import portier3
from events.monde3.Gandalf3 import Gandalf3

#PNJ MONDE 4
from events.monde4.PNJ15 import PNJ15
from events.monde4.PNJ16 import PNJ16
from events.monde4.PNJ17 import PNJ17
from events.monde4.PNJ18 import PNJ18
from events.monde4.PNJ19 import PNJ19
from events.monde4.panneau11 import panneau11
from events.monde4.panneau12 import panneau12
from events.monde4.panneau13 import panneau13
from events.monde4.panneau14 import panneau14
from events.monde4.panneau15 import panneau15
from events.monde4.panneau16 import panneau16
from events.monde4.fish import fish
from events.monde4.portier4 import portier4
from events.monde4.bibliothèque import bibliothèque
from events.monde4.grenouille import grenouille
from events.monde4.serpent import serpent
from events.monde4.lezard import lezard
from events.monde4.bocal import bocal
from events.monde4.baton import baton
from events.monde4.herbe import herbe
from events.monde4.portier4_2 import portier4_2
from events.monde4.fish2 import fish2
from events.monde4.portier4_2_cache import portier4_2_cache
from events.monde4.farine import farine
from events.monde4.Gandalf4 import Gandalf4

# PNJ MONDE5
from events.monde5.portier5 import portier5
from events.monde5.porte_close import porte_close
from events.monde5.Event_Invisible import Event_Invisible
from events.monde5.Gandalf5 import Gandalf5
from events.monde5.Gandalf5_1 import Gandalf5_1
from events.monde5.Panneau_Place import Panneau_Place
from events.monde5.PNJ20 import PNJ20
from events.monde5.PNJ21 import PNJ21
from events.monde5.PNJ22 import PNJ22
from events.monde5.PNJ23 import PNJ23
from events.monde5.panneau17 import panneau17
from events.monde5.panneau18 import panneau18
from events.monde5.tag_maison import tag_maison
from events.monde5.PNJ24_1 import PNJ24_1
from events.monde5.Event_Invisible2 import Event_Invisible2
from events.monde5.enfant5 import enfant5

#PNJ MONDE 6
from events.monde6.Fig_Enfant import Fig_Enfant
from events.monde6.Fig_Arbre import Fig_Arbre
from events.monde6.Fig_Voiture import Fig_Voiture
from events.monde6.Fig_Ouragan import Fig_Ouragan
from events.monde6.Fig_Orange import Fig_Orange
from events.monde6.Fig_Lune import Fig_Lune
from events.monde6.PNJ24 import PNJ24
from events.monde6.PNJ25 import PNJ25
from events.monde6.PNJ26 import PNJ26
from events.monde6.PNJ27 import PNJ27
from events.monde6.panneau19 import panneau19
from events.monde6.panneau20 import panneau20
from events.monde6.TV6 import TV6
from events.monde6.portier6 import portier6
from events.monde6.Gandalf6 import Gandalf6

#PNJ INTRO-------------------------------------
def handle_PNJ1_event(game, player, npc):                           #l'événement prof_event se déclenche
    event = PNJ1(game.screen, game, player)
    game.event = event

def handle_PNJ2_event(game, player, npc):                          #l'événement prof_event2 se déclenche
    event = PNJ2(game.screen, game, player)
    game.event = event

def handle_PNJ3_event(game, player, npc):                          #l'événement prof_event3 se déclenche
    event = PNJ3(game.screen, game, player)
    game.event = event

def handle_TV_event(game, player, npc):                          #l'événement TV se déclenche
    event = TV(game.screen, game, player)
    game.event = event

def handle_Panneau0_event(game, player, npc):                          #l'événement Panneau0 se déclenche
    event = Panneau0(game.screen, game, player)
    game.event = event

def handle_Save_event(game, player, npc):                          #l'événement Panneau0 se déclenche
    event = Save(game.screen, game, player)
    game.event = event


#-----------------------------------------------------

#PNJ MONDE 1--------------------------------------------
def handle_Panneau1_OffreEmploi_event(game,player,npc):
    event = Panneau1_OffreEmploi(game.screen,game,player)
    game.event = event

def handle_Panneau2_Indice_event(game,player,npc):
    event = Panneau2_Indice(game.screen,game,player)
    game.event = event

def handle_Panneau3_Toilettes_event(game,player,npc):
    event = Panneau3_Toilettes(game.screen,game,player)
    game.event = event

def handle_Panneau4_Scène_Errès_event(game,player,npc):
    event = Panneau4_Scène_Errès(game.screen,game,player)
    game.event = event

def handle_PNJ4_event(game,player,npc):
    event = PNJ4(game.screen,game,player)
    game.event = event

def handle_PNJ5_event(game,player,npc):
    event = PNJ5(game.screen,game,player)
    game.event = event

def handle_PNJ6_event(game,player,npc):
    event = PNJ6(game.screen,game,player)
    game.event = event

def handle_portier_event(game,player,npc):
    event = portier(game.screen,game,player)
    game.event = event

def handle_Gandalf1_event(game,player,npc):
    event = Gandalf1(game.screen,game,player)
    game.event = event

def handle_Screen1_event(game,player,npc):
    event = Screen1(game.screen,game,player)
    game.event = event
#--------------------------------------------------------------------

#PNJ MONDE 2 ------------------------------------------------------------
def handle_Panneau5_Indice_event(game,player,npc):
    event = Panneau5_Indice(game.screen,game,player)
    game.event = event

def handle_Panneau6_Scene_Erres_event(game, player, npc):
    event = Panneau6_Scene_Erres(game.screen,game,player)
    game.event = event

def handle_Gandalf2_event(game,player,npc):
    event = Gandalf2(game.screen,game,player)
    game.event = event

def handle_PNJ7_event(game,player,npc):
    event = PNJ7(game.screen,game,player)
    game.event = event

def handle_PNJ8_event(game,player,npc):
    event = PNJ8(game.screen,game,player)
    game.event = event

def handle_PNJ9_event(game,player,npc):
    event = PNJ9(game.screen,game,player)
    game.event = event

def handle_PNJ10_event(game,player,npc):
    event = PNJ10(game.screen,game,player)
    game.event = event

def handle_Maison_papier_event(game,player,npc):
    event = Maison_papier(game.screen,game,player)
    game.event = event

def handle_Fantome_du_lac_event(game,player,npc):
    event = Fantome_du_lac(game.screen,game,player)
    game.event = event

def handle_Clef_event(game,player,npc):
    event = Clef(game.screen,game,player)
    game.event = event

def handle_un_event(game,player,npc):
    event = un(game.screen,game,player)
    game.event = event

def handle_deux_event(game,player,npc):
    event = deux(game.screen,game,player)
    game.event = event

def handle_trois_event(game,player,npc):
    event = trois(game.screen,game,player)
    game.event = event

def handle_quatre_event(game,player,npc):
    event = quatre(game.screen,game,player)
    game.event = event

def handle_cinq_event(game,player,npc):
    event = cinq(game.screen,game,player)
    game.event = event

def handle_six_event(game,player,npc):
    event = six(game.screen,game,player)
    game.event = event

def handle_sept_event(game,player,npc):
    event = sept(game.screen,game,player)
    game.event = event

def handle_huit_event(game,player,npc):
    event = huit(game.screen,game,player)
    game.event = event

def handle_neuf_event(game,player,npc):
    event = neuf(game.screen,game,player)
    game.event = event

def handle_dix_event(game,player,npc):
    event = dix(game.screen,game,player)
    game.event = event

def handle_onze_event(game,player,npc):
    event = onze(game.screen,game,player)
    game.event = event

def handle_douze_event(game,player,npc):
    event = douze(game.screen,game,player)
    game.event = event

def handle_treize_event(game,player,npc):
    event = treize(game.screen,game,player)
    game.event = event

def handle_quatorze_event(game,player,npc):
    event = quatorze(game.screen,game,player)
    game.event = event

def handle_quinze_event(game,player,npc):
    event = quinze(game.screen,game,player)
    game.event = event

def handle_Panneau6_2_toilettes_event(game,player,npc):
    event = Panneau6_2_toilettes(game.screen,game,player)
    game.event = event
#----------------------------------------------------------------------

#PNJ MONDE 3 -------------------------------------------------------------
def handle_PNJ11_event(game,player,npc):
    event = PNJ11(game.screen,game,player)
    game.event = event

def handle_PNJ12_event(game,player,npc):
    event = PNJ12(game.screen,game,player)
    game.event = event

def handle_PNJ13_event(game,player,npc):
    event = PNJ13(game.screen,game,player)
    game.event = event

def handle_PNJ14_event(game,player,npc):
    event = PNJ14(game.screen,game,player)
    game.event = event

def handle_Panneau7_event(game,player,npc):
    event = Panneau7(game.screen,game,player)
    game.event = event

def handle_Panneau9_event(game,player,npc):
    event = Panneau9(game.screen,game,player)
    game.event = event

def handle_Panneau10_event(game,player,npc):
    event = Panneau10(game.screen,game,player)
    game.event = event

def handle_portier3_event(game,player,npc):
    event = portier3(game.screen,game,player)
    game.event = event

def handle_Gandalf3_event(game,player,npc):
    event = Gandalf3(game.screen,game,player)
    game.event = event

#---------------------------------------------------------------------

#PNJ MONDE 4
def handle_bibliothèque_event(game,player,npc):
    event = bibliothèque(game.screen,game,player)
    game.event = event

def handle_fish_event(game,player,npc):
    event = fish(game.screen,game,player)
    game.event = event

def handle_panneau11_event(game,player,npc):
    event = panneau11(game.screen,game,player)
    game.event = event

def handle_panneau12_event(game,player,npc):
    event = panneau12(game.screen,game,player)
    game.event = event

def handle_panneau13_event(game,player,npc):
    event = panneau13(game.screen,game,player)
    game.event = event

def handle_panneau14_event(game,player,npc):
    event = panneau14(game.screen,game,player)
    game.event = event

def handle_panneau15_event(game,player,npc):
    event = panneau15(game.screen,game,player)
    game.event = event

def handle_panneau16_event(game,player,npc):
    event = panneau16(game.screen,game,player)
    game.event = event

def handle_PNJ15_event(game,player,npc):
    event = PNJ15(game.screen,game,player)
    game.event = event

def handle_PNJ16_event(game,player,npc):
    event = PNJ16(game.screen,game,player)
    game.event = event

def handle_PNJ17_event(game,player,npc):
    event = PNJ17(game.screen,game,player)
    game.event = event

def handle_PNJ18_event(game,player,npc):
    event = PNJ18(game.screen,game,player)
    game.event = event

def handle_PNJ19_event(game,player,npc):
    event = PNJ19(game.screen,game,player)
    game.event = event

def handle_portier4_event(game,player,npc):
    event = portier4(game.screen,game,player)
    game.event = event
    
def handle_grenouille_event(game,player,npc):
    event = grenouille(game.screen,game,player)
    game.event = event

def handle_serpent_event(game,player,npc):
    event = serpent(game.screen,game,player)
    game.event = event

def handle_lezard_event(game,player,npc):
    event = lezard(game.screen,game,player)
    game.event = event

def handle_bocal_event(game,player,npc):
    event = bocal(game.screen,game,player)
    game.event = event

def handle_baton_event(game,player,npc):
    event = baton(game.screen,game,player)
    game.event = event

def handle_herbe_event(game,player,npc):
    event = herbe(game.screen,game,player)
    game.event = event

def handle_portier4_2_event(game,player,npc):
    event = portier4_2(game.screen,game,player)
    game.event = event
    
def handle_portier4_2_cache_event(game,player,npc):
    event = portier4_2_cache(game.screen,game,player)
    game.event = event

def handle_fish2_event(game,player,npc):
    event = fish2(game.screen,game,player)
    game.event = event

def handle_farine_event(game,player,npc):
    event = farine(game.screen,game,player)
    game.event = event

def handle_Gandalf4_event(game,player,npc):
    event = Gandalf4(game.screen,game,player)
    game.event = event

#---------------------------------------------------------------------------------------------------------------

#PNJ MONDE 5
def handle_portier5_event(game,player,npc):
    event = portier5(game.screen,game,player)
    game.event = event
    
def handle_porte_close_event(game,player,npc):
    event = porte_close(game.screen,game,player)
    game.event = event

def handle_Event_Invisible_event(game,player,npc):
    event = Event_Invisible(game.screen,game,player)
    game.event = event

def handle_Event_Invisible2_event(game,player,npc):
    event = Event_Invisible2(game.screen,game,player)
    game.event = event

def handle_Gandalf5_event(game,player,npc):
    event = Gandalf5(game.screen, game, player,npc)
    game.event = event

def handle_Gandalf5_1_event(game,player,npc):
    event = Gandalf5_1(game.screen, game, player)
    game.event = event

def handle_Panneau_Place_event(game,player,npc):
    event = Panneau_Place(game.screen,game,player)
    game.event = event

def handle_PNJ20_event(game,player,npc):
    event = PNJ20(game.screen,game,player)
    game.event = event

def handle_PNJ21_event(game,player,npc):
    event = PNJ21(game.screen,game,player)
    game.event = event

def handle_PNJ22_event(game,player,npc):
    event = PNJ22(game.screen,game,player)
    game.event = event
    
def handle_PNJ23_event(game,player,npc):
    event = PNJ23(game.screen,game,player)
    game.event = event

def handle_PNJ24_1_event(game,player,npc):
    event = PNJ24_1(game.screen,game,player)
    game.event = event

def handle_panneau17_event(game,player,npc):
    event = panneau17(game.screen,game,player)
    game.event = event

def handle_panneau18_event(game,player,npc):
    event = panneau18(game.screen,game,player)
    game.event = event

def handle_tag_maison_event(game,player,npc):
    event = tag_maison(game.screen,game,player)
    game.event = event

def handle_enfant5_event(game,player,npc):
    event = enfant5(game.screen,game,player)
    game.event = event

#---------------------------------------------------------------------------------------------------------------

# PNJ MONDE 6
def handle_Fig_Arbre_event(game,player,npc):
    event = Fig_Arbre(game.screen,game,player)
    game.event = event

def handle_Fig_Voiture_event(game,player,npc):
    event = Fig_Voiture(game.screen,game,player)
    game.event = event

def handle_Fig_Ouragan_event(game,player,npc):
    event = Fig_Ouragan(game.screen,game,player)
    game.event = event

def handle_Fig_Orange_event(game,player,npc):
    event = Fig_Orange(game.screen,game,player)
    game.event = event

def handle_Fig_Lune_event(game,player,npc):
    event = Fig_Lune(game.screen,game,player)
    game.event = event

def handle_Fig_Enfant_event(game,player,npc):
    event = Fig_Enfant(game.screen,game,player)
    game.event = event

def handle_PNJ24_event(game,player,npc):
    event = PNJ24(game.screen,game,player)
    game.event = event

def handle_PNJ25_event(game,player,npc):
    event = PNJ25(game.screen,game,player)
    game.event = event

def handle_PNJ26_event(game,player,npc):
    event = PNJ26(game.screen,game,player)
    game.event = event

def handle_PNJ27_event(game,player,npc):
    event = PNJ27(game.screen,game,player)
    game.event = event

def handle_panneau19_event(game,player,npc):
    event = panneau19(game.screen,game,player)
    game.event = event

def handle_panneau20_event(game,player,npc):
    event = panneau20(game.screen,game,player)
    game.event = event

def handle_TV6_event(game,player,npc):
    event = TV6(game.screen,game,player)
    game.event = event

def handle_portier6_event(game,player,npc):
    event = portier6(game.screen,game,player)
    game.event = event

def handle_Gandalf6_event(game,player,npc):
    event = Gandalf6(game.screen,game,player)
    game.event = event
    
#---------------------------------------------------------------------------------------------------------------

def handle(game, player, npc, keep_player_position=False):
    if not keep_player_position:
        player.position = player.last_position


#PNJ INTRO --------------------------------------
    if npc.name == 'PNJ1':                                        #le nom permet de déclencher les bons dialogues SSI TU CHANGE LE NOM DANS CONFIG !!!!! (ici prof)
        handle_PNJ1_event(game, player, npc)

    if npc.name == 'PNJ2':
        handle_PNJ2_event(game, player, npc)

    if npc.name == 'PNJ3':
        handle_PNJ3_event(game, player, npc)

    if npc.name == 'TV':
        handle_TV_event(game, player, npc)

    if npc.name == 'Panneau0':
        handle_Panneau0_event(game, player, npc)

    if npc.name == 'Save':
        handle_Save_event(game, player, npc)

#---------------------------------------------------

#PNJ MONDE1-----------------------------------------
    if npc.name == 'Panneau1_OffreEmploi':                                       
        handle_Panneau1_OffreEmploi_event(game, player, npc)

    if npc.name == 'Panneau2_Indice':
        handle_Panneau2_Indice_event(game, player, npc)

    if npc.name == 'Panneau3_Toilettes':
        handle_Panneau3_Toilettes_event(game, player, npc)

    if npc.name == 'Panneau4_Scène_Errès':
        handle_Panneau4_Scène_Errès_event(game, player, npc)

    if npc.name == 'PNJ4':
        handle_PNJ4_event(game, player, npc)

    if npc.name == 'PNJ5':
        handle_PNJ5_event(game, player, npc)

    if npc.name == 'PNJ6':
        handle_PNJ6_event(game, player, npc)

    if npc.name == 'portier':
        handle_portier_event(game, player, npc)

    if npc.name == 'Gandalf1':
        handle_Gandalf1_event(game, player, npc)

    if npc.name == 'Screen1':
        handle_Screen1_event(game, player, npc)
#-------------------------------------------------------------------

#PNJ MONDE 2---------------------------------------------------------
    if npc.name == 'Gandalf2':                                       
        handle_Gandalf2_event(game, player, npc)

    if npc.name == 'Panneau5_Indice':                                       
        handle_Panneau5_Indice_event(game, player, npc)

    if npc.name == 'Panneau6_Scene_Erres':
        handle_Panneau6_Scene_Erres_event(game, player, npc)

    if npc.name == 'PNJ7':                                       
        handle_PNJ7_event(game, player, npc)

    if npc.name == 'PNJ8':                                       
        handle_PNJ8_event(game, player, npc)

    if npc.name == 'PNJ9':                                       
        handle_PNJ9_event(game, player, npc)

    if npc.name == 'PNJ10':                                       
        handle_PNJ10_event(game, player, npc)

    if npc.name == 'Maison_papier':                                       
        handle_Maison_papier_event(game, player, npc)

    if npc.name == 'Fantome_du_lac':                                       
        handle_Fantome_du_lac_event(game, player, npc)

    if npc.name == 'Clef':
        handle_Clef_event(game, player, npc)

    if npc.name == 'un':
        handle_un_event(game, player, npc)

    if npc.name == 'deux':                                       
        handle_deux_event(game, player, npc)

    if npc.name == 'trois':                                       
        handle_trois_event(game, player, npc)

    if npc.name == 'quatre':                                       
        handle_quatre_event(game, player, npc)

    if npc.name == 'cinq':                                       
        handle_cinq_event(game, player, npc)

    if npc.name == 'six':                                       
        handle_six_event(game, player, npc)

    if npc.name == 'sept':                                       
        handle_sept_event(game, player, npc)

    if npc.name == 'huit':                                       
        handle_huit_event(game, player, npc)

    if npc.name == 'neuf':                                       
        handle_neuf_event(game, player, npc)

    if npc.name == 'dix':                                       
        handle_dix_event(game, player, npc)

    if npc.name == 'onze':                                       
        handle_onze_event(game, player, npc)

    if npc.name == 'douze':                                       
        handle_douze_event(game, player, npc)

    if npc.name == 'treize':                                       
        handle_treize_event(game, player, npc)

    if npc.name == 'quatorze':                                       
        handle_quatorze_event(game, player, npc)

    if npc.name == 'quinze':                                       
        handle_quinze_event(game, player, npc)

    if npc.name == 'Panneau6_2_toilettes':                                       
        handle_Panneau6_2_toilettes_event(game, player, npc)
        
#-----------------------------------------------------------------------------

#PNJ MONDE 3 -----------------------------------------------------------------
    if npc.name == 'PNJ11':                                       
        handle_PNJ11_event(game, player, npc)

    if npc.name == 'PNJ12':                                       
        handle_PNJ12_event(game, player, npc)

    if npc.name == 'PNJ13':                                       
        handle_PNJ13_event(game, player, npc)

    if npc.name == 'PNJ14':                                       
        handle_PNJ14_event(game, player, npc)

    if npc.name == 'Panneau7':                                       
        handle_Panneau7_event(game, player, npc)

    if npc.name == 'Panneau9':                                       
        handle_Panneau9_event(game, player, npc)

    if npc.name == 'Panneau10':                                       
        handle_Panneau10_event(game, player, npc)

    if npc.name == 'portier3':                                       
        handle_portier3_event(game, player, npc)

    if npc.name == 'Gandalf3':                                       
        handle_Gandalf3_event(game, player, npc)
#----------------------------------------------------------------------------------

#PNJ MONDE 4 ------------------------------------------------------------------------
    if npc.name == 'bibliothèque':                                       
        handle_bibliothèque_event(game, player, npc)

    if npc.name == 'fish':                                       
        handle_fish_event(game, player, npc)

    if npc.name == 'panneau11':                                       
        handle_panneau11_event(game, player, npc)

    if npc.name == 'panneau12':                                       
        handle_panneau12_event(game, player, npc)

    if npc.name == 'panneau13':                                       
        handle_panneau13_event(game, player, npc)

    if npc.name == 'panneau14':                                       
        handle_panneau14_event(game, player, npc)

    if npc.name == 'panneau15':                                       
        handle_panneau15_event(game, player, npc)

    if npc.name == 'panneau16':                                       
        handle_panneau16_event(game, player, npc)

    if npc.name == 'PNJ15':                                       
        handle_PNJ15_event(game, player, npc)

    if npc.name == 'PNJ16':                                       
        handle_PNJ16_event(game, player, npc)

    if npc.name == 'PNJ17':                                       
        handle_PNJ17_event(game, player, npc)

    if npc.name == 'PNJ18':                                       
        handle_PNJ18_event(game, player, npc)

    if npc.name == 'PNJ19':                                       
        handle_PNJ19_event(game, player, npc)

    if npc.name == 'portier4':                                       
        handle_portier4_event(game, player, npc)
      
    if npc.name == 'grenouille':                                       
        handle_grenouille_event(game, player, npc)

    if npc.name == 'serpent':                                       
        handle_serpent_event(game, player, npc)

    if npc.name == 'lezard':                                       
        handle_lezard_event(game, player, npc)

    if npc.name == 'bocal':                                       
        handle_bocal_event(game, player, npc)

    if npc.name == 'baton':                                       
        handle_baton_event(game, player, npc)

    if npc.name == 'herbe':                                       
        handle_herbe_event(game, player, npc)

    if npc.name == 'portier4_2':                                       
        handle_portier4_2_event(game, player, npc)

    if npc.name == 'fish2':                                       
        handle_fish2_event(game, player, npc)

    if npc.name == 'portier4_2_cache':                                       
        handle_portier4_2_cache_event(game, player, npc)

    if npc.name == 'farine':                                       
        handle_farine_event(game, player, npc)

    if npc.name == 'Gandalf4':                                       
        handle_Gandalf4_event(game, player, npc)
#----------------------------------------------------------------------------------------------------------

#PNJ MONDE 5 ------------------------------------------------------------------------
    if npc.name == 'portier5':                                       
        handle_portier5_event(game, player, npc)

    if npc.name == 'porte_close':                                       
        handle_porte_close_event(game, player, npc)

    if npc.name == 'Event_Invisible':                                       
        handle_Event_Invisible_event(game, player, npc)

    if npc.name == 'Event_Invisible2':                                       
        handle_Event_Invisible2_event(game, player, npc)

    if npc.name == 'Gandalf5':
        # Quand Gandalf5 est déjà en mode "suit", il ne doit plus déclencher son event.
        if not getattr(game, "gandalf5_following", False):
            handle_Gandalf5_event(game, player, npc)

    if npc.name == 'Gandalf5_1':                                       
        handle_Gandalf5_1_event(game, player, npc)

    if npc.name == 'Panneau_Place':                                       
        handle_Panneau_Place_event(game, player, npc)

    if npc.name == 'PNJ20':                                       
        handle_PNJ20_event(game, player, npc)

    if npc.name == 'PNJ21':                                       
        handle_PNJ21_event(game, player, npc)

    if npc.name == 'PNJ22':                                       
        handle_PNJ22_event(game, player, npc)

    if npc.name == 'PNJ23':                                       
        handle_PNJ23_event(game, player, npc)

    if npc.name == 'PNJ24':                                       
        handle_PNJ24_event(game, player, npc)

    if npc.name == 'panneau17':                                       
        handle_panneau17_event(game, player, npc)

    if npc.name == 'panneau18':                                       
        handle_panneau18_event(game, player, npc)

    if npc.name == 'tag_maison':                                       
        handle_tag_maison_event(game, player, npc)

    if npc.name == 'enfant5':                                       
        handle_enfant5_event(game, player, npc)
#----------------------------------------------------------------------------------------------------------

#PNJ MONDE 5 ------------------------------------------------------------------------
    if npc.name == 'Fig_Arbre':                                       
        handle_Fig_Arbre_event(game, player, npc)

    if npc.name == 'Fig_Voiture':                                       
        handle_Fig_Voiture_event(game, player, npc)

    if npc.name == 'Fig_Ouragan':                                       
        handle_Fig_Ouragan_event(game, player, npc)

    if npc.name == 'Fig_Orange':                                       
        handle_Fig_Orange_event(game, player, npc)

    if npc.name == 'Fig_Lune':                                       
        handle_Fig_Lune_event(game, player, npc)

    if npc.name == 'Fig_Enfant':                                       
        handle_Fig_Enfant_event(game, player, npc)
        
    if npc.name == 'PNJ24_1':                                       
        handle_PNJ24_1_event(game, player, npc)

    if npc.name == 'PNJ25':                                       
        handle_PNJ25_event(game, player, npc)

    if npc.name == 'PNJ26':                                       
        handle_PNJ26_event(game, player, npc)

    if npc.name == 'PNJ27':                                       
        handle_PNJ27_event(game, player, npc)

    if npc.name == 'panneau19':                                       
        handle_panneau19_event(game, player, npc)

    if npc.name == 'panneau20':                                       
        handle_panneau20_event(game, player, npc)

    if npc.name == 'TV6':                                       
        handle_TV6_event(game, player, npc)

    if npc.name == 'portier6':                                       
        handle_portier6_event(game, player, npc)

    if npc.name == 'Gandalf6':                                       
        handle_Gandalf6_event(game, player, npc)
