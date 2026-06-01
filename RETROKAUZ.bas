10 rem *** retrokauz game collector v1.0 (gpl) ***
20 dim g$(100),e$(100),s$(100),m$(100),y(100),r(100)
25 h=6:r=14:s=154:rem h=hintergrund r=rahmen s=schrift
30 c=0:d$="games"
40 gosub 1000
45 gosub 9000:rem farben setzen

60 rem *** startbildschirm ***
70 print chr$(147);chr$(s)
80 print "========================================"
90 print "      retrokauz game-collector v1.0     "
100 print "========================================"
110 print "(c) 2026 dennis rapp - www.retrokauz.de"
120 print "licensed under gnu gpl v3.0"
130 print ""
140 print "laden...  [";
141 for i=1 to 10
142 for j=1 to 430:next j
143 print "=";
144 next i
145 print "]"


200 print chr$(147);chr$(s)
210 print "================================="
220 print "<           hauptmenue          >"
230 print "================================="
240 print ""
250 print "  [ 1 ] neuer eintrag"
260 print "  [ 2 ] spiele anzeigen"
270 print "  [ 3 ] spiele filtern"
280 print "  [ 4 ] eintrag loeschen"
290 print "  [ 5 ] statistik"
300 print "  [ 6 ] farbschema waehlen"
306 print "  [ 7 ] backup wiederherstellen"
307 print "  [ 8 ] programm beenden"
310 print ""
370 print "========================================"
380 print "eintraege:";c
400 input "auswahl";a$
410 if a$="1" then gosub 3000
420 if a$="2" then gosub 7000
430 if a$="3" then gosub 5000
440 if a$="4" then gosub 6000
450 if a$="5" then gosub 8000
455 if a$="6" then gosub 9100
460 if a$="7" then gosub 2200
465 if a$="8" then gosub 1500
470 goto 200

1000 rem *** laden ***
1010 open 1,8,2,d$+",s,r"
1015 if st>63 then print "Datei '";d$;"' nicht gefunden!":close 1:c=0:return:rem datei nicht da
1030 input#1,c
1035 if c=0 then close 1:return
1040 for i=1 to c
1050 input#1,g$(i)
1060 input#1,e$(i)
1070 input#1,y(i)
1080 input#1,s$(i)
1090 input#1,m$(i)
1100 input#1,r(i)
1105 if st<>0 and st<>64 then i=c:rem 64=eof (ende ok)
1110 next i
1120 close 1:return

1500 rem *** programm beenden ***
1505 print chr$(147);chr$(s)
1510 print "================================="
1515 print "<       programm beenden? (j/n)      > "
1520 print "================================="  
1525 print ""   
1530 input a$:if a$<>"j" then return
1535 h=6:r=14:s=154:gosub 9000:print chr$(147);"auf wiedersehen! der retrokauz dankt!":end
 

2000 rem *** speichern ***
2001 print chr$(147);chr$(s)
2002 print "================================="
2003 print "<       speichere daten...      >"
2004 print "================================="
2005 if c > 0 then goto 2010
2006 print "kein eintrag vorhanden!"
2007 print "bitte enter druecken"
2008 get a$:if a$<>chr$(13) then 2008
2009 return
2010 rem *** backup & speichern ***
2011 open 15,8,15
2012 print#15,"s0:"+d$+".bak"
2013 print#15,"r0:"+d$+".bak="+d$
2014 close 15
2015 open 1,8,2,d$+",s,w"
2020 print#1,c
2030 for i=1 to c
2040 print#1,g$(i)
2050 print#1,e$(i)
2060 print#1,y(i)
2062 print#1,s$(i)
2064 print#1,m$(i)
2066 print#1,r(i)
2068 next i
2069 close 1
2070 open 15,8,15:input#15,en,em$,et,es:close 15
2080 if en > 0 and en <> 62 then print "fehler:";en;em$:goto 2007
2090 print "erfolgreich gespeichert.":goto 2007

2200 rem *** backup-manager ***
2210 print chr$(147);chr$(s)
2211 print "================================="
2212 print "<       backup-manager          >"
2213 print "================================="
2215 print "pruefe backup..."
2220 open 1,8,2,d$+".bak,s,r"
2225 if st>63 then print "kein backup gefunden.":close 1:goto 3180
2230 close 1
2235 print "backup vorhanden."
2240 print "aktuelle daten werden ueberschrieben!"
2245 print "wirklich wiederherstellen? (j/n)"
2250 get a$:if a$="" then 2250
2255 if a$<>"j" then return
2260 print "stelle wieder her..."
2265 open 15,8,15
2270 print#15,"s0:"+d$
2275 print#15,"r0:"+d$+"="+d$+".bak"
2280 close 15
2282 c=0:gosub 1000
2285 print "backup geladen! eintraege:";c
2290 goto 3180


3000 rem *** neuer eintrag ***
3005 print chr$(147);chr$(s)
3006 print "================================="
3007 print "<         neuer eintrag         >"
3008 print "================================="
3010 if c=100 then print "liste voll!":goto 3180
3020 c=c+1:print "eintrag nr.";c
3030 print "----------------------------------------"
3040 input "name  : ";g$(c)
3050 input "studio: ";e$(c)
3060 input "jahr  : ";y(c)
3070 if y(c)<1950 or y(c)>2050 then print "jahr 1950-2050!":goto 3060
3090 print chr$(147);"waehle system (1-18):"
3100 print "1:nes        7:atari st  13:ps2"
3102 print "2:snes       8:genesis   14:ps3"
3104 print "3:gameboy    9:saturn    15:c64"
3106 print "4:famicom   10:xbox      16:c16"
3108 print "5:atari 4/8 11:ps1       17:ti-99"
3110 print "6:atari vcs 12:pc-dos    18:amstrad"
3112 input s1:if s1<1 or s1>18 then 3090
3114 restore:for i=1 to s1:read s$(c):next i
3120 print "medium: 1:disk 2:tape 3:cart 4:cd/dvd"
3122 print "        5:iso-datei"
3124 input m1:if m1<1 or m1>5 then 3120
3126 if m1=1 then m$(c)="disk":if m1=2 then m$(c)="tape"
3128 if m1=3 then m$(c)="cart":if m1=4 then m$(c)="cd/dvd"
3130 if m1=5 then m$(c)="iso"
3150 print "rating (1 sehr schlecht - 10 sehr gut):"
3152 input r(c):if r(c)<1 or r(c)>10 then 3150
3160 print "----------------------------------------"
3161 print "eintraege speichern? (j/n)"
3164 get a$:if a$="n" then c=c-1:return
3165 if a$<>"j" then 3164
3168 gosub 4000:gosub 2000:return
3180 print "bitte enter druecken"
3181 get a$:if a$<>chr$(13) then 3181
3182 return
3190 data nes,snes,gameboy,famicom,atari 4/8,vcs,atari st,genesis,saturn,xbox,ps1,pc-dos,ps2,ps3,c64,c16,ti-99/4a,amstrad

4000 rem *** bubble sort ***
4010 if c < 2 then return
4020 for i = 1 to c-1:for j = 1 to c-i
4040 if g$(j) <= g$(j+1) then 4100
4050 t$=g$(j):g$(j)=g$(j+1):g$(j+1)=t$:t$=e$(j):e$(j)=e$(j+1):e$(j+1)=t$
4070 t=y(j):y(j)=y(j+1):y(j+1)=t:t$=s$(j):s$(j)=s$(j+1):s$(j+1)=t$
4085 t$=m$(j):m$(j)=m$(j+1):m$(j+1)=t$:t=r(j):r(j)=r(j+1):r(j+1)=t
4100 next j:next i:return

5000 rem *** spiele suchen & filtern ***
5010 print chr$(147);chr$(s)
5011 print "================================="
5012 print "<        suche & filter         >"
5013 print "================================="
5020 print " 1:system  2:name (teilsuche)"
5022 print " 3:medium  4:rating  5:jahr"
5030 print "---------------------------------"
5040 input "wahl";f$
5050 f1=val(f$):if f1<1 or f1>5 then return
5060 input "begriff/wert";t$:t$=left$(t$,20)
5080 print chr$(147):k=0
5090 for i=1 to c
5100 if f1=1 and s$(i)=t$ then gosub 5500:k=k+1:goto 5130
5105 if f1<>2 then 5115
5107 l1=len(g$(i)):l2=len(t$):if l2>l1 then 5115
5108 for p=1 to (l1-l2)+1
5110 if mid$(g$(i),p,l2)=t$ then gosub 5500:k=k+1:p=l1
5112 next p:goto 5130
5115 if f1=3 and m$(i)=t$ then gosub 5500:k=k+1
5116 if f1=4 and r(i)=val(t$) then gosub 5500:k=k+1
5118 if f1=5 and y(i)=val(t$) then gosub 5500:k=k+1
5130 next i
5140 if k=0 then print "keine treffer."
5150 print "treffer:";k:goto 3180

5500 print i;". ";chr$(28);g$(i);chr$(s) :rem name rot, rest schema-farbe
5520 print "   ";s$(i);"/";m$(i);" (";y(i);") r:";r(i)
5530 print "----------------------------------------"
5540 return

6000 rem *** loeschen mit bestaetigung ***
6010 print chr$(147);chr$(s)
6011 print "========================================"
6012 print "<           eintrag loeschen           >"
6013 print "========================================"
6015 if c=0 then print "liste ist leer.":goto 3180
6020 for i=1 to c:print i;".";g$(i):next i
6030 input "nummer zum loeschen (0=abbruch)";n
6040 if n<1 or n>c then return
6060 print "wirklich ";chr$(158);g$(n);chr$(s);" loeschen?"
6070 input "(j/n)";a$:if a$<>"j" then return
6080 for i=n to c-1
6090 g$(i)=g$(i+1):e$(i)=e$(i+1):y(i)=y(i+1)
6100 s$(i)=s$(i+1):m$(i)=m$(i+1):r(i)=r(i+1)
6110 next i
6120 c=c-1:print "geloescht.":goto 3180

7000 rem *** anzeigen ***
7010 p=1
7020 print chr$(147);chr$(s)
7021 print "========================================"
7022 print "<             spieleliste              >"
7023 print "========================================"
7025 if c=0 then print "keine eintraege!":goto 3180
7030 e=p+3:if e>c then e=c
7050 print "----------------------------------------"
7060 for i=p to e
7070 print i;". ";chr$(28);g$(i);chr$(s) :rem name dunkelrot
7080 print "   ";s$(i);"/";m$(i);" (";y(i);") rating:";r(i)
7090 print "   studio: ";e$(i)
7100 print "----------------------------------------"
7110 next i
7120 print "(leertaste) weiter  (enter) ende"
7125 get a$:if a$="" then 7125
7130 if a$=" " then p=p+4:if p<=c then 7020
7140 return


8000 rem *** statistik ***
8010 print chr$(147);chr$(s)
8011 print "========================================"
8012 print "<              statistik               >"
8013 print "========================================"
8015 if c=0 then print "liste ist leer.":goto 3180
8020 rt=0:for i=1 to c:rt=rt+r(i):next i
8030 print "anzahl spiele    : ";c
8040 print "bewertung durchschnitt : ";int((rt/c)*10)/10
8050 print "----------------------------------------"
8060 print "spiele pro system:"
8070 restore:for i=1 to 18:read sy$:sc=0
8080 for j=1 to c:if s$(j)=sy$ then sc=sc+1
8090 next j
8100 if sc>0 then print sy$;tab(15);": ";sc
8110 next i
8120 print "----------------------------------------"
8130 goto 3180

9000 poke 53280,r:poke 53281,h:print chr$(s):return
9100 rem *** farbauswahl ***
9110 print chr$(147);chr$(s)
9111 print "================================="
9112 print "<       farbschema waehlen      >"
9113 print "================================="
9114 print ""
9120 print "  [ 1 ] classic (cyan on blue)"
9130 print "  [ 2 ] hacker (green on black)"
9140 print "  [ 3 ] retro (black and white)"
9150 input f:if f=1 then h=6:r=14:s=154 :rem s=154 ist c64-hellblau
9160 if f=2 then h=0:r=0:s=30  :rem s=30 ist gruen
9170 if f=3 then h=15:r=12:s=144 :rem s=144 ist schwarz
9180 gosub 9000:return
