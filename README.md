# README

## Suomi

Pieni koodi tekstitysten generointiin ["Kalevala laulettuna"](https://www.youtube.com/channel/UCqoyq2JdWolL_bOOaR904bQ)-videosarjaan. Suomenkieliset tekstitykset on otettu vuonna 1849 valmistuneesta ns. Uudesta Kalevalasta (28. painos). Englanninkieliset tekstitykset ovat W. F. Kirbyn käännöksestä vuodelta 1907.

Tekstitykset generoituvat .srt-formaatissa ja ne löytyvät kansiosta subtitles/. Tekstityksiä generoitaessa osa säkeiden alkuajoista määritetään manuaalisesti, minkä jälkeen algoritmi interpoloi loput tekstien vaihtumisajankohdat.

### Käyttöohje

Jos haluat käyttää koodia tekstitysten lisäämiseen uuteen runoon, onnistuu se muokaamalla generate.py tiedostoa. Aloita kopioimalla jokin jo olemassa olevista tekstityksiä generoivista funktioista (esim. runo_1() riveillä 126-154).

Anna funktiolle uusi nimi muokkaamalla riviä
```python
    def runo_1(test=False):
```

Vaihda säkeiden alkuajat vastaamaan videota riveillä
```python
    time_stamps = { 1:      time(0,12.6),
                    25:     time(1,44.2),
                    50:     time(3,15.5),
                    75:     time(4,44.5),
                    100:    time(6,10.6),
                    125:    time(7,35.2),
                    150:    time(8,58.5),
                    175:    time(10,20.6),
                    200:    time(11,42.6),
                    225:    time(13,3.7),
                    250:    time(14,24.3),
                    275:    time(15,45.1),
                    300:    time(17,5.4),
                    325:    time(18,25.7),
                    345:    time(19,30),
                    346:    time(19,33)}
```
Jokaisen rivin ensimmäinen numero tarkoittaa säkeen numeroa ja funktiokutsun time() sisällä olevat luvut kyseisen säkeen alkamisaikaa minuutteina ja sekunteina. Sekunnit kannattaa antaa kymmenyksen tarkkuudella. Ensimmäinen ja viimeinen säe tulee aina antaa. Jos runo on pidempi kuin tässä esimerkissä, joudut lisäämään rivejä. Joka 25:nnen säkeen määrittäminen vaikuttaisi riittävältä. Lisäinformaatiota löytyy runo_1()-funktion kommenteista tiedostossa generate.py.

Vaihda numero rivillä
```python
    generate(1, time_stamps, repeat=True, test=test)
```
vastaamaan sen runon numeroa, jonka tekstejä olet generoimassa.

Suorita luomasi funktio esimerkiksi muokkaamalla tiedoston loppua
```python
if __name__=="__main__":
    runo_1()
    runo_2()
    runo_3()
    runo_4()
    runo_5()
    runo_6()
    runo_7()
```
Voit korvata funktiokutsut runo_1(), runo_2(), jne. luomallasi funktiolla. Nyt uudet tekstitykset generoituvat, kun suoritat koodin Python-tulkilla (versio 3):
```
$ python generate.py
```


## English

A small code for generating captions/subtitles for ["Kalevala laulettuna"](https://www.youtube.com/channel/UCqoyq2JdWolL_bOOaR904bQ) video series. The Finnish captions are taken from the 1849 version of Kalevala (28th edition). The English subtitles are from the 1907 translation by W. F. Kirby.

The subtitles are generated in .srt-format and they can be found in subtitles/ directory. When generating the subtitles, some of the starting times of the verses are defined manually. The rest of the times are interpolated algorithmically.

### How-to

If you wish to use the code for adding subtitles for a new poem, it can be done by modifying the generate.py file. Start by copying one of the existing subtitle generation functions (such as runo_1() on lines 126-154).

Give the function a new name by modifying the row
```python
def runo_1(test=False):
```

Change the starting times of the verses to correspond to the video on the lines
```python
    time_stamps = { 1:      time(0,12.6),
                    25:     time(1,44.2),
                    50:     time(3,15.5),
                    75:     time(4,44.5),
                    100:    time(6,10.6),
                    125:    time(7,35.2),
                    150:    time(8,58.5),
                    175:    time(10,20.6),
                    200:    time(11,42.6),
                    225:    time(13,3.7),
                    250:    time(14,24.3),
                    275:    time(15,45.1),
                    300:    time(17,5.4),
                    325:    time(18,25.7),
                    345:    time(19,30),
                    346:    time(19,33)}
```
The first number on each line stands for the number of a verse. The numbers inside the function call time() are the corresponding times as minutes and seconds. The seconds should be given with an accuracy of 0.1 seconds. The first and last verses should always be given. If the poem is longer than the one in the example, you will have to add lines. It seems that defining every 25th verse gives good results. For more information, check the comments in the runo_1() function of generate.py.

Change the number on the line
```python
    generate(1, time_stamps, repeat=True, test=test)
```
to corrspond to the poem that you are working on.

Execute the new function, for example, by editing the end of the file
```python
if __name__=="__main__":
    runo_1()
    runo_2()
    runo_3()
    runo_4()
    runo_5()
    runo_6()
    runo_7()
```
You can replace the function calls runo_1(), runo_2(), ... with the new function. Now the subtitles are generated when you execute the code with a Python (version 3) interpreter:
```
$ python generate.py
```