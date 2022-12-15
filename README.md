# FRA-knäck 3 – Lös analytikertestet

Lösningsförslag till [FRA-knäck 3](https://www.fra.se/nyheter/nyheter/nyhetsarkiv/news/fraknack3losanalytikertestet.5.3023631f184a985bf6933a.html)

1. Ladda ned filen analytikertestet.pcap från länken ovan och [Wireshark](https://www.wireshark.org)
2. Exportera käll- och destinationsadresserna i filen till en text-fil.

```
  tshark -r analytikertestet.pcap -T fields -e ip.dst -e ip.src > ./data.txt
```

3. Ladda ned och installera [Python 3](https://www.python.org/)
4. Lägg till modulerna networkx och matplotlib.pyplot

```
  pip install networkx matplotlib.pyplot
```

5. Kör fra_knack3.py. Den läser in ip-adresserna från filen i steg två ovan och ritar en riktad multigraf över vilken källadress har skickat paket till vilken destinationsadress.

```
  python3 fra_knack3.py
```

6. Analysera grafen
   1. Vilket IP-nummer har chefen för organisationen? (tex: 10.10.10.2)
      Chefen har antagligen det IP-nummer alla terrorister rapporterar till.
   2. Vilket IP-nummer har troligaste ställföreträdaren till chefen?
      I grafen finns det en adress som chefen har skickat trafik till. Vi kan anta att detta är ställföreträdarens IP-nummer.
   3. Hur många celler består gruppen av?
      Här kan vi antingen räkna antalet IP-nummer som har skickat trafik till chefen, eller antalet kluster i grafen.
   4. Vilka två terrorister sammanbor mest troligt?
      I en av cellerna finns det två adresser som inte har skickat någon trafik mellan sig. Eftersom de två terroristerna kan prata direkt med varandra är det troligen dessa två IP-nummer som innehas av de två sammanboende terroristerna.
