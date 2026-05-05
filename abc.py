alianza = [{"nombre": "Años 90", "cantidad_partidos": 0}, {"nombre": "Años 2000", "cantidad_partidos": 3}]
partido = [{"dia": 3, "mes": "mayo", "alianza": "Años 90"}, {"dia": 3, "mes": "mayo", "alianza": "Años 2000"}]
evento = [{"dia": 4, "mes": "mayo", "nombre": "Inicio de Jardinera, Baby Futbol y control estricto de asistencia"},
          {"dia": 18, "mes": "mayo", "nombre": "Presentación Oficial de Animadores"}]

for i, a in enumerate(alianza):
    for p in partido:
        if p["alianza"] == a["nombre"]:
            alianza[i]["cantidad_partidos"] += 1

for a in alianza:
 if a["cantidad_partidos"] > 1:
    print("La alianza de los " + a["nombre"] + " tiene " + str(a["cantidad_partidos"]) + " partidos en mes")
 else:
    print("La alianza de los " + a["nombre"] + " tiene " + str(a["cantidad_partidos"]) + " partido en mes")


for p in partido:
    print("La alianza de los " + p["alianza"] + " tiene un partido el " + str(p["dia"]) + " de " + str(p["mes"]))

for e in evento:
    print(e["nombre"] + " ocurre el " + str(e["dia"]) + " de " + str(e["mes"]))