# README

## Suomi

Pieni koodi tekstitysten generointiin ["Kalevala laulettuna"](https://www.youtube.com/channel/UCqoyq2JdWolL_bOOaR904bQ)-videosarjaan. Suomenkieliset tekstitykset on otettu vuonna 1849 valmistuneesta ns. Uudesta Kalevalasta (28. painos). Englannin kieliset tekstitykset ovat W. F. Kirbyn käännöksestä vuodelta 1907.

Tekstitykset generoituvat .srt-formaatissa ja ne löytyvät kansiosta subtitles/. Tekstityksiä generoitaessa osa säkeiden alkuajoista määritetään manuaalisesti, minkä jälkeen algoritmi interpoloi loput tekstien vaihtumisajankohdat. Yhden säkeen määrittäminen 25:stä vaikuttaisi toimivan riittävän hyvin.

## English

A small code for generating captions/subtitles for ["Kalevala laulettuna"](https://www.youtube.com/channel/UCqoyq2JdWolL_bOOaR904bQ) video series. The Finnish captions are taken from the 1849 version of Kalevala (28th edition). The English subtitles are from the 1907 translation by W. F. Kirby.

The subtitles are generated in .srt-format and they can be found in subtitles/ directory. When generating the subtitles, some of the starting times of the verses are defined manually. The rest of the times are interpolated algorithmically. It seems that defining one in 25 verses manually gives good results.