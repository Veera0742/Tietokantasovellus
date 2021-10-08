# Tietokantasovellus

**Luontoretkeilysovellus**

Sovelluksessa näkyy tietyn alueen retkeily- ja telttailualueet, joista voi etsiä tietoa ja lukea arvioita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

1. Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
2. Käyttäjä näkee retkeilypaikan kartalla ja voi painaa sen kohdasta, jolloin siitä näytetään lisää tietoa (kuten kuvaus ja palvelut).
3. Käyttäjä voi antaa arvion (tähdet ja kommentti) paikasta ja lukea muiden antamia arvioita.
4. Ylläpitäjä voi lisätä ja poistaa retkeilypaikkoja sekä määrittää siitä näytettävät tiedot.
5. Käyttäjä voi etsiä kaikki retkeilypaikat, joiden kuvauksessa on annettu sana.
6. Käyttäjä näkee myös listan, jossa retkeilypaikat on järjestetty parhaimmasta huonoimpaan arvioiden mukaisesti.
7. Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion.
8. Ylläpitäjä voi luoda ryhmiä, joihin retkeilyaluita voi luokitella. Alue voi kuulua yhteen tai useampaan ryhmään.

Tilanne 23.9.2021:
Tällä hetkellä sovellukseen voi luoda uudet tunnukset ja kirjautua sisään. Sisäänkirjautunut käyttäjä voi nähdä muutamia esimerkki retkeilypaikkoja ja niiden lyhyet kuvaukset. Sovellukseen ei ole vielä luotu eri käyttäjä rooleja eikä kirjoittaa arvioita. Tällä hetkellä käytössä kaksi tietokantaa. 

Tilanne 8.10.2021:
Tällä hetkellä sovellukseen voi luoda uudet tunnukset ja kirjautua sisään. Sisäänkirjautumisen yhteydessä voi valita onko käyttäjä vai admin. Sisäänkirjautunut käyttäjä voi nähdä muutamia esimerkki retkeilypaikkoja ja niiden lyhyet kuvaukset, kirjoittaa arvosteluja sekä nähdä niitä ja lukea erillisen linkin kautta kohteen palveluista. Käyttäjä voi myös etsiä kohteita joko nimellä tai alueittain. Tällä hetkellä vain kaksi Uudenmaan kohdetta luotu. Admin oikeuksilla voi edellä mainittujen lisäksi luoda uusia kohteita, kirjoittaa niistä kuvauksia sekä kertoa kohteen palveluista. Admin voi myös poistaa kohteita. Tällä hetkellä käytössä on viisi tietokantaa. 

Sovellusta voi testata Herokussa: [Heroku linkki](https://tietokantasovellus2.herokuapp.com/)
