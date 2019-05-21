import bottle
import model
# uvozimo 
vislice = model.Vislice()
id = vislice.nova_igra()
igra, stanje = vislice.igre[id]

@bottle.get('/')
def index():
    #Z dekoratorjem bottle.get na naslov "/" pošljete predlogo index.tpl.
    # ta funkcija more vrnt predlogo 
    return bottle.template('index.tpl')
    # v views mapci

@bottle.get('/igra/')
def testiigre():
    return bottle.template('igra.html',id_igra = id, igra = igra, stanje = stanje)
    


# to je funkcija k se skos kopira k prikaze sliko
@bottle.get('/img/<ime>')
def slike(ime):
    return bottle.static_file(ime, root = 'img')


bottle.run(reloader = True, debug = True)
