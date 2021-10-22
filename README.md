# Tietokantasovellus

**Luontoretkeilysovellus**

Sovelluksessa näkyy tietyn alueen retkeily- ja telttailualueet, joista voi etsiä tietoa ja lukea arvioita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
2. Käyttäjä voi antaa arvion (tähdet ja kommentti) paikasta ja lukea muiden antamia arvioita.
3. Ylläpitäjä voi lisätä ja poistaa retkeilypaikkoja sekä määrittää siitä näytettävät tiedot.
4. Käyttäjä voi etsiä kaikki retkeilypaikat, joiden kuvauksessa on annettu sana.
5. Käyttäjä näkee myös listan, jossa retkeilypaikat on järjestetty parhaimmasta huonoimpaan arvioiden mukaisesti.
6. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
7. Ylläpitäjä voi luoda ryhmiä, joihin retkeilyaluita voi luokitella. Alue voi kuulua yhteen tai useampaan ryhmään.

Tilanne 23.9.2021:
Tällä hetkellä sovellukseen voi luoda uudet tunnukset ja kirjautua sisään. Sisäänkirjautunut käyttäjä voi nähdä muutamia esimerkki retkeilypaikkoja ja niiden lyhyet kuvaukset. Sovellukseen ei ole vielä luotu eri käyttäjä rooleja eikä kirjoittaa arvioita. Tällä hetkellä käytössä kaksi tietokantaa. 

Tilanne 8.10.2021:
Tällä hetkellä sovellukseen voi luoda uudet tunnukset ja kirjautua sisään. Sisäänkirjautumisen yhteydessä voi valita onko käyttäjä vai admin. Sisäänkirjautunut käyttäjä voi nähdä muutamia esimerkki retkeilypaikkoja ja niiden lyhyet kuvaukset, kirjoittaa arvosteluja sekä nähdä niitä ja lukea erillisen linkin kautta kohteen palveluista. Käyttäjä voi myös etsiä kohteita joko nimellä tai alueittain. Tällä hetkellä vain kaksi Uudenmaan kohdetta luotu. Admin oikeuksilla voi edellä mainittujen lisäksi luoda uusia kohteita, kirjoittaa niistä kuvauksia sekä kertoa kohteen palveluista. Admin voi myös poistaa kohteita. Tällä hetkellä käytössä on viisi tietokantaa. 

Tilanne 22.10.2021:
Sovellukseen voi luoda uudet tunnukset ja kirjautua sisään. Sisäänkirjautumisen yhteydessä voi valita onko käyttäjä vai admin. Sisäänkirjautunut käyttäjä voi tutkia retkeilypaikkoja nimen perusteella, alueittain tai ryhmittäin. Käyttäjä näkee myös kohteiden top5- listan arvosteluiden perusteella. Kohteesta klikkaamalla käyttäjä voi nähdä niiden lyhyet kuvaukset, kirjoittaa arvosteluja sekä nähdä muiden arvosteluja ja lukea erillisen linkin kautta kohteen palveluista. Käyttäjä voi myös etsiä tiettyä sanaa kohteen kuvauksesta, jolloin tulokseksi tulevat kaikki kohteet, joiden kuvauksessa sana esiintyy. Admin oikeuksilla voi edellä mainittujen lisäksi luoda uusia kohteita, kirjoittaa niistä kuvauksia, sekä luokitella kohteita alueittain sekä ryhmittäin sekä kertoa kohteen palveluista. Admin voi myös poistaa kohteita. Käytössä on kahdeksan tietokantaa. 

Ideoita tulevaisuuden kehittelyyn: Sovellukseen voisi lisätä erikokoisia karttoja, joihin kohteita voisi lisätä ja niitä olisi helppo etsiä. Tällä hetkellä sovellukseen voi lisätä vain yhden palvelun/ryhmän per kohde mutta tulevaisuudessa voisi kehittää mahdollisuuden lisätä useita. Sen lisäksi voisi myös kehittää haun, jolla voisi etsiä kohteita palveluiden perusteella.

Sovellusta voi testata Herokussa: [Heroku linkki](https://tietokantasovellus2.herokuapp.com/)
