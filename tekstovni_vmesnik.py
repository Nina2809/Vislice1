import model

def izpis_igre(igra):
    return """==================================================
{geslo}
Napačne črke: {napacne_crke}
ugibaš še {stevilo}.krat.
=================================================""".format(
    geslo=igra.pravilni_del_gesla(),
    napacne_crke=igra.nepravilni_ugibi(),
    stevilo=model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo

)

def izpis_zmage(igra):
    return "Čestitke! uganil/a si geslo {}.".format(igra)

def izpis_parza(igra):
    return "Več sreče prihodnič!"

def zahtevaj_vnos()
    return input ("Ugibaj: ")

def pozeni_vmesnik():
    igra = model.nova_igra()
        while True:
        print (izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(uzpis_zmage(igra))
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
        
pozeni_vmesnik