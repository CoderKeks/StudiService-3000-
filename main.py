from Service.KursService import KursService
from Service.StudierendeService import StudierendeService
from Models.Kurs import Kurs

kurs_service = KursService()
studierender_service = StudierendeService()

    
def menu_layer_two_option_1():
    studierende_string_list = "\n".join([str(studierender) for studierender in studierender_service.get_all()])
    if len(studierende_string_list) == 0:
        response_2 = '4'
    else:
        response_2 = input(f"""
#########################################                     

{studierende_string_list}

#########################################


Was wollen Sie tun?
    1. Einen Studierenden genauer betrachten
    2. Einen Studierenden hinzufügen
    3. Einen Studierenden löschen
    4. Zurück gehen



""")
        
def menu_layer_two_option_2():
    studierende_string_list = "\n".join([str(studierender) for studierender in studierender_service.get_all()])
    if len(studierende_string_list) == 0:
        response_2 = '4'
    else:
        response_2 = input(f"""
#########################################                     

{studierende_string_list}

#########################################


Was wollen Sie tun?
    1. Einen Studierenden genauer betrachten
    2. Einen Studierenden hinzufügen
    3. Einen Studierenden löschen
    4. Zurück gehen



""")



def menu_layer_one():
    response = input("""
Was wollen Sie tun?
    1. Studierende anzeigen und bearbeiten
    2. Kurse anzeigen und bearbeiten



""")
    if response == '1':
        menu_layer_two_option_1()
    elif response == '2':
        menu_layer_two_option_2()


if __name__ == "__main__":
    while True:
        menu_layer_one()


    # kurs_service.create(Kurs('Deutsch', 'Ruhl', 1))
    # print(kurs_service.getAll())
    