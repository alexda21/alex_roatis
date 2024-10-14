articol = ("""David Popovici a adus a 91-a medalie de aur pentru România în istoria Jocurilor Olimpice.

Citește mai mult la: https://www.digi24.ro/stiri/sport/alte-sporturi/jo-2024-david-popovici-inoata-in-aceasta-seara-pentru-medalia-de-aur-la-200-m-liber-el-s-a-calificat-cu-cel-mai-bun-timp-2877215

Informaţiile publicate pe site-ul Digi24.ro pot fi preluate, în conformitate cu legislația aplicabilă, doar în limita a 120 de caractere.""")
lungime = len(articol)
jumatate = lungime//2
print(jumatate)
prima_parte = articol[0:jumatate]
majuscule = prima_parte.upper()
print(majuscule)
fara_spatiu = prima_parte.strip()
print(fara_spatiu)
a_doua_parte =  articol[jumatate:]
print(a_doua_parte)
inversate = articol[jumatate:0:-1]
print(inversate)
litere_mari = a_doua_parte.title()
print('litere_mari')
import string
fara_semne = a_doua_parte.translate(str.maketrans(",",string.punctuation))
print('fara_semne')
rezultat =' fara_spatiu+fara_semne'
print(rezultat)

