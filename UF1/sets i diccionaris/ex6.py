NacionalitatMarca = {
"Seat": "Espanya",
"Renault": "França",
"Volkswaguen": "Alemanya",
"Citroën": "França",
"Opel": "Alemanya",
"Peugeot": "França",
"Fiat": "Itàlia",
"BMW": "Alemanya",
"Mercedes": "Alemanya",
"Škoda": "Txèquia",
"Mini": "Regne Unit",
"Smart": "Alemanya",
"Alfa Romeo": "Itàlia",
"Lancia": "Itàlia",
"Kia": "Corea del Sud",
"Hiundai": "Corea del Sud",
"Dacia": "Rumania",
"Toyota": "Japó",
"Honda": "Japó",
"Misubishi": "Japó",
"Jeep": "EEUU",
"Tesla": "EEUU"
}

for marca,pais in NacionalitatMarca.items(): #key,value
    if marca == "Mini":
        print(pais)