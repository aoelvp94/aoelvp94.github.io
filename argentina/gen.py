#!/usr/bin/env python3
"""Generate bilingual Argentina hub teasers + one page per visited province."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FX = 1550  # ~ARS per USD, BNA early Nov 2026


def usd(ars: int) -> str:
    return f"~USD {int(round(ars / FX))}"


def ars_fmt(n: int, lang: str) -> str:
    return f"{n:,}" if lang == "en" else f"{n:,}".replace(",", ".")


def usd_span(ars: int, ars_high: int | None = None) -> str:
    lo = int(round(ars / FX))
    if ars_high is None:
        return f"~USD {lo}"
    hi = int(round(ars_high / FX))
    return f"~USD {lo}–{hi}"


# Park fees: APN, valores vigentes desde 1 jun 2026 (tarifa general = extranjero).
APN = {
    "iguazu_gen": 60000,
    "iguazu_ar": 25000,
    "glaciares": 50000,
    "tdf": 40000,
    "nahuel": 35000,
    "palmar": 25000,
    "cardones": 25000,
    "calilegua": 25000,
    "condorito": 25000,
}

PROVINCES = [
    {
        "slug": "jujuy",
        "region": "norte",
        "es": {
            "name": "Jujuy",
            "where": "NOA · Quebrada de Humahuaca",
            "teaser": "Cerros de colores, pueblos andinos y un ritmo más lento que Buenos Aires.",
            "vibe": "El norte cambia el chip: cerros de colores, pueblos andinos y un ritmo más lento que Buenos Aires. La Quebrada de Humahuaca es Patrimonio de la UNESCO y se siente. Subí con tiempo: la altura se nota.",
            "season": "Ideal may–oct en la Quebrada: cielo claro, noches heladas, altura. Evitá dic–mar si la idea es ruta seca (lluvia y a veces cortes). Abrigo sí o sí después de las 18.",
            "arrive": "Vuelo a JUJ (Horacio Guzmán) desde AEP/EZE (~2 h) o micro desde Retiro (~20–22 h). Muchos combinan Salta + Jujuy en auto o tour. Desde Purmamarca sale el micro a San Pedro de Atacama por el Paso de Jama.",
            "do": [
                "Purmamarca y el Cerro de los Siete Colores, Tilcara, Humahuaca.",
                "Salinas Grandes si el clima da (día completo con la Quebrada).",
                "Calilegua si querés selva de yungas en vez de puna (Parque Nacional, tarifa general APN).",
            ],
            "eat": "Humita, tamales, empanadas jujeñas, locro, llama en algunas cartas. El api con pastelitos si coincidís con feria o invierno.",
            "hack": "El cruce a Chile no es Cristo Redentor: es el Paso de Jama. Andesmar sale de Salta ~1:00, terminal de Jujuy ~2:45, Purmamarca ~3:40, San Pedro ~11:30 (oct. 2026). ~USD 75–100 el tramo. No es un day trip. Detalle en la <a href=\"../#hacks\">hub de hacks</a>.",
        },
        "en": {
            "name": "Jujuy",
            "where": "Northwest · Quebrada de Humahuaca",
            "teaser": "Colored hills, Andean towns, and a slower tempo than Buenos Aires.",
            "vibe": "The north flips the script: colored hills, Andean towns, and a slower tempo than Buenos Aires. The Quebrada de Humahuaca is UNESCO-listed and it shows. Give yourself time: the altitude is real.",
            "season": "Ideal May–Oct in the Quebrada: clear skies, freezing nights, altitude. Avoid Dec–Mar if you want dry roads (rain, occasional closures). A jacket after 6 p.m. is not optional.",
            "arrive": "Fly to JUJ (Horacio Guzmán) from AEP/EZE (~2 h) or a long-distance bus from Retiro (~20–22 h). Plenty of people combine Salta + Jujuy by car or tour. From Purmamarca the bus to San Pedro de Atacama runs Paso de Jama.",
            "do": [
                "Purmamarca and Cerro de los Siete Colores, Tilcara, Humahuaca.",
                "Salinas Grandes if the weather plays along (full day with the Quebrada).",
                "Calilegua if you want yungas jungle instead of puna (national park, APN general fee).",
            ],
            "eat": "Humita, tamales, Jujuy-style empanadas, locro, llama on some menus. Api with pastelitos if you hit a market day or winter.",
            "hack": "The Chile crossing from here is Paso de Jama, not Cristo Redentor. Andesmar leaves Salta ~1:00, Jujuy ~2:45, Purmamarca ~3:40, San Pedro ~11:30 (Oct 2026). ~USD 75–100. Not a day trip. Detail on the <a href=\"../#hacks\">hub hacks</a>.",
        },
        "legs_es": [("bus", "Micro ~20–22 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~20–22 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["salta", "tucuman", "santiago-del-estero", "catamarca"],
        "tours": [
            {
                "url": "https://movitrack.com.ar/excursiones-clasicas",
                "es_name": "Movitrack — Quebrada de Humahuaca",
                "en_name": "Movitrack — Quebrada de Humahuaca",
                "es": "Salida clásica desde Salta (también tienen oficina en San Salvador de Jujuy): Purmamarca, Tilcara, Humahuaca. Día largo; almuerzo y entradas a museos/pucará suelen ir aparte. Si ya estás en la Quebrada, un auto rinde más que volver a Salta.",
                "en": "Classic departure from Salta (they also have an office in San Salvador de Jujuy): Purmamarca, Tilcara, Humahuaca. A long day; lunch and museum/pucará tickets are usually extra. If you are already in the Quebrada, a car beats bouncing back to Salta.",
                "duration_es": "día completo (~12 h desde Salta)",
                "duration_en": "full day (~12 h from Salta)",
                "includes_es": "traslado y guía; comidas y entradas aparte",
                "includes_en": "transfer and guide; meals and tickets extra",
                "ars": 94500,
                "asof": "movitrack.com.ar/excursiones-clasicas, nov. 2026",
                "asof_en": "movitrack.com.ar/excursiones-clasicas, Nov 2026",
                "note_es": "por persona, hoja clásica del operador",
                "note_en": "per person, operator classic sheet",
            },
            {
                "url": "https://movitrack.com.ar/excursiones-clasicas",
                "es_name": "Movitrack — Salinas Grandes",
                "en_name": "Movitrack — Salinas Grandes",
                "es": "Salar vía Purmamarca / Cuesta de Lipán. Altura: abrigo y agua. El Safari a las Nubes (4×4 + Polvorilla + salinas, jornada muy larga) no tiene tarifa en esa misma hoja: confirmalo en Movitrack o en GetYourGuide/Viator, no en un número inventado.",
                "en": "Salt flats via Purmamarca / Cuesta de Lipán. Altitude: jacket and water. Safari a las Nubes (4×4 + Polvorilla + salt flats, a very long day) is not on that same sheet: confirm it with Movitrack or on GetYourGuide/Viator — not an invented fare.",
                "duration_es": "día completo (~13 h desde Salta)",
                "duration_en": "full day (~13 h from Salta)",
                "includes_es": "traslado y guía; comidas y Ojos del Salar aparte",
                "includes_en": "transfer and guide; meals and Ojos del Salar extra",
                "ars": 97500,
                "asof": "movitrack.com.ar/excursiones-clasicas, nov. 2026",
                "asof_en": "movitrack.com.ar/excursiones-clasicas, Nov 2026",
                "note_es": "por persona, hoja clásica del operador",
                "note_en": "per person, operator classic sheet",
            },
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Calilegua (APN)",
                "en_name": "Calilegua National Park (APN)",
                "es": "Selva de yungas, no puna. Entrada oficial; no hace falta un tour para caminar los senderos habilitados.",
                "en": "Yungas jungle, not puna. Official gate fee; you do not need a tour for the open trails.",
                "duration_es": "tu día en el parque",
                "duration_en": "your park day",
                "includes_es": "senderos habilitados; no hay lancha ni 4×4 incluido",
                "includes_en": "open trails; no boat or 4×4 included",
                "ars": APN["calilegua"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general (extranjeros); nacionales ~ARS 12.000",
                "note_en": "general fee (foreign visitors); Argentine residents ~ARS 12,000",
            }
        ],
    },
    {
        "slug": "salta",
        "region": "norte",
        "es": {
            "name": "Salta",
            "where": "NOA · valles calchaquíes",
            "teaser": "«Salta la linda»: centro colonial, cerros cerca y base para Cafayate.",
            "vibe": "«Salta la linda» no es marketing vacío: centro colonial, cerros cerca y buena mesa. Base cómoda para valles calchaquíes y Cafayate.",
            "season": "Ideal abr–jun y sep–nov (seco, días claros). Evitá dic–mar si no querés lluvia de temporada y calor en el valle; Cafayate en verano pega fuerte.",
            "arrive": "Vuelo a SLA (~2 h desde Buenos Aires) o micro (~18–20 h). Auto o tour para Cafayate/Cachi: las distancias engañan.",
            "do": [
                "Centro y Cerro San Bernardo. El monumento a Güemes está al pie del cerro (Av. Uruguay y Paseo Güemes); las escaleras suben atrás. Ficha en la <a href=\"../#proceres\">hub</a>.",
                "Cachi o Cafayate por Ruta 40/68; torrontés en bodegas.",
                "Museo de Arqueología de Alta Montaña si te interesa historia incaica.",
                "Parque Nacional Los Cardones en el camino a Cachi.",
            ],
            "eat": "Empanadas salteñas (jugosas, a menudo al horno), locro, tamales, cabrito. Un clásico del centro es Doña Salta (empanadas y comida regional; suele haber cola). Peña folklórica de noche si te late.",
            "hack": "Combo sólido: Salta + Quebrada + Salinas, 4–5 días. Si seguís a Bolivia: micro Salta→La Quiaca (~7 h, Andesmar/Balut, desde ~ARS 35.000 / ~USD 23, oct. 2026) y el puente a Villazón. Jama a Chile sale de acá de madrugada.",
        },
        "en": {
            "name": "Salta",
            "where": "Northwest · Calchaquí valleys",
            "teaser": "“Salta la linda”: colonial centre, hills close by, and a base for Cafayate.",
            "vibe": "“Salta la linda” is not empty marketing: colonial centre, hills close by, and a serious table. A comfortable base for the Calchaquí valleys and Cafayate.",
            "season": "Ideal Apr–Jun and Sep–Nov (dry, clear days). Avoid Dec–Mar if you don’t want the wet season and valley heat; Cafayate in summer hits hard.",
            "arrive": "Fly to SLA (~2 h from Buenos Aires) or take the bus (~18–20 h). Car or tour for Cafayate/Cachi: distances lie.",
            "do": [
                "The centre and Cerro San Bernardo. The Güemes monument sits at the foot of the hill (Av. Uruguay and Paseo Güemes); the stairs start behind it. Card on the <a href=\"../#proceres\">hub</a>.",
                "Cachi or Cafayate via Ruta 40/68; torrontés at wineries.",
                "High Mountain Archaeology Museum if Inca history pulls you in.",
                "Los Cardones National Park on the way to Cachi.",
            ],
            "eat": "Salta empanadas (juicy, often baked), locro, tamales, goat. A downtown classic is Doña Salta (queues are normal). A folklore peña at night if that’s your thing.",
            "hack": "The solid combo is Salta + Quebrada + salt flats, 4–5 days. Onward to Bolivia: bus Salta→La Quiaca (~7 h, Andesmar/Balut, from ~ARS 35,000 / ~USD 23, Oct 2026) and the bridge into Villazón. The Chile bus via Jama leaves from here before dawn.",
        },
        "legs_es": [("bus", "Micro ~18–20 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~18–20 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["jujuy", "tucuman", "santiago-del-estero", "catamarca"],
        "tours": [
            {
                "url": "https://movitrack.com.ar/excursiones-clasicas",
                "es_name": "Movitrack — Cafayate / Cachi",
                "en_name": "Movitrack — Cafayate / Cachi",
                "es": "Operador salteño de toda la vida para valles. Cafayate (Quebrada de las Conchas + pueblo/bodega) y Cachi salen a la misma tarifa en la hoja clásica. Almuerzo y catas extra. Tren a las Nubes es otro producto (no corre todos los días; el ticket lo vende el tren, no Movitrack).",
                "en": "A long-standing Salta operator for the valleys. Cafayate (Quebrada de las Conchas + town/winery) and Cachi share the same fare on the classic sheet. Lunch and tastings extra. Tren a las Nubes is a different product (not daily; the train sells its own ticket).",
                "duration_es": "día completo (~12 h)",
                "duration_en": "full day (~12 h)",
                "includes_es": "traslado y guía; comidas y bodega/entradas aparte",
                "includes_en": "transfer and guide; meals and winery/tickets extra",
                "ars": 77500,
                "asof": "movitrack.com.ar/excursiones-clasicas, nov. 2026",
                "asof_en": "movitrack.com.ar/excursiones-clasicas, Nov 2026",
                "note_es": "por persona; Cafayate o Cachi",
                "note_en": "per person; Cafayate or Cachi",
            },
            {
                "url": "https://movitrack.com.ar/excursiones-clasicas",
                "es_name": "Movitrack — Humahuaca y Salinas",
                "en_name": "Movitrack — Humahuaca and salt flats",
                "es": "Humahuaca ARS 94.500 y Salinas Grandes ARS 97.500 en la misma hoja. Días de 12–13 h desde Salta. Safari a las Nubes (4×4 + viaducto + salinas) no está tarifado ahí: preguntá al operador o mirá GetYourGuide/Viator.",
                "en": "Humahuaca ARS 94,500 and Salinas Grandes ARS 97,500 on the same sheet. 12–13 h days from Salta. Safari a las Nubes (4×4 + viaduct + salt flats) is not priced there: ask the operator or check GetYourGuide/Viator.",
                "duration_es": "día completo (~12–13 h)",
                "duration_en": "full day (~12–13 h)",
                "includes_es": "traslado y guía; comidas aparte",
                "includes_en": "transfer and guide; meals extra",
                "ars": 94500,
                "ars_high": 97500,
                "asof": "movitrack.com.ar/excursiones-clasicas, nov. 2026",
                "asof_en": "movitrack.com.ar/excursiones-clasicas, Nov 2026",
                "note_es": "Humahuaca–Salinas en la hoja clásica",
                "note_en": "Humahuaca–salt flats on the classic sheet",
            },
            {
                "url": "https://movitrack.com.ar/excursiones-clasicas",
                "es_name": "Movitrack — city tour Salta",
                "en_name": "Movitrack — Salta city tour",
                "es": "Circuito de centro y alrededores si acabás de aterrizar. Tres horas; no reemplaza Cafayate ni la Quebrada.",
                "en": "Centre and outskirts if you just landed. Three hours; it does not replace Cafayate or the Quebrada.",
                "duration_es": "~3 h",
                "duration_en": "~3 h",
                "includes_es": "recorrido urbano guiado",
                "includes_en": "guided city loop",
                "ars": 44500,
                "asof": "movitrack.com.ar/excursiones-clasicas, nov. 2026",
                "asof_en": "movitrack.com.ar/excursiones-clasicas, Nov 2026",
                "note_es": "por persona",
                "note_en": "per person",
            },
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Los Cardones (APN)",
                "en_name": "Los Cardones National Park (APN)",
                "es": "Cardones y ruta a Cachi. Entrada oficial; muchos tours a Cachi la cruzan.",
                "en": "Cardón cactus and the Cachi road. Official gate fee; many Cachi tours pass through.",
                "duration_es": "parada en el día a Cachi",
                "duration_en": "a stop on the Cachi day",
                "includes_es": "ingreso al parque",
                "includes_en": "park admission",
                "ars": APN["cardones"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general",
                "note_en": "general fee",
            },
        ],
    },
    {
        "slug": "tucuman",
        "region": "norte",
        "es": {
            "name": "Tucumán",
            "where": "NOA · la más chica, de las más densas",
            "teaser": "Calor, 1816 y una cultura de sánguche que es religión local.",
            "vibe": "La más chica de las provincias y una de las más densas: calor, historia independentista y una cultura de sánguche que es religión local.",
            "season": "Ideal abr–jun y ago–oct. Evitá dic–feb: calor húmedo y tormentas de tarde. Tafí del Valle es más fresco todo el año.",
            "arrive": "Vuelo a TUC (~2 h) o micro (~14–16 h) desde Buenos Aires. Tafí queda a ~2 h en auto por montaña.",
            "do": [
                "Casa Histórica (la independencia, 1816) y el centro de San Miguel.",
                "Sangucherías de barrio: eso es Tucumán más que un tour.",
            ],
            "eat": "Sánguche de milanesa (el clásico tucumano, en pan sanguchero) y empanadas tucumanas. Eso, antes que cualquier restaurante «de autor». Buscá sangucherías de barrio.",
            "hack": "Fácil de encadenar con Santiago del Estero, Catamarca o Salta.",
        },
        "en": {
            "name": "Tucumán",
            "where": "Northwest · smallest province, one of the densest",
            "teaser": "Heat, 1816, and a sandwich culture that is a local religion.",
            "vibe": "The smallest province and one of the densest: heat, independence history, and a sandwich culture that is a local religion.",
            "season": "Ideal Apr–Jun and Aug–Oct. Avoid Dec–Feb: humid heat and afternoon storms. Tafí del Valle is cooler year-round.",
            "arrive": "Fly to TUC (~2 h) or bus (~14–16 h) from Buenos Aires. Tafí is ~2 h by car into the mountains.",
            "do": [
                "Casa Histórica (independence, 1816) and downtown San Miguel.",
                "Neighbourhood sandwich shops: that is Tucumán more than a tour.",
            ],
            "eat": "Milanesa sandwich (the Tucumán classic, in sanguchero bread) and Tucumán empanadas. That, before any “auteur” restaurant. Look for neighbourhood sandwich shops.",
            "hack": "Easy to chain with Santiago del Estero, Catamarca, or Salta.",
        },
        "legs_es": [("bus", "Micro ~14–16 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~14–16 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["santiago-del-estero", "salta", "jujuy", "catamarca"],
        "tours": [],
        "tips": {
            "es_title": "Para cuando vayas — Tafí del Valle",
            "en_title": "For when you go — Tafí del Valle",
            "es": """<p>Tafí del Valle (~2.000 m) es el clásico de «subir a fresco» desde San Miguel. <strong>Yo no lo marqué como visitado</strong>: es un tip para lectores, no un pin del mapa. ~107–126 km por RN38 y RP307 (Quebrada de los Sosa), ~2 h 30 de micro.</p>
      <p><a href="https://transporteaconquija.com.ar/" rel="noopener">Transporte Aconquija</a> es la empresa del valle. Ficha de Plataforma10 / el propio operador: <strong>ARS 18.000–20.000</strong> / {usd_lo}–{usd_hi} el tramo (jul–nov. 2026). Desde oct. 2026 el provincial se paga con tarjeta/QR, no efectivo. Ruinas de Quilmes y Amaicha quedan más al oeste: otro salto, auto o tour, no un day trip apurado.</p>""".format(usd_lo="~USD 12", usd_hi="13"),
            "en": """<p>Tafí del Valle (~2,000 m) is the classic “go up to cool off” from San Miguel. <strong>I did not mark it as visited</strong>: a reader tip, not a map pin. ~107–126 km via RN38 and RP307 (Quebrada de los Sosa), ~2 h 30 by bus.</p>
      <p><a href="https://transporteaconquija.com.ar/" rel="noopener">Transporte Aconquija</a> is the valley company. Plataforma10 / operator card: <strong>ARS 18,000–20,000</strong> / ~USD 12–13 one-way (Jul–Nov 2026). From Oct 2026 the provincial bus is card/QR, not cash. Quilmes ruins and Amaicha sit further west: another hop, car or tour, not a rushed day trip.</p>""",
        },
    },
    {
        "slug": "catamarca",
        "region": "norte",
        "es": {
            "name": "Catamarca",
            "where": "NOA · valles y alta montaña",
            "teaser": "Entre Tucumán y la puna: calor de valle, oeste de altura y menos brochure que Salta.",
            "vibe": "Estuve. No armé un diario de días, así que esta ficha es corta a propósito: no invento lodges ni anécdotas. San Fernando del Valle es la base calurosa; el oeste (Belén, Tinogasta, Fiambalá) es desierto de altura, seísmiles y vino. Menos circuito internacional que Salta o Jujuy. El postcard del oeste — Campo de Piedra Pómez, lagunas — depende de clima y operación local.",
            "season": "Valle: calor fuerte dic–feb (fácil 35–40 °C). Mejor abr–jun y sep–nov. El oeste es seco, noches frías, altura de verdad: abrigo después de las 18 aunque el valle hierva. Dic–mar hay lluvia en sierras y a veces cortes. Misma lógica NOA: seco = otoño–primavera.",
            "arrive": "Vuelo a CTC (Coronel Felipe Varela, ~2 h desde Buenos Aires) o micro (~16–18 h). Fácil de encadenar con Tucumán. El Paso de San Francisco a Chile existe; no te armo horarios que no chequeé.",
            "do": [
                "Centro de San Fernando del Valle del Catamarca.",
                "Si el plan es montaña o desierto: Belén, Tinogasta, Fiambalá. Son distancias largas: auto o agencia, no un day trip improvisado desde el valle.",
                "Campo de Piedra Pómez y lagunas de altura son el cliché del oeste. Confirmá operación y permisos en el lugar; no hay un operador único que yo nombre con tarifa pública.",
            ],
            "eat": "Empanadas, locro, cabrito, vino de altura del oeste. Mesa de norte, no de brochure mendocino.",
            "hack": "No amarro un operador. Se entiende en combo con Tucumán o Salta, no como un salto de dos noches «porque queda en el mapa».",
        },
        "en": {
            "name": "Catamarca",
            "where": "Northwest · valleys and high Andes",
            "teaser": "Between Tucumán and the puna: hot valley, high-altitude west, less brochure than Salta.",
            "vibe": "I have been. I did not keep a day-by-day diary, so this page stays short on purpose: no invented lodges or anecdotes. San Fernando del Valle is the hot base; the west (Belén, Tinogasta, Fiambalá) is high desert, 6,000 m peaks, and wine. Less of an international circuit than Salta or Jujuy. The western postcard — Campo de Piedra Pómez, high lagoons — depends on weather and local operations.",
            "season": "Valley: hard heat Dec–Feb (easily 35–40 °C). Better Apr–Jun and Sep–Nov. The west is dry, cold nights, real altitude: a jacket after 6 p.m. even if the valley is boiling. Dec–Mar means rain in the hills and occasional closures. Same northwest logic: dry = autumn–spring.",
            "arrive": "Fly to CTC (Coronel Felipe Varela, ~2 h from Buenos Aires) or take the bus (~16–18 h). Easy to chain with Tucumán. Paso de San Francisco into Chile exists; I am not inventing timetables I have not checked.",
            "do": [
                "Downtown San Fernando del Valle de Catamarca.",
                "If the plan is mountain or desert: Belén, Tinogasta, Fiambalá. Long distances: car or agency, not an improvised day trip from the valley.",
                "Campo de Piedra Pómez and high lagoons are the western cliché. Confirm operations and permits on the ground; there is no single operator I can name with a public rate.",
            ],
            "eat": "Empanadas, locro, goat, high-altitude wine from the west. Northern table, not a Mendoza brochure.",
            "hack": "I am not locking an operator. It makes sense as a combo with Tucumán or Salta, not as a two-night hop “because it is on the map.”",
        },
        "legs_es": [("bus", "Micro ~16–18 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~16–18 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["tucuman", "santiago-del-estero", "salta"],
        "tours": [],
    },
    {
        "slug": "santiago-del-estero",
        "region": "norte",
        "es": {
            "name": "Santiago del Estero",
            "where": "NOA · folklore y termas",
            "teaser": "Menos circuito internacional, más chacarera, siesta y Termas de Río Hondo.",
            "vibe": "El folklore tiene casa acá. Menos circuito turístico internacional, más chamamé/chacarera, siestas largas y termas cerca.",
            "season": "Ideal may–sep: el calor afloja y las termas rinden. Evitá dic–feb — es de las provincias más calientes del país (40 °C+ y siesta obligatoria).",
            "arrive": "Vuelo a SDE (~1 h 45) o micro de noche desde Buenos Aires (~12–14 h). Fácil de encadenar con Tucumán.",
            "do": [
                "Centro santiagueño.",
                "Termas de Río Hondo (a un rato).",
                "Si te late la música, preguntá por peñas. No esperes la infraestructura de Salta.",
            ],
            "eat": "Empanadas, cabrito, locro, mazamorra. Comida de olla y de domingo.",
            "hack": "Las termas se resuelven en el destino. Para el resto, más que un tour armado, conviene un local que te oriente: no hay un operador «imprescindible» que yo pueda recomendar con nombre.",
        },
        "en": {
            "name": "Santiago del Estero",
            "where": "Northwest · folklore and hot springs",
            "teaser": "Less of an international circuit; more chacarera, siesta, and Termas de Río Hondo.",
            "vibe": "Folklore has a home here. Less of an international tourist circuit, more chamamé/chacarera, long siestas, and hot springs nearby.",
            "season": "Ideal May–Sep: the heat eases and the hot springs pay off. Avoid Dec–Feb — one of the hottest provinces in the country (40 °C+ and a mandatory siesta).",
            "arrive": "Fly to SDE (~1 h 45) or an overnight bus from Buenos Aires (~12–14 h). Easy to chain with Tucumán.",
            "do": [
                "Downtown Santiago del Estero.",
                "Termas de Río Hondo (a short hop).",
                "If music is the point, ask about peñas. Do not expect Salta’s infrastructure.",
            ],
            "eat": "Empanadas, goat, locro, mazamorra. Pot food and Sunday tables.",
            "hack": "The hot springs you sort out on the ground. For the rest, a local pointing you is more useful than a packaged tour: there is no must-book operator I can name.",
        },
        "legs_es": [("bus", "Micro ~12–14 h · noche"), ("air", "Avión ~1 h 45")],
        "legs_en": [("bus", "Bus ~12–14 h · overnight"), ("air", "Flight ~1 h 45")],
        "nearby": ["tucuman", "cordoba", "salta", "catamarca"],
        "tours": [],
    },
    {
        "slug": "misiones",
        "region": "litoral",
        "es": {
            "name": "Misiones",
            "where": "Litoral · Iguazú y selva",
            "teaser": "Selva, humedad y el ruido blanco de las cataratas. Puerto Iguazú es la base.",
            "vibe": "Selva, humedad y el ruido blanco de las cataratas. Puerto Iguazú es la base; el show es el parque. Repelente, agua, zapatillas que se puedan mojar.",
            "season": "Todo el año (selva siempre húmeda). Ideal abr–jun y ago–oct: menos horno, buen caudal. Evitá no ir «porque es invierno»: el parque abre. Dic–feb es el más caluroso y con más tormentas.",
            "arrive": "Vuelo a IGR (~1 h 45–2 h desde Buenos Aires) suele ganar al micro (~16–20 h, noche). Posadas queda más cerca (~12–15 h de micro). Desde el aeropuerto hay transfer al pueblo y al parque.",
            "do": [
                "Parque Nacional Iguazú: circuitos superior, inferior y Garganta del Diablo (las pasarelas se hacen por cuenta propia).",
                "Cruzar al parque brasileño si tenés tiempo y papeles: es la postal panorámica, no un reemplazo del lado argentino.",
                "Si ya estás en Posadas, Encarnación (Paraguay) está al otro lado del puente: chipá y otra moneda, no reemplaza las cataratas.",
            ],
            "eat": "Influencia litoraleña y brasileña/paraguaya: pescado de río (surubí, dorado cuando hay), mandioca, chipá. El parque es caro para comer: llevá algo.",
            "hack": "Micro Rio Uruguay / Crucero del Norte a «Cataratas Brasil», cada hora desde ~7:30. Pasaporte. Pedile al chofer que pare en migraciones de Brasil. No apretés los dos parques en un día. Ciudad del Este no es este cruce.",
        },
        "en": {
            "name": "Misiones",
            "where": "Litoral · Iguazú and jungle",
            "teaser": "Jungle, humidity, and the white noise of the falls. Puerto Iguazú is the base.",
            "vibe": "Jungle, humidity, and the white noise of the falls. Puerto Iguazú is the base; the park is the show. Bug spray, water, shoes that can get wet.",
            "season": "Year-round (the jungle is always humid). Ideal Apr–Jun and Aug–Oct: less of an oven, solid water volume. Don’t skip it “because it’s winter”: the park is open. Dec–Feb is hottest, with more storms.",
            "arrive": "A flight to IGR (~1 h 45–2 h from Buenos Aires) usually beats the bus (~16–20 h, overnight). Posadas is closer by bus (~12–15 h). Transfers run from the airport to town and the park.",
            "do": [
                "Iguazú National Park: upper and lower circuits plus Garganta del Diablo (the walkways you do on your own).",
                "Cross to the Brazilian park if you have time and papers: it is the panoramic postcard, not a replacement for the Argentine side.",
                "If you are already in Posadas, Encarnación (Paraguay) is across the bridge: chipá and another currency, not a substitute for the falls.",
            ],
            "eat": "Litoral plus Brazilian/Paraguayan influence: river fish (surubí, dorado when available), mandioca, chipá. Food inside the park is expensive: bring something.",
            "hack": "Rio Uruguay / Crucero del Norte bus to “Cataratas Brasil”, about hourly from ~7:30. Passport. Ask the driver to stop at Brazilian immigration. Do not squeeze both parks into one day. Ciudad del Este is a different crossing.",
        },
        "legs_es": [("bus", "Micro ~16–20 h · noche"), ("air", "Avión ~1 h 45–2 h")],
        "legs_en": [("bus", "Bus ~16–20 h · overnight"), ("air", "Flight ~1 h 45–2 h")],
        "nearby": ["entre-rios", "santa-fe"],
        "tours": [
            {
                "url": "https://iguazuargentina.com/planifica-tu-visita/compra-tus-entradas/",
                "es_name": "Entrada Parque Nacional Iguazú (APN)",
                "en_name": "Iguazú National Park ticket (APN)",
                "es": "Incluye tren ecológico y circuitos habilitados ese día. Comprá oficial; el parque no es la lancha. Garganta a veces cierra por caudal: mirá el parte del parque esa mañana.",
                "en": "Includes the ecological train and the circuits open that day. Buy official; the park ticket is not the boat. Garganta sometimes closes with high water: check the park notice that morning.",
                "duration_es": "el día en el parque (abrí temprano)",
                "duration_en": "your park day (go early)",
                "includes_es": "tren ecológico y pasarelas abiertas; lancha aparte",
                "includes_en": "ecological train and open boardwalks; boat extra",
                "ars": APN["iguazu_gen"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; residentes nacionales ARS 25.000",
                "note_en": "general fee; Argentine residents ARS 25,000",
            },
            {
                "url": "https://tickets.iguazujungle.com/",
                "es_name": "Iguazú Jungle — Gran Aventura",
                "en_name": "Iguazú Jungle — Gran Aventura",
                "es": "Sendero Yacaratiá en vehículo abierto + lancha por rápidos hasta la base de los saltos. Te empapás. Edad mínima 12 años, DNI/pasaporte original, restricciones de embarque (embarazo, movilidad, etc.). Parque y traslados aparte. Reservá a la mañana: los cupos se van.",
                "en": "Yacaratiá trail in an open vehicle + a boat up the rapids to the base of the falls. You will get soaked. Minimum age 12, original ID/passport, boarding restrictions (pregnancy, mobility, etc.). Park and transfers extra. Book in the morning: slots go.",
                "duration_es": "~2 h (operador; algunas fichas dicen ~2 h 15)",
                "duration_en": "~2 h (operator; some write-ups say ~2 h 15)",
                "includes_es": "guía bilingüe, vehículo, lancha, bolsa estanca; no capa de lluvia ni entrada al parque",
                "includes_en": "bilingual guide, vehicle, boat, dry bag; no rain poncho or park ticket",
                "ars": 100000,
                "asof": "iguazujungle.com / tickets.iguazujungle.com, nov. 2026",
                "asof_en": "iguazujungle.com / tickets.iguazujungle.com, Nov 2026",
                "note_es": "excursión sola; parque aparte",
                "note_en": "excursion only; park extra",
            },
        ],
    },
    {
        "slug": "entre-rios",
        "region": "litoral",
        "es": {
            "name": "Entre Ríos",
            "where": "Litoral · ríos, termas, carnaval",
            "teaser": "Argentina de fin de semana largo: termas, carnaval y el corredor a Uruguay.",
            "vibe": "Ríos, islas, carnaval y termas. Es Argentina de fin de semana largo más que de postcard internacional.",
            "season": "Termas todo el año. Ideal sep–nov y mar–may para río sin vapor. Carnaval de Gualeguaychú: ene–feb, va con eso. Evitá enero si buscás silencio (y odiás mosquitos).",
            "arrive": "Micro desde Retiro (unas 3–6 h según el destino) o auto por la RN14. Vuelos puntuales a Paraná (PRA) cuando hay.",
            "do": [
                "Termas (Federación, Colón, Villa Elisa).",
                "Carnaval de Gualeguaychú en temporada.",
                "Palacio San José cerca de Concepción del Uruguay.",
                "Parque Nacional El Palmar si estás por Colón (yatay y palmares).",
            ],
            "eat": "Pescado de río, cítricos, salames y quesos de la zona. Menos asado-de-guía, más mesa familiar.",
            "hack": "El micro EGA Buenos Aires→Montevideo pisa este corredor (Gualeguaychú / Fray Bentos). Si ya estás en la provincia, Uruguay queda a un puente, no a un vuelo.",
        },
        "en": {
            "name": "Entre Ríos",
            "where": "Litoral · rivers, hot springs, carnival",
            "teaser": "Long-weekend Argentina: hot springs, carnival, and the corridor to Uruguay.",
            "vibe": "Rivers, islands, carnival, and hot springs. Long-weekend Argentina more than an international postcard.",
            "season": "Hot springs year-round. Ideal Sep–Nov and Mar–May for the river without the steam. Gualeguaychú carnival: Jan–Feb, that’s the point. Avoid January if you want quiet (and hate mosquitoes).",
            "arrive": "Bus from Retiro (~3–6 h depending on the town) or drive RN14. Occasional flights to Paraná (PRA).",
            "do": [
                "Hot springs (Federación, Colón, Villa Elisa).",
                "Gualeguaychú carnival in season.",
                "Palacio San José near Concepción del Uruguay.",
                "El Palmar National Park if you are near Colón (yatay palms).",
            ],
            "eat": "River fish, citrus, local salami and cheese. Less guidebook asado, more family table.",
            "hack": "The EGA Buenos Aires→Montevideo bus uses this corridor (Gualeguaychú / Fray Bentos). If you are already in the province, Uruguay is a bridge, not a flight.",
        },
        "legs_es": [("bus", "Micro ~3–6 h"), ("local", "Según el pueblo")],
        "legs_en": [("bus", "Bus ~3–6 h"), ("local", "Depends on the town")],
        "nearby": ["caba", "santa-fe", "buenos-aires"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional El Palmar (APN)",
                "en_name": "El Palmar National Park (APN)",
                "es": "Palmares de yatay cerca de Colón. Entrada oficial.",
                "en": "Yatay palms near Colón. Official gate fee.",
                "ars": APN["palmar"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general",
                "note_en": "general fee",
            }
        ],
    },
    {
        "slug": "santa-fe",
        "region": "centro",
        "es": {
            "name": "Santa Fe",
            "where": "Litoral / centro · Rosario",
            "teaser": "Rosario: río, banderas, carlito y el salto corto que sí se siente ciudad.",
            "vibe": "Yo marqué Rosario: ciudad de río, banderas y una soberbia simpática. Menos vitrina turística que CABA, más escala humana y costanera. La capital provincial es otra película; esta página es sobre el salto que yo sí hice.",
            "season": "Ideal sep–nov y mar–may, costanera caminable. Evitá dic–feb si no te gusta el calor húmedo de río.",
            "arrive": "Micro desde Retiro (~3–4 h), tren a Rosario Norte cuando corre, o vuelo a ROS (~1 h). Es el salto corto más lógico desde Buenos Aires.",
            "do": [
                "Monumento Nacional a la Bandera (Belgrano; Santa Fe 581). Sala y cripta suelen ser gratis, el mirador se paga — confirmá en <a href=\"https://www.monumentoalabandera.gob.ar/visita\" rel=\"noopener\">monumentoalabandera.gob.ar</a>. La cripta es homenaje; los restos están en Santo Domingo, CABA. Ficha en la <a href=\"../#proceres\">hub</a>.",
                "Costanera e islas frente a la ciudad.",
                "Centros culturales. Si hay clásico de fútbol, el clima cambia.",
            ],
            "eat": "El carlito (sándwich de miga, jamón, queso, manteca y ketchup; patrimonio local — nació en bares tipo Cachito). También pescado de río y helado.",
            "hack": "Rosario es parada lógica hacia el litoral, no un «hub aéreo» para Iguazú: si tu vuelo es BA–IGR, dormir acá «porque queda de paso» no ahorra nada.",
        },
        "en": {
            "name": "Santa Fe",
            "where": "Litoral / centre · Rosario",
            "teaser": "Rosario: river, flags, the carlito sandwich, and the short hop that still feels like a city.",
            "vibe": "I marked Rosario: river city, flags, and a likeable swagger. Less of a tourist vitrine than CABA, more human scale and a waterfront. The provincial capital is a different film; this page is the hop I actually made.",
            "season": "Ideal Sep–Nov and Mar–May, walkable waterfront. Avoid Dec–Feb if you don’t like humid river heat.",
            "arrive": "Bus from Retiro (~3–4 h), the train to Rosario Norte when it runs, or a flight to ROS (~1 h). The most logical short hop from Buenos Aires.",
            "do": [
                "National Flag Memorial (Belgrano; Santa Fe 581). The hall and crypt are usually free, the tower is paid — confirm at <a href=\"https://www.monumentoalabandera.gob.ar/visita\" rel=\"noopener\">monumentoalabandera.gob.ar</a>. The crypt is a tribute; the remains are at Santo Domingo, CABA. Card on the <a href=\"../#proceres\">hub</a>.",
                "The waterfront and islands across the river.",
                "Cultural centres. If there is a football derby, the mood shifts.",
            ],
            "eat": "The carlito (thin-bread sandwich with ham, cheese, butter, and ketchup — local heritage, born in bars like Cachito). Also river fish and ice cream.",
            "hack": "Rosario is a logical stop toward the litoral, not an “air hub” for Iguazú: if your flight is BA–IGR, sleeping here “because it is on the way” saves nothing.",
        },
        "legs_es": [("bus", "Micro ~3–4 h"), ("air", "Avión ~1 h")],
        "legs_en": [("bus", "Bus ~3–4 h"), ("air", "Flight ~1 h")],
        "nearby": ["entre-rios", "cordoba", "caba"],
        "tours": [],
    },
    {
        "slug": "cordoba",
        "region": "centro",
        "es": {
            "name": "Córdoba",
            "where": "Capital universitaria · las sierras quedan a un micro",
            "teaser": "Ciudad viva (universidad, cuarteto, fernet). Las sierras — Punilla, Calamuchita, Traslasierra — son tips de distancia y boleto, no pines aparte.",
            "vibe": "Estuve en la capital. Universidad enorme, cuarteto, fernet con Coca y una ciudad que se mueve de día y de noche. El fin de semana cordobés se va a las sierras: yo no marqué cada pueblo. Esta página parte la ficha — ciudad visitada / valles para cuando vayas — a propósito. No invento anécdotas de hostería.",
            "season": "Dos climas, no uno. <strong>Ciudad:</strong> rinde casi todo el año. Verano (dic–feb) caliente y seco, fácil 32–36 °C y siesta; invierno (jun–ago) seco, ~5–18 °C, sol de tarde. Mejor mar–may y sep–nov. <strong>Sierras:</strong> mismas estaciones, noches más frías. Ideal sep–nov y mar–may. Enero en Carlos Paz es calor + muchedumbre. Cosquín folklore = última semana de enero; Cosquín Rock = febrero (Punilla). Oktoberfest de Villa General Belgrano = octubre. Detalle y boletos en <a href=\"#tips\">sierras</a>.",
            "arrive": "Desde Buenos Aires: vuelo a COR (~1 h 20, hub doméstico fuerte) o micro (~9–11 h, suele noche, cama). Indicativo CABA→Córdoba en la <a href=\"../#red-precios\">red de precios</a>: micro ~ARS 23.000–70.000 / ~USD 15–45; avión «desde» Turismocity 2 nov. 2026 ~ARS 88.000 / ~USD 57. El aeropuerto (Pajas Blancas) queda ~11 km al norte: taxi/remís/Uber al centro ~25–40 min. La Terminal de Ómnibus (T1/T2) es el nudo hacia las sierras — no salís a Punilla a pie desde el centro. Auto tiene sentido si encadenás dos valles; para un día a Carlos Paz o Alta Gracia el micro alcanza. Desde COR también conectás Mendoza y el NOA sin volver a Ezeiza.",
            "do": [
                "Centro histórico y Manzana Jesuítica (UNESCO): iglesia de la Compañía, Universidad Nacional, Colegio Monserrat. Se camina.",
                "Nueva Córdoba (estudiantes, bares) y Güemes (bares, diseño, feria). Parque Sarmiento si querés verde sin salir de la ciudad.",
                "Cuarteto de noche si te late: tunga-tunga, baile de a dos, no dinner-show. Quality Espacio, Plaza de la Música; confirmá cartelera. Rodrigo y La Mona en la <a href=\"../#musica\">hub</a>.",
                "Las sierras no son un barrio: son otro viaje de 40–180 km. Circuitos y micros en <a href=\"#tips\">sierras</a>.",
            ],
            "eat": "En la capital: fernet con Coca (sí, es cultural; el vaso largo es el default), empanadas cordobesas, locro, asado, pizza y comida de estudiante en Nueva Córdoba. No amarro un restaurante que puede cerrar mañana. En las sierras — si vas — cabrito, humita, comida de hostería; Carlos Paz es más parrilla de fin de semana que pueblo de olla.",
            "hack": "Empate clásico CABA–Córdoba: cama nocturno vs vuelo corto. Si el plan es un valle, no duermas en Ezeiza: llegá a Córdoba, terminal, micro. Un día rinde Carlos Paz o Alta Gracia; Punilla norte (La Cumbre / Capilla) pide salir temprano; Calamuchita + Cumbrecita es día largo; Traslasierra no es day trip. Boletos en <a href=\"#tips\">la tabla</a>.",
        },
        "en": {
            "name": "Córdoba",
            "where": "University capital · the sierras are a bus ride",
            "teaser": "A living city (university, cuarteto, fernet). The sierras — Punilla, Calamuchita, Traslasierra — are distance-and-ticket tips, not extra pins.",
            "vibe": "I have been to the capital. A huge university, cuarteto, fernet and Coke, and a city that moves day and night. The Córdoba weekend leaves for the sierras: I did not mark each town. This page splits on purpose — visited city / valleys for when you go. No invented inn anecdotes.",
            "season": "Two climates, not one. <strong>City:</strong> works almost year-round. Summer (Dec–Feb) hot and dry, easily 32–36 °C and a siesta; winter (Jun–Aug) dry, ~5–18 °C, afternoon sun. Better Mar–May and Sep–Nov. <strong>Sierras:</strong> the same seasons, colder nights. Ideal Sep–Nov and Mar–May. January in Carlos Paz is heat + crowds. Cosquín folklore = last week of January; Cosquín Rock = February (Punilla). Villa General Belgrano Oktoberfest = October. Detail and fares in <a href=\"#tips\">sierras</a>.",
            "arrive": "From Buenos Aires: fly to COR (~1 h 20, a real domestic hub) or bus (~9–11 h, often overnight, cama). Indicative BA→Córdoba on the <a href=\"../#red-precios\">fare network</a>: bus ~ARS 23,000–70,000 / ~USD 15–45; flight “from” Turismocity 2 Nov 2026 ~ARS 88,000 / ~USD 57. The airport (Pajas Blancas) sits ~11 km north: taxi/remis/Uber to the centre ~25–40 min. The bus terminal (T1/T2) is the hub for the sierras — you do not walk to Punilla from downtown. A car makes sense if you chain two valleys; for a Carlos Paz or Alta Gracia day the bus is enough. From COR you can also connect Mendoza and the northwest without going back to Ezeiza.",
            "do": [
                "Historic centre and the Jesuit Block (UNESCO): Compañía church, the national university, Colegio Monserrat. Walkable.",
                "Nueva Córdoba (students, bars) and Güemes (bars, design, a fair). Parque Sarmiento if you want green without leaving town.",
                "Cuarteto at night if that’s your thing: tunga-tunga, couple-dancing, not a dinner-show. Quality Espacio, Plaza de la Música; confirm the bill. Rodrigo and La Mona on the <a href=\"../#musica\">hub</a>.",
                "The sierras are not a neighbourhood: they are another 40–180 km trip. Circuits and buses in <a href=\"#tips\">sierras</a>.",
            ],
            "eat": "In the capital: fernet and Coke (yes, it is cultural; the long glass is the default), Córdoba empanadas, locro, asado, pizza and student food in Nueva Córdoba. I am not locking a restaurant that may close tomorrow. In the sierras — if you go — goat, humita, inn food; Carlos Paz is more a weekend grill than a pot-food village.",
            "hack": "Classic CABA–Córdoba tie: overnight cama vs a short flight. If a valley is the plan, do not sleep at Ezeiza: reach Córdoba, terminal, bus. One day covers Carlos Paz or Alta Gracia; northern Punilla (La Cumbre / Capilla) wants an early start; Calamuchita + Cumbrecita is a long day; Traslasierra is not a day trip. Tickets in <a href=\"#tips\">the table</a>.",
        },
        "legs_es": [("bus", "Micro ~9–11 h · suele noche"), ("air", "Avión ~1,5 h")],
        "legs_en": [("bus", "Bus ~9–11 h · often overnight"), ("air", "Flight ~1.5 h")],
        "nearby": ["santa-fe", "mendoza", "santiago-del-estero", "caba"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Quebrada del Condorito (APN)",
                "en_name": "Quebrada del Condorito National Park (APN)",
                "es": "Sierras de verdad, cóndores si el día da. Entrada oficial.",
                "en": "Actual sierras, condors if the day plays along. Official gate fee.",
                "ars": APN["condorito"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "duration_es": "el día en el parque",
                "duration_en": "your park day",
                "includes_es": "ingreso; traslado desde Córdoba aparte",
                "includes_en": "admission; transfer from Córdoba extra",
                "note_es": "tarifa general",
                "note_en": "general fee",
            }
        ],
        "city_extra": {
            "es_title": "Ciudad: comida, cultura, noche",
            "en_title": "The city: food, culture, night",
            "es": """<p>La capital es universitaria: UNC, más de trescientos mil estudiantes en un año normal. Eso explica la densidad de bares, el fernet y por qué Nueva Córdoba a las 23 no parece una ciudad de interior. No es Buenos Aires y no quiere serlo.</p>
      <h3>Barrios que importan</h3>
      <ul class="season-list">
        <li><strong>Centro / Manzana Jesuítica</strong> — El piso colonial y universitario. Se camina de día. A la noche el centro se vacía más que Nueva Córdoba.</li>
        <li><strong>Nueva Córdoba</strong> — Estudiantes, departamentos, bares, after. El pulmón de la noche barata. No es «pintoresco»: es gente.</li>
        <li><strong>Güemes</strong> — Bares, diseño, feria (suele ser fin de semana; confirmá). Un poco más mixto que Nueva Córdoba.</li>
        <li><strong>Cerro de las Rosas / zona norte</strong> — Más residencial, más auto, otra franja de edad. No es el primer barrio si venís dos noches.</li>
      </ul>
      <h3>Noche y oído</h3>
      <p>Fernet Branca con Coca, vaso largo, es el trago de la ciudad — no un gag de turismo. El oído de la noche es <strong>cuarteto</strong>: tunga-tunga, baile de a dos, no un dinner-show. Quality Espacio (Circunvalación) es la sala grande; La Plaza de la Música y boliches de Nueva Córdoba completan. La Mona es el piso; Rodrigo «El Potro» es el que lo hizo nacional; Ulises, Q’Lokura y La Konga llenan ahora. El Festival Nacional del Cuarteto existe desde 2023 — confirmá sede. Ficha larga en el <a href="../#musica">mapa de música</a>. Si no te late, hay rock y electrónico; no son el default. La noche arranca tarde: antes de las 00 mucha puerta está tibia.</p>
      <h3>Cultura de día</h3>
      <p>Manzana Jesuítica (UNESCO). Palacio Ferreyra / Emilio Caraffa si querés museo. Teatro del Libertador si hay función (confirmá cartelera). Parque Sarmiento para un rato de verde. No armo un ranking de restaurantes: el peso se mueve y las puertas cambian. Pedí empanadas y un fernet; el resto es boca a boca del día.</p>""",
            "en": """<p>The capital is a university city: UNC, more than three hundred thousand students in a normal year. That explains the density of bars, the fernet, and why Nueva Córdoba at 11 p.m. does not look like a sleepy inland town. It is not Buenos Aires and does not want to be.</p>
      <h3>Neighbourhoods that matter</h3>
      <ul class="season-list">
        <li><strong>Centre / Jesuit Block</strong> — The colonial and university floor. Walk it by day. At night the centre empties more than Nueva Córdoba.</li>
        <li><strong>Nueva Córdoba</strong> — Students, apartments, bars, afters. The cheap-night lung. Not “picturesque”: it is people.</li>
        <li><strong>Güemes</strong> — Bars, design, a fair (usually weekend; confirm). A little more mixed than Nueva Córdoba.</li>
        <li><strong>Cerro de las Rosas / north</strong> — More residential, more car, another age band. Not the first neighbourhood if you have two nights.</li>
      </ul>
      <h3>Night and ear</h3>
      <p>Fernet Branca and Coke, long glass, is the city’s drink — not a tourism gag. The night’s ear is <strong>cuarteto</strong>: tunga-tunga, couple-dancing, not a dinner-show. Quality Espacio (ring road) is the big room; La Plaza de la Música and Nueva Córdoba clubs fill the rest. La Mona is the floor; Rodrigo “El Potro” is the one who made it national; Ulises, Q’Lokura, and La Konga fill rooms now. The National Cuarteto Festival has existed since 2023 — confirm the venue. Longer card on the hub <a href="../#musica">music map</a>. If it is not your thing, there is rock and electronic; they are not the default. The night starts late: before midnight a lot of doors are still warm.</p>
      <h3>Daytime culture</h3>
      <p>Jesuit Block (UNESCO). Palacio Ferreyra / Emilio Caraffa if you want a museum. Teatro del Libertador if there is a show (confirm the bill). Parque Sarmiento for a stretch of green. I am not ranking restaurants: pesos move and doors change. Ask for empanadas and a fernet; the rest is that day’s word of mouth.</p>""",
        },
        "tips": {
            "toc_es": "Sierras",
            "toc_en": "Sierras",
            "es_flag_h": "La capital es el pin. Los valles no.",
            "en_flag_h": "The capital is the pin. The valleys are not.",
            "es_flag_p": "Yo marqué Córdoba ciudad. Carlos Paz, La Cumbre, Capilla, Alta Gracia y el resto son guía práctica para lectores: no pines del mapa, no un checklist de pueblos que pisé uno por uno.",
            "en_flag_p": "I marked Córdoba city. Carlos Paz, La Cumbre, Capilla, Alta Gracia and the rest are a practical reader guide: not map pins, not a checklist of towns I walked one by one.",
            "es_title": "Sierras desde la capital — distancias, micros, circuitos",
            "en_title": "Sierras from the capital — distances, buses, circuits",
            "es": """<p>La provincia es un abanico de valles al oeste de la capital. <strong>Primero llegás a Córdoba ciudad</strong> (vuelo ~1 h 20 / micro ~9–11 h desde Buenos Aires) y recién ahí el valle. Micros interurbanos salen de la <strong>Terminal de Ómnibus (T1/T2)</strong>. Tarifas: ERSEP oct. 2026 (+14,7%) donde hay nota de prensa; el resto es hoja de terminal ~jun. 2026 o un rango entre dos fichas vecinas. Confirmá en boletería el día que viajás. FX ~ARS 1.550/USD (BNA, nov. 2026). El colectivo urbano de la capital es otra red (tarjeta/QR del día; no mezcles ese boleto con el interurbano).</p>

      <h3>Capital vs sierras, en una frase</h3>
      <ul class="season-list">
        <li><strong>Capital</strong> — Universidad, cuarteto, fernet, Manzana Jesuítica. Visité esto.</li>
        <li><strong>Punilla</strong> (oeste, RN38 / lago San Roque) — Carlos Paz, Cosquín, La Falda, La Cumbre, Capilla del Monte. El valle más cerca y más masivo.</li>
        <li><strong>Paravachasca</strong> (sudoeste) — Alta Gracia. Día jesuita corto.</li>
        <li><strong>Calamuchita</strong> (sur) — Villa General Belgrano, La Cumbrecita. Día largo o noche.</li>
        <li><strong>Traslasierra</strong> (más al oeste, Camino de las Altas Cumbres) — Mina Clavero, Nono, Villa Dolores. Finde, no day trip.</li>
        <li><strong>Quebrada del Condorito</strong> — Parque nacional en las sierras grandes. Auto o excursión; no un colectivo de esquina. Entrada APN tarifa general ARS 25.000 / ~USD 16 (desde 1 jun 2026).</li>
      </ul>

      <h3>Pueblos y boletos (ida, desde la Terminal de Córdoba)</h3>
      <div class="table-wrap">
        <table class="prices">
          <thead><tr><th>Valle / pueblo</th><th>Para qué</th><th>Desde Córdoba</th><th>Micro ida (estimativo)</th></tr></thead>
          <tbody>
            <tr><td><strong>Punilla · Villa Carlos Paz</strong></td><td>Lago San Roque, fin de semana masivo, casino, no «naturaleza virgen».</td><td>~36–40 km · 45–60 min</td><td class="num">ARS 6.500 / ~USD 4 <span class="mute">ERSEP 1 oct. 2026</span></td></tr>
            <tr><td><strong>Punilla · Cosquín</strong></td><td>Festival de folklore (última semana de ene); pueblo de ruta el resto del año.</td><td>~55–63 km · ~1 h 15</td><td class="num">ARS 10.000 / ~USD 6 <span class="mute">ERSEP oct. 2026</span></td></tr>
            <tr><td><strong>Punilla · La Falda</strong></td><td>Entre Cosquín y La Cumbre; sierras más «veraneo clásico».</td><td>~80 km · ~1 h 30–1 h 45</td><td class="num">~ARS 13.000–18.000 / ~USD 8–12 <span class="mute">entre Cosquín y Capilla; confirmá boletería</span></td></tr>
            <tr><td><strong>Punilla · La Cumbre</strong></td><td>Más quieto que Carlos Paz; golf, aire de veraneo inglés viejo, base para el norte del valle.</td><td>~90–100 km · ~1 h 45–2 h</td><td class="num">~ARS 15.000–20.000 / ~USD 10–13 <span class="mute">sin ficha ERSEP propia acá; confirmá</span></td></tr>
            <tr><td><strong>Punilla · Capilla del Monte</strong></td><td>Cerro Uritorco, más seco, fama ovni / alternativa. El más lejos del valle corto.</td><td>~108–110 km · ~2 h</td><td class="num">ARS 21.000 / ~USD 14 <span class="mute">ERSEP oct. 2026</span></td></tr>
            <tr><td><strong>Paravachasca · Alta Gracia</strong></td><td>Estancia jesuita UNESCO, museo del Che, día corto.</td><td>~36 km · ~40 min</td><td class="num">~ARS 5.700 / ~USD 4 <span class="mute">terminal jun. 2026; confirmá</span></td></tr>
            <tr><td><strong>Calamuchita · Villa General Belgrano</strong></td><td>Oktoberfest (oct), base para La Cumbrecita.</td><td>~90 km · ~1 h 45</td><td class="num">~ARS 18.000–20.000 / ~USD 12–13 <span class="mute">~17.700 jun. 2026 + aumento oct.</span></td></tr>
            <tr><td><strong>Calamuchita · La Cumbrecita</strong></td><td>Pueblo peatonal «alemán»; transbordo en VGB (Pájaro Blanco u otro local).</td><td>~120 km · 2–3 h con transbordo</td><td class="num">VGB + tramo local; confirmá Pájaro Blanco</td></tr>
            <tr><td><strong>Traslasierra · Mina Clavero / Nono</strong></td><td>Otro valle, por Altas Cumbres. Río, fin de semana.</td><td>~150 km · ~3 h</td><td class="num">~ARS 36.000 / ~USD 23 <span class="mute">jun./oct. 2026</span></td></tr>
            <tr><td><strong>Traslasierra · Villa Dolores</strong></td><td>Punta más lejos del mismo corredor.</td><td>~180 km · ~3 h+</td><td class="num">ARS 47.300 / ~USD 31 <span class="mute">jun./oct. 2026</span></td></tr>
          </tbody>
        </table>
      </div>
      <p class="wx">Ida. La vuelta suele costar parecido. Enero y fines largos llenan el coche a Carlos Paz: comprá con tiempo. Empresas: varias salen de la misma terminal — compará en boletería / Plataforma10; no me caso con un logo.</p>

      <h3>Circuitos cortos desde la capital (sugeridos, no un itinerario que yo corrí pueblo por pueblo)</h3>
      <ul class="season-list">
        <li><strong>Medio día · Carlos Paz</strong> — El más fácil. Lago, costanera, vuelta a dormir a la capital. No lo vendas como «naturaleza»: es el balneario de la ciudad. ~ARS 6.500 / ~USD 4 el tramo.</li>
        <li><strong>Día corto · Alta Gracia</strong> — Estancia jesuita + (si te late) casa de Che. ~40 min. Cierra más temprano que un boliche: salí de mañana. ~ARS 5.700 / ~USD 4.</li>
        <li><strong>Día Punilla medio · Cosquín + La Falda o La Cumbre</strong> — Un solo valle, misma ruta. En enero Cosquín es el festival (última semana); el resto del año es pueblo de paso. Salí temprano si llegás a La Cumbre. Boletos en la tabla: Cosquín ARS 10.000; La Cumbre rango, confirmá.</li>
        <li><strong>Día Punilla largo · Capilla del Monte / Uritorco</strong> — ~2 h. Más seco, más rareza. No apretés Carlos Paz + Uritorco «porque queda en el mapa»: son 70 km más de valle y otra energía. ARS 21.000 / ~USD 14 el tramo.</li>
        <li><strong>Día largo · Calamuchita (VGB + Cumbrecita)</strong> — Salida temprana. VGB es la base; Cumbrecita es peatonal y pide transbordo. En octubre (Oktoberfest) dormí allá o aceptá el micro de vuelta lleno. ~ARS 18.000–20.000 a VGB + local.</li>
        <li><strong>Día con auto o tour · Quebrada del Condorito</strong> — Cóndores si el día da. No hay un micro de esquina que te deje en el mirador. APN ARS 25.000 / ~USD 16 + traslado. Confirmá operación.</li>
        <li><strong>Finde, no día · Traslasierra</strong> — Altas Cumbres (~3 h). Mina Clavero / Nono. Volver el mismo día es masoquismo de ruta. ~ARS 36.000 / ~USD 23 a Mina Clavero.</li>
      </ul>
      <p>No mezcles Punilla norte y Calamuchita el mismo día «para aprovechar». Son valles distintos, terminal de ida distinta en espíritu, y el sol se acaba. Mejor época para cualquiera de estos circuitos: sep–nov y mar–may. Enero funciona si aceptás gente y calor; julio es seco y frío de noche en altura.</p>""",
            "en": """<p>The province is a fan of valleys west of the capital. <strong>You reach Córdoba city first</strong> (flight ~1 h 20 / bus ~9–11 h from Buenos Aires) and only then the valley. Intercity buses leave from the <strong>bus terminal (T1/T2)</strong>. Fares: ERSEP Oct 2026 (+14.7%) where the press listed them; the rest is a ~Jun 2026 terminal sheet or a range between two neighbouring cards. Confirm at the window the day you travel. FX ~ARS 1,550/USD (BNA, Nov 2026). The capital’s city bus is a different network (that day’s card/QR; do not mix it with the intercity ticket).</p>

      <h3>Capital vs sierras, in one line</h3>
      <ul class="season-list">
        <li><strong>Capital</strong> — University, cuarteto, fernet, Jesuit Block. I visited this.</li>
        <li><strong>Punilla</strong> (west, RN38 / Lake San Roque) — Carlos Paz, Cosquín, La Falda, La Cumbre, Capilla del Monte. The closest and most massive valley.</li>
        <li><strong>Paravachasca</strong> (southwest) — Alta Gracia. A short Jesuit day.</li>
        <li><strong>Calamuchita</strong> (south) — Villa General Belgrano, La Cumbrecita. A long day or a night.</li>
        <li><strong>Traslasierra</strong> (further west, Camino de las Altas Cumbres) — Mina Clavero, Nono, Villa Dolores. A weekend, not a day trip.</li>
        <li><strong>Quebrada del Condorito</strong> — National park in the big sierras. Car or tour; not a corner bus. APN general fee ARS 25,000 / ~USD 16 (from 1 Jun 2026).</li>
      </ul>

      <h3>Towns and tickets (one-way, from Córdoba terminal)</h3>
      <div class="table-wrap">
        <table class="prices">
          <thead><tr><th>Valley / town</th><th>What it’s for</th><th>From Córdoba</th><th>Bus one-way (indicative)</th></tr></thead>
          <tbody>
            <tr><td><strong>Punilla · Villa Carlos Paz</strong></td><td>Lake San Roque, mass weekend, casino, not “untouched nature”.</td><td>~36–40 km · 45–60 min</td><td class="num">ARS 6,500 / ~USD 4 <span class="mute">ERSEP 1 Oct 2026</span></td></tr>
            <tr><td><strong>Punilla · Cosquín</strong></td><td>Folklore festival (last week of Jan); a road town the rest of the year.</td><td>~55–63 km · ~1 h 15</td><td class="num">ARS 10,000 / ~USD 6 <span class="mute">ERSEP Oct 2026</span></td></tr>
            <tr><td><strong>Punilla · La Falda</strong></td><td>Between Cosquín and La Cumbre; more “classic summering” sierras.</td><td>~80 km · ~1 h 30–1 h 45</td><td class="num">~ARS 13,000–18,000 / ~USD 8–12 <span class="mute">between Cosquín and Capilla; confirm at the window</span></td></tr>
            <tr><td><strong>Punilla · La Cumbre</strong></td><td>Quieter than Carlos Paz; golf, an old English-summering air, a base for the north of the valley.</td><td>~90–100 km · ~1 h 45–2 h</td><td class="num">~ARS 15,000–20,000 / ~USD 10–13 <span class="mute">no dedicated ERSEP card here; confirm</span></td></tr>
            <tr><td><strong>Punilla · Capilla del Monte</strong></td><td>Cerro Uritorco, drier, UFO / alternative fame. The far end of the short valley.</td><td>~108–110 km · ~2 h</td><td class="num">ARS 21,000 / ~USD 14 <span class="mute">ERSEP Oct 2026</span></td></tr>
            <tr><td><strong>Paravachasca · Alta Gracia</strong></td><td>UNESCO Jesuit estancia, Che museum, a short day.</td><td>~36 km · ~40 min</td><td class="num">~ARS 5,700 / ~USD 4 <span class="mute">terminal Jun 2026; confirm</span></td></tr>
            <tr><td><strong>Calamuchita · Villa General Belgrano</strong></td><td>Oktoberfest (Oct), base for La Cumbrecita.</td><td>~90 km · ~1 h 45</td><td class="num">~ARS 18,000–20,000 / ~USD 12–13 <span class="mute">~17,700 Jun 2026 + Oct hike</span></td></tr>
            <tr><td><strong>Calamuchita · La Cumbrecita</strong></td><td>Car-free “German” village; change in VGB (Pájaro Blanco or another local).</td><td>~120 km · 2–3 h with a transfer</td><td class="num">VGB + local hop; confirm Pájaro Blanco</td></tr>
            <tr><td><strong>Traslasierra · Mina Clavero / Nono</strong></td><td>Another valley, via Altas Cumbres. River, weekend.</td><td>~150 km · ~3 h</td><td class="num">~ARS 36,000 / ~USD 23 <span class="mute">Jun/Oct 2026</span></td></tr>
            <tr><td><strong>Traslasierra · Villa Dolores</strong></td><td>Further along the same corridor.</td><td>~180 km · ~3 h+</td><td class="num">ARS 47,300 / ~USD 31 <span class="mute">Jun/Oct 2026</span></td></tr>
          </tbody>
        </table>
      </div>
      <p class="wx">One-way. The return is usually similar. January and long weekends fill the Carlos Paz coach: buy ahead. Companies: several leave the same terminal — compare at the window / Plataforma10; I am not marrying a logo.</p>

      <h3>Short circuits from the capital (suggested, not an itinerary I walked town by town)</h3>
      <ul class="season-list">
        <li><strong>Half day · Carlos Paz</strong> — The easy one. Lake, waterfront, back to sleep in the capital. Do not sell it as “nature”: it is the city’s resort. ~ARS 6,500 / ~USD 4 the hop.</li>
        <li><strong>Short day · Alta Gracia</strong> — Jesuit estancia + (if you want) Che’s house. ~40 min. It shuts earlier than a club: leave in the morning. ~ARS 5,700 / ~USD 4.</li>
        <li><strong>Medium Punilla day · Cosquín + La Falda or La Cumbre</strong> — One valley, one road. In January Cosquín is the festival (last week); the rest of the year it is a pass-through town. Leave early if you reach La Cumbre. Tickets in the table: Cosquín ARS 10,000; La Cumbre a range, confirm.</li>
        <li><strong>Long Punilla day · Capilla del Monte / Uritorco</strong> — ~2 h. Drier, weirder. Do not squeeze Carlos Paz + Uritorco “because they are on the map”: that is 70 km more of valley and another energy. ARS 21,000 / ~USD 14 the hop.</li>
        <li><strong>Long day · Calamuchita (VGB + Cumbrecita)</strong> — Early start. VGB is the base; Cumbrecita is car-free and wants a transfer. In October (Oktoberfest) sleep there or accept a full bus back. ~ARS 18,000–20,000 to VGB + local.</li>
        <li><strong>Day with a car or tour · Quebrada del Condorito</strong> — Condors if the day plays along. There is no corner bus that drops you at the lookout. APN ARS 25,000 / ~USD 16 + transfer. Confirm operations.</li>
        <li><strong>Weekend, not a day · Traslasierra</strong> — Altas Cumbres (~3 h). Mina Clavero / Nono. Coming back the same day is road masochism. ~ARS 36,000 / ~USD 23 to Mina Clavero.</li>
      </ul>
      <p>Do not mix northern Punilla and Calamuchita the same day “to make the most of it.” They are different valleys, a different outgoing mood at the terminal, and the sun runs out. Best window for any of these circuits: Sep–Nov and Mar–May. January works if you accept people and heat; July is dry and cold at night up high.</p>""",
        },
    },
    {
        "slug": "caba",
        "region": "amba",
        "es": {
            "name": "CABA",
            "where": "Ciudad Autónoma de Buenos Aires",
            "teaser": "Cafés, protestas, tango y una energía que cansa y enamora. No es «Argentina»: es una capa.",
            "vibe": "La capital es enorme y contradictoria: cafés, protestas, tango, malbec y una energía que cansa y enamora. No es «Argentina»: es una capa.",
            "season": "Ideal sep–nov y mar–may. Evitá dic–feb si no bancás calor húmedo y tormentas; jun–ago es fresco y gris, no extremo.",
            "arrive": "EZE (internacional) o AEP (doméstico y algunos regionales). AEP 20–40 min al centro; EZE 45–75 min. Tienda León / Uber. Dentro: SUBE, subte, colectivo, DiDi/Cabify/Uber.",
            "do": [
                "Palermo (parques, bares), San Telmo (feria domingo), Recoleta (cementerio: Sarmiento está ahí; ficha en la <a href=\"../#proceres\">hub</a>).",
                "Plaza de Mayo y la Catedral Metropolitana: el mausoleo de San Martín está adentro (nave derecha). El walking tour suele pasar; no hace falta un ticket aparte. Fichas de próceres en la <a href=\"../#proceres\">hub</a>.",
                "Puerto Madero para la foto, La Boca un rato corto con las cosas pegadas al cuerpo.",
                "Free walking tours en Plaza de Mayo/San Telmo (propina). Tango en milonga de verdad si te anima, no sólo dinner-show.",
            ],
            "eat": "Parrilla (Don Julio en Palermo, con reserva), bodegón (El Preferido de Palermo), pizza al molde en Güerrín, café histórico en Café Tortoni y Los 36 Billares, choripán en ferias (La Choripanería en Mercado de San Telmo). Helado de dulce de leche en cualquier heladería seria.",
            "hack": "Tigre ~50 min en tren Mitre desde Retiro (~ARS 790 con SUBE registrada, oct. 2026). La Plata ~1 h 16 desde Constitución. San Antonio de Areco ~2 h. Tandil no es day trip. Montevideo: hay micro EGA de noche, no sólo Buquebus — ver hacks en la hub.",
        },
        "en": {
            "name": "CABA",
            "where": "City of Buenos Aires",
            "teaser": "Cafés, protests, tango, and an energy that exhausts and charms. It is not “Argentina”: it is a layer.",
            "vibe": "The capital is huge and contradictory: cafés, protests, tango, malbec, and an energy that exhausts and charms. It is not “Argentina”: it is a layer.",
            "season": "Ideal Sep–Nov and Mar–May. Avoid Dec–Feb if you don’t like humid heat and storms; Jun–Aug is cool and grey, not extreme.",
            "arrive": "EZE (international) or AEP (domestic and some regional). AEP 20–40 min to the centre; EZE 45–75 min. Tienda León / Uber. Inside the city: SUBE, subway, buses, DiDi/Cabify/Uber.",
            "do": [
                "Palermo (parks, bars), San Telmo (Sunday fair), Recoleta (cemetery: Sarmiento is there; card on the <a href=\"../#proceres\">hub</a>).",
                "Plaza de Mayo and the Metropolitan Cathedral: San Martín’s tomb is inside (right aisle). The walking tour usually passes; no separate ticket. Short historical cards on the <a href=\"../#proceres\">hub</a>.",
                "Puerto Madero for the photo, La Boca briefly with your things zipped.",
                "Free walking tours at Plaza de Mayo/San Telmo (tip). Tango in a real milonga if you are up for it, not only a dinner show.",
            ],
            "eat": "Parrilla (Don Julio in Palermo, book ahead), bodegón (El Preferido de Palermo), thick-crust pizza at Güerrín, historic cafés Tortoni and Los 36 Billares, choripán at fairs (La Choripanería in Mercado de San Telmo). Dulce de leche ice cream at any serious heladería.",
            "hack": "Tigre ~50 min on the Mitre train from Retiro (~ARS 790 with a registered SUBE, Oct 2026). La Plata ~1 h 16 from Constitución. San Antonio de Areco ~2 h. Tandil is not a day trip. Montevideo: there is an overnight EGA bus, not only Buquebus — see the hub hacks.",
        },
        "legs_es": [("local", "Estás acá"), ("air", "AEP 20–40 min · EZE 45–75 min")],
        "legs_en": [("local", "You are here"), ("air", "AEP 20–40 min · EZE 45–75 min")],
        "nearby": ["buenos-aires", "entre-rios", "santa-fe"],
        "tours": [
            {
                "url": "https://www.guruwalk.com/buenos-aires",
                "es_name": "Free walking tour (propina)",
                "en_name": "Free walking tour (tip-based)",
                "es": "Varias empresas salen de Plaza de Mayo o San Telmo, 2–3 h, inglés y español. No hay tarifa: se propina al final. No amarro una como «la» mejor: mirá reseñas recientes en GuruWalk, GetYourGuide o Viator.",
                "en": "Several companies leave from Plaza de Mayo or San Telmo, 2–3 h, English and Spanish. No fare: you tip at the end. I am not locking one as “the” walk: read recent reviews on GuruWalk, GetYourGuide, or Viator.",
                "duration_es": "2–3 h",
                "duration_en": "2–3 h",
                "includes_es": "guía a pie por el centro; propina al final, no un boleto",
                "includes_en": "a walking guide through the centre; a tip at the end, not a ticket",
                "price_es": "propina típica ~USD 10–20 (algunas notas locales hablan de ARS 2.000–5.000: es propina, no tarifa)",
                "price_en": "typical tip ~USD 10–20 (some local notes say ARS 2,000–5,000: that is a tip, not a fare)",
                "asof": "modelo tip-based, nov. 2026",
                "asof_en": "tip-based model, Nov 2026",
                "note_es": "no hay hoja de operador único",
                "note_en": "no single operator sheet",
            },
            {
                "url": "https://turismo.buenosaires.gob.ar/",
                "es_name": "Milonga (clase + pista)",
                "en_name": "Milonga (class + floor)",
                "es": "Tango de verdad: se baila, no se mira desde una mesa con show. Cubiertos y códigos de pista cambian por salón. Glorieta de Belgrano es al aire libre y sin ticket. Dinner-show (Viejo Almacén, Señor Tango y compañía) es teatro para visitantes: otra plata, otro plan.",
                "en": "Real tango: you dance, you don’t watch from a dinner table. Covers and floor codes change by hall. Glorieta de Belgrano is outdoors and unticketed. A dinner show (Viejo Almacén, Señor Tango and the rest) is visitor theatre: different money, different plan.",
                "duration_es": "clase 1–2 h; milonga hasta tarde",
                "duration_en": "class 1–2 h; milonga runs late",
                "includes_es": "entrada al salón; copa y zapato a veces extra",
                "includes_en": "door cover; drink and shoes sometimes extra",
                "ars": 3000,
                "ars_high": 8000,
                "asof": "rango de puerta 2026, no un salón único",
                "asof_en": "door range 2026, not one hall",
                "note_es": "cubierto; clase principiante suele ARS 4.000–10.000",
                "note_en": "cover; beginner class often ARS 4,000–10,000",
            },
            {
                "url": "https://www.getyourguide.com/buenos-aires-l145/tango-tc186/",
                "es_name": "Dinner-show de tango (si insistís)",
                "en_name": "Tango dinner show (if you insist)",
                "es": "No elijo «el» mejor show: cambian elenco, menú y precio. Pack cena + espectáculo ~USD 80–150 según sala. Compará GetYourGuide/Viator esa semana; si querés tango y no teatro, andá a una milonga.",
                "en": "I am not picking “the” show: cast, menu, and price move. Dinner + show packs ~USD 80–150 depending on the room. Compare GetYourGuide/Viator that week; if you want tango not theatre, go to a milonga.",
                "duration_es": "~3 h (cena + show)",
                "duration_en": "~3 h (dinner + show)",
                "includes_es": "suele incluir cena y espectáculo; copas extra varían",
                "includes_en": "usually dinner and the show; extra drinks vary",
                "usd_only": "aprox. USD 80–150",
                "usd_only_en": "about USD 80–150",
                "asof": "rango de mercado, nov. 2026",
                "asof_en": "market range, Nov 2026",
                "note_es": "confirmá en GetYourGuide/Viator, no en esta guía",
                "note_en": "confirm on GetYourGuide/Viator, not here",
            },
        ],
    },
    {
        "slug": "buenos-aires",
        "region": "amba",
        "es": {
            "name": "Buenos Aires",
            "where": "Provincia · interior, Tigre, costa",
            "teaser": "No es sólo la costa: Tandil, Tigre, La Plata. Mar del Plata tiene su propia lógica de verano.",
            "vibe": "La provincia no es sólo la costa: pueblos, campo, Tandil, sierras chicas y una escala más argentina de almacén. Mar del Plata es el balneario masivo de los argentinos: en verano un quilombo hermoso; fuera de temporada, puerto y viento.",
            "season": "Tigre casi todo el año; Tandil y sierras mejor oct–nov y mar–abr. Mar del Plata: ideal nov o mar. Evitá enero en la costa (el argentino promedio va entonces; la RN2 se llena). Invierno en MdP: puerto y viento, muchos hoteles abajo.",
            "arrive": "Tren, micro o auto desde CABA. MdP: micro desde Retiro (~5–6 h, Tony Tur / Plusmar), tren desde Constitución cuando hay, o vuelo a MDQ (~1 h). En enero el micro se llena: reservá.",
            "do": [
                "Tigre: Puerto de Frutos y lancha al Delta (volvé a cenar).",
                "La Plata: arquitectura y el Museo de Ciencias Naturales.",
                "Tandil o Sierra de la Ventana para aire; estancias de fin de semana.",
                "Mar del Plata: rambla y playas (Playa Grande, Bristol), puerto y lobos marinos, Barrio Los Troncos.",
            ],
            "eat": "Queso y salame de Tandil, facturas de pueblo, asado de campo. En MdP: mariscos y milanesa a la napolitana con papas en porción geológica; churros en la rambla; el puerto para pescado más simple.",
            "hack": "Tandil no entra en el día (~5 h de micro). Un city tour pago a Tigre sobra si el tren sale cada rato. El conurbano es otra película: andá con local.",
        },
        "en": {
            "name": "Buenos Aires Province",
            "where": "Province · hinterland, Tigre, coast",
            "teaser": "Not only the coast: Tandil, Tigre, La Plata. Mar del Plata has its own summer logic.",
            "vibe": "The province is not only the coast: towns, farmland, Tandil, small sierras, and a more Argentine corner-store scale. Mar del Plata is the mass beach resort Argentines actually use: in summer a beautiful mess; off season, harbour and wind.",
            "season": "Tigre almost year-round; Tandil and the small sierras better Oct–Nov and Mar–Apr. Mar del Plata: ideal Nov or Mar. Avoid January on the coast (the average Argentine goes then; RN2 fills up). Winter in MdP: harbour and wind, many hotels shuttered.",
            "arrive": "Train, bus, or car from CABA. MdP: bus from Retiro (~5–6 h, Tony Tur / Plusmar), train from Constitución when it runs, or a flight to MDQ (~1 h). In January the bus fills: book.",
            "do": [
                "Tigre: Puerto de Frutos and a boat into the Delta (back for dinner).",
                "La Plata: architecture and the natural-science museum.",
                "Tandil or Sierra de la Ventana for air; weekend estancias.",
                "Mar del Plata: rambla and beaches (Playa Grande, Bristol), the port and sea lions, Barrio Los Troncos.",
            ],
            "eat": "Tandil cheese and salami, town bakeries, countryside asado. In MdP: seafood and a geological portion of milanesa napolitana; churros on the rambla; the port for simpler fish.",
            "hack": "Tandil is not a day trip (~5 h by bus). A paid city tour to Tigre is surplus if the train leaves every few minutes. Greater Buenos Aires is a different film: go with a local.",
        },
        "legs_es": [("bus", "1–6 h desde CABA"), ("local", "Tren / micro / auto")],
        "legs_en": [("bus", "1–6 h from CABA"), ("local", "Train / bus / car")],
        "nearby": ["caba", "entre-rios"],
        "tours": [],
        "anchor_note_es": "Mar del Plata es la costa de esta provincia; lo dejo acá y no como provincia inventada.",
        "anchor_note_en": "Mar del Plata is this province’s coast; it lives here, not as a fake extra province.",
        "extra_id": "mar-del-plata",
    },
    {
        "slug": "mendoza",
        "region": "cuyo",
        "es": {
            "name": "Mendoza",
            "where": "Cuyo · vino y cordillera",
            "teaser": "Malbec, alta montaña y el cruce a Santiago cuando el paso abre.",
            "vibe": "Vino y montaña. La ciudad es chata y arbolada; el telón es la cordillera. Si te gusta el malbec, es parada obligatoria.",
            "season": "Ideal oct–nov y mar–abr (bodegas; vendimia alrededor de marzo). Evitá dic–feb si no bancás 35–40 °C. Invierno = ski en Las Leñas/Penitentes: otra logística, no el plan vino.",
            "arrive": "Vuelo a MDZ (~1 h 50) o micro (~14–16 h). Auto o bici en Maipú; para Valle de Uco conviene tour o conductor: el vino no maneja.",
            "do": [
                "Bodegas en Luján de Cuyo, Maipú o Valle de Uco.",
                "Cerro de la Gloria, en el Parque San Martín: el monumento al Ejército de los Andes. Subida en auto o a pie; es el San Martín de esta ciudad, no sólo bodega. Ficha en la <a href=\"../#proceres\">hub</a>.",
                "Uspallata y alta montaña; Aconcagua desde el parque (mirar, no hace falta subir).",
                "Cruce a Santiago por Cristo Redentor cuando el paso está abierto.",
            ],
            "eat": "Asado, empanadas mendocinas, chivo, aceitunas. Brindá con malbec, torrontés si venís del norte, o un blanco de altura en Uco.",
            "hack": "Micros Andesmar / CATA / El Rápido: Mendoza → Terminal Sur de Santiago, ~7–8 h, desde ~ARS 45.000–70.000 (~USD 30–45, prensa nov. 2026). Avión MDZ–SCL (~1 h, JetSMART/SKY/LATAM) cuando el paso cierra. En 2026 el Cristo Redentor acumuló ~90 días cerrado. No es un tour de compras del día.",
        },
        "en": {
            "name": "Mendoza",
            "where": "Cuyo · wine and the Andes",
            "teaser": "Malbec, high mountains, and the Santiago crossing when the pass is open.",
            "vibe": "Wine and mountains. The city is flat and tree-lined; the Andes are the backdrop. If you like malbec, it is a required stop.",
            "season": "Ideal Oct–Nov and Mar–Apr (wineries; harvest festival around March). Avoid Dec–Feb if you don’t like 35–40 °C. Winter = skiing at Las Leñas/Penitentes: different logistics, not the wine plan.",
            "arrive": "Fly to MDZ (~1 h 50) or bus (~14–16 h). Car or bike in Maipú; for Valle de Uco you want a tour or a driver: the wine does not drive.",
            "do": [
                "Wineries in Luján de Cuyo, Maipú, or Valle de Uco.",
                "Cerro de la Gloria, in Parque San Martín: the Army of the Andes monument. Drive or walk up; this city’s San Martín, not only wine. Card on the <a href=\"../#proceres\">hub</a>.",
                "Uspallata and the high Andes; Aconcagua from the park (look, you do not have to climb).",
                "The Santiago crossing via Cristo Redentor when the pass is open.",
            ],
            "eat": "Asado, Mendoza empanadas, goat, olives. Toast with malbec, torrontés if you came from the north, or a high-altitude white in Uco.",
            "hack": "Andesmar / CATA / El Rápido buses: Mendoza → Santiago Terminal Sur, ~7–8 h, from ~ARS 45,000–70,000 (~USD 30–45, press Nov 2026). MDZ–SCL flight (~1 h, JetSMART/SKY/LATAM) when the pass shuts. In 2026 Cristo Redentor was closed ~90 days. Not a same-day shopping tour.",
        },
        "legs_es": [("bus", "Micro ~14–16 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~14–16 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["cordoba", "caba"],
        "tours": [
            {
                "url": "https://troutandwine.com/tours/lujan-de-cuyo-wine/",
                "es_name": "Trout & Wine — Luján de Cuyo / Valle de Uco",
                "en_name": "Trout & Wine — Luján de Cuyo / Uco Valley",
                "es": "Operador conocido, grupos chicos, guía en inglés. Luján desde USD 220; Uco desde USD 230 (hoja del operador). Recogida ~8:30–9:00, vuelta a la tarde. Si querés pagar en pesos, contactalos antes. Deluxe privado es otra tarifa (USD 360/370, ocupación doble). En Maipú, bici + remís de vuelta sigue siendo el clásico económico — no le pongo un número de alquiler que no vi en una hoja.",
                "en": "A known operator, small groups, English guide. Luján from USD 220; Uco from USD 230 (operator sheet). Pickup ~8:30–9:00, back in the afternoon. To pay in pesos, contact them first. Private deluxe is a different fare (USD 360/370, double occupancy). In Maipú, bike + a remise back is still the cheap classic — I am not inventing a rental number I have not seen on a sheet.",
                "duration_es": "~8 h (día completo)",
                "duration_en": "~8 h (full day)",
                "includes_es": "pickup en hotel, guía en inglés, catas, almuerzo gourmet, agua; propina aparte",
                "includes_en": "hotel pickup, English guide, tastings, gourmet lunch, water; gratuities extra",
                "usd_only": "desde USD 220 (Luján) / 230 (Uco) · ~ARS 341.000 / 356.500 al FX de esta guía",
                "usd_only_en": "from USD 220 (Luján) / 230 (Uco) · ~ARS 341,000 / 356,500 at this guide’s FX",
                "asof": "troutandwine.com, nov. 2026",
                "asof_en": "troutandwine.com, Nov 2026",
                "note_es": "publicado en USD; ARS a consultar",
                "note_en": "listed in USD; ask if you want ARS",
            }
        ],
    },
    {
        "slug": "chubut",
        "region": "patagonia",
        "es": {
            "name": "Chubut",
            "where": "Patagonia atlántica · Puerto Madryn",
            "teaser": "Mar frío, viento y fauna. Madryn es la base; Península Valdés es el motivo.",
            "vibe": "Mar frío, viento y fauna. La ciudad es una base; Península Valdés es el motivo. Puerto Pirámides queda a ~95 km.",
            "season": "Ballena franca jun–dic (temporada 2026 desde el 9 de jun.; pico sep–oct). Pingüinos más bien sep–mar. El Doradillo, costa, jun–oct. Evitá armar un safari en feb–may pensando en ballenas: no están.",
            "arrive": "Vuelo a REL (Trelew, ~2 h) + transfer (~1 h) o micro de noche desde Buenos Aires (~18–20 h). Auto ayuda para la península.",
            "do": [
                "Avistaje de ballena franca desde Puerto Pirámides (el puerto cierra con viento).",
                "Pingüinos en temporada, elefantes marinos.",
                "Gaiman si querés té galés.",
            ],
            "eat": "Cordero, merluza, centolla cuando hay, torta galesa en Gaiman. El marisco es más fresco que sofisticado.",
            "hack": "Auto (lo más sano) o micro Mar y Valle a Pirámides. No apretés toda la península en media mañana sin auto: la fauna está lejos.",
        },
        "en": {
            "name": "Chubut",
            "where": "Atlantic Patagonia · Puerto Madryn",
            "teaser": "Cold sea, wind, and wildlife. Madryn is the base; Península Valdés is the reason.",
            "vibe": "Cold sea, wind, and wildlife. The town is a base; Península Valdés is the reason. Puerto Pirámides is ~95 km away.",
            "season": "Southern right whales Jun–Dec (2026 season from 9 Jun; peak Sep–Oct). Penguins more like Sep–Mar. El Doradillo, from the coast, Jun–Oct. Don’t plan a Feb–May safari expecting whales: they aren’t there.",
            "arrive": "Fly to REL (Trelew, ~2 h) + transfer (~1 h) or an overnight bus from Buenos Aires (~18–20 h). A car helps on the peninsula.",
            "do": [
                "Southern right whale watching from Puerto Pirámides (the port closes in wind).",
                "Penguins in season, elephant seals.",
                "Gaiman if you want Welsh tea.",
            ],
            "eat": "Lamb, hake, king crab when it is around, Welsh cake in Gaiman. The seafood is fresher than fancy.",
            "hack": "A car (the sane option) or the Mar y Valle bus to Pirámides. Do not squeeze the whole peninsula into a morning without a car: the animals are far apart.",
        },
        "legs_es": [("bus", "Micro ~18–20 h · noche"), ("air", "Avión ~2 h + 1 h transfer")],
        "legs_en": [("bus", "Bus ~18–20 h · overnight"), ("air", "Flight ~2 h + 1 h transfer")],
        "nearby": ["rio-negro", "santa-cruz"],
        "tours": [
            {
                "url": "https://www.hydrosport.ar/eng/tarifas",
                "es_name": "Hydro Sport — avistaje de ballenas",
                "en_name": "Hydro Sport — whale watching",
                "es": "Lancha desde Puerto Pirámides (no desde Madryn). Temporada jun–dic; el puerto cierra con viento. Hay otras lanchas en el muelle (Southern Spirit, Tito Bottazzi y más) y la prensa 2026 habla de tarifas unificadas: compará, no persigas a los animales. Traslado Madryn–Pirámides aparte.",
                "en": "Boat from Puerto Pirámides (not from Madryn). Season Jun–Dec; the port closes in wind. Other boats at the pier (Southern Spirit, Tito Bottazzi and more) and 2026 press talks about unified fares: compare, and do not chase the animals. Madryn–Pirámides transfer extra.",
                "duration_es": "1 h 30 de navegación",
                "duration_en": "1 h 30 on the water",
                "includes_es": "embarque en Pirámides; no incluye traslado ni entrada a Valdés",
                "includes_en": "boarding at Pirámides; transfer and Valdés ticket extra",
                "ars": 150000,
                "ars_high": 195000,
                "asof": "hydrosport.ar/eng/tarifas + prensa unificada sep. 2026",
                "asof_en": "hydrosport.ar/eng/tarifas + unified press Sep 2026",
                "note_es": "baja 15/6–31/8 ARS 150.000 · alta desde 1/9 ARS 195.000 (adultos)",
                "note_en": "low 15 Jun–31 Aug ARS 150,000 · high from 1 Sep ARS 195,000 (adults)",
            },
            {
                "url": "https://www.argentina.gob.ar/turismo",
                "es_name": "Entrada Península Valdés (área protegida)",
                "en_name": "Península Valdés protected-area ticket",
                "es": "Entrada 2026 al área protegida. No incluye lancha ni el micro a Pirámides. El Doradillo (ballenas desde la costa) es otro plan, más barato, cuando hay marea y temporada.",
                "en": "2026 protected-area ticket. Does not include the boat or the bus to Pirámides. El Doradillo (whales from the shore) is a different, cheaper plan when tide and season line up.",
                "duration_es": "el día en la península",
                "duration_en": "your peninsula day",
                "includes_es": "ingreso al área protegida",
                "includes_en": "protected-area admission",
                "ars": 50000,
                "asof": "temporada 2026",
                "asof_en": "2026 season",
                "note_es": "extranjeros; residentes ~ARS 20.000",
                "note_en": "foreign visitors; residents ~ARS 20,000",
            },
        ],
        "tips": {
            "es_title": "Para cuando vayas — Trevelin (el otro Chubut)",
            "en_title": "For when you go — Trevelin (the other Chubut)",
            "es": """<p>Yo marqué <strong>Puerto Madryn</strong> (Atlántico). Trevelin es el oeste: pueblo galés a ~25 km de Esquel, cordillera, no ballenas. <strong>No es un pin visitado.</strong> Desde Bariloche son ~280–320 km por RN40 (~4–5 h). Gaiman (té galés cerca de Trelew) sí queda del lado de Madryn; no lo confundás con Trevelin. Micro Bariloche–Esquel: confirmá en Plataforma10 / Vía Bariloche esa semana — no publico un carrito que no vi.</p>""",
            "en": """<p>I marked <strong>Puerto Madryn</strong> (Atlantic). Trevelin is the west: a Welsh town ~25 km from Esquel, Andes, not whales. <strong>Not a visited pin.</strong> From Bariloche it is ~280–320 km on RN40 (~4–5 h). Gaiman (Welsh tea near Trelew) is on the Madryn side; don’t mix it up with Trevelin. Bariloche–Esquel bus: confirm on Plataforma10 / Vía Bariloche that week — I am not publishing a cart I have not seen.</p>""",
        },
    },
    {
        "slug": "rio-negro",
        "region": "patagonia",
        "es": {
            "name": "Río Negro",
            "where": "Patagonia de lagos · Bariloche",
            "teaser": "Lagos, bosque, chocolate y egresados en temporada. Villa La Angostura ya sería Neuquén: yo no la marqué.",
            "vibe": "Lagos, bosque, chocolate y una ciudad que en temporada alta se llena de egresados. El paisaje perdona el resto. Yo marqué Bariloche en Río Negro; Villa La Angostura ya sería Neuquén.",
            "season": "Lagos/trekking dic–mar (mejor ene–mar; nov–dic hay egresados). Ski jun–sep. Evitá esperar ambos en el mismo viaje. Otoño (abr–may) es más quieto y más lluvia.",
            "arrive": "Vuelo a BRC (~2 h, muchas frecuencias) o micro de ~20–24 h. Auto para circuitos; en invierno, cadenas y paciencia.",
            "do": [
                "Circuito Chico, Cerro Catedral (trekking o ski).",
                "Navegación en Nahuel Huapi.",
                "Ruta de los Siete Lagos hacia Villa La Angostura si tenés auto (Neuquén: yo no la marqué).",
            ],
            "eat": "Chocolate (Rapa Nui en Mitre y Villegas es un clásico de vidriera), trucha, cordero, cerveza artesanal. El té chocolateado después de un cerro es parte del ritual.",
            "hack": "Dos productos distintos hacia Chile: el micro por Paso Cardenal Samoré a Osorno / Puerto Montt (~6–8 h, ~USD 25–45) es traslado. El Cruce Andino es el paseo de tres lagos (~12 h).",
        },
        "en": {
            "name": "Río Negro",
            "where": "Lake Patagonia · Bariloche",
            "teaser": "Lakes, forest, chocolate, and graduating-class crowds in season. Villa La Angostura would be Neuquén: I did not mark it.",
            "vibe": "Lakes, forest, chocolate, and a town that fills with graduating-class trips in high season. The landscape forgives the rest. I marked Bariloche in Río Negro; Villa La Angostura would already be Neuquén.",
            "season": "Lakes/trekking Dec–Mar (best Jan–Mar; Nov–Dec is school-leavers). Ski Jun–Sep. Don’t expect both in one trip. Autumn (Apr–May) is quieter and wetter.",
            "arrive": "Fly to BRC (~2 h, many frequencies) or a ~20–24 h bus. A car for the loops; in winter, chains and patience.",
            "do": [
                "Circuito Chico, Cerro Catedral (trekking or skiing).",
                "A boat on Nahuel Huapi.",
                "Seven Lakes road toward Villa La Angostura if you have a car (Neuquén: I did not mark it).",
            ],
            "eat": "Chocolate (Rapa Nui at Mitre and Villegas is a shop-window classic), trout, lamb, craft beer. Chocolate tea after a hill is part of the ritual.",
            "hack": "Two different Chile products: the bus via Paso Cardenal Samoré to Osorno / Puerto Montt (~6–8 h, ~USD 25–45) is transport. Cruce Andino is the three-lake outing (~12 h).",
        },
        "legs_es": [("bus", "Micro ~20–24 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~20–24 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["chubut", "santa-cruz"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Nahuel Huapi (APN)",
                "en_name": "Nahuel Huapi National Park (APN)",
                "es": "El parque alrededor de Bariloche. Entrada oficial; Circuito Chico se hace en auto, bici o bus turístico. La lancha y Catedral van aparte.",
                "en": "The park around Bariloche. Official gate fee; Circuito Chico is car, bike, or tourist bus. The boat and Catedral are extra.",
                "duration_es": "el día en el parque",
                "duration_en": "your park day",
                "includes_es": "ingreso; no incluye lancha ni aerosilla",
                "includes_en": "admission; boat and chairlift extra",
                "ars": APN["nahuel"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; nacionales ~ARS 15.000",
                "note_en": "general fee; Argentine residents ~ARS 15,000",
            },
            {
                "url": "https://www.turisur.com.ar/?c=inicio&lang=es&v=tarifas",
                "es_name": "Turisur — Circuito Chico",
                "en_name": "Turisur — Circuito Chico",
                "es": "Bus turístico clásico (Campanario, Llao Llao, Bahía López). También se hace en auto o bici más barato. Tangol lista el mismo producto más caro (ARS 50.000 ES / 116.666 con guía en inglés): compará. Aerosilla de Campanario aparte.",
                "en": "Classic tourist bus (Campanario, Llao Llao, Bahía López). Cheaper by car or bike. Tangol lists the same product higher (ARS 50,000 Spanish / 116,666 with an English guide): compare. Campanario chairlift extra.",
                "duration_es": "~4,5 h (8:30–13:00 en la hoja Turisur 2026)",
                "duration_en": "~4.5 h (8:30–13:00 on the Turisur 2026 sheet)",
                "includes_es": "bus y guía; parque y Campanario aparte",
                "includes_en": "bus and guide; park and Campanario extra",
                "ars": 40500,
                "asof": "turisur.com.ar tarifas terrestres 2026",
                "asof_en": "turisur.com.ar land fares 2026",
                "note_es": "adulto; infante 0–3 sin cargo",
                "note_en": "adult; infant 0–3 free",
            },
            {
                "url": "https://islavictoriayarrayanes.com/horarios-y-tarifas/",
                "es_name": "Cau Cau / Turisur — Isla Victoria y Arrayanes",
                "en_name": "Cau Cau / Turisur — Isla Victoria and Arrayanes",
                "es": "Navegación en Nahuel Huapi desde Puerto Pañuelo. Parque APN y tasa de embarque (ARS 7.600) se pagan en el puerto. Traslado terrestre opcional ARS 22.000. Resellers (Tangol) cotizan el paquete más caro: la hoja del barco es esta.",
                "en": "Nahuel Huapi boat from Puerto Pañuelo. APN park fee and boarding tax (ARS 7,600) are paid at the port. Optional land transfer ARS 22,000. Resellers (Tangol) quote a fatter package: the boat sheet is this one.",
                "duration_es": "tarde ~12:15–18:30, o día completo con traslado 10:20–18:30",
                "duration_en": "afternoon ~12:15–18:30, or full day with transfer 10:20–18:30",
                "includes_es": "catamarán, Arrayanes ~45 min, Isla Victoria ~2 h 30; parque y tasa aparte",
                "includes_en": "catamaran, Arrayanes ~45 min, Isla Victoria ~2 h 30; park and tax extra",
                "ars": 140000,
                "asof": "islavictoriayarrayanes.com / Turisur, desde 1 jun 2026",
                "asof_en": "islavictoriayarrayanes.com / Turisur, from 1 Jun 2026",
                "note_es": "adulto; menores/jubilados ARS 70.000",
                "note_en": "adult; children/Argentine seniors ARS 70,000",
            },
            {
                "url": "https://catedralaltapatagonia.com/tarifas/",
                "es_name": "Cerro Catedral — Día Peatón",
                "en_name": "Cerro Catedral — pedestrian day",
                "es": "Ascenso y descenso peatón (Tour Catedral / Telecabina Amancay según operación del día). No es un tour guiado: es el medio de elevación. Pase esquiador es otra tarifa (prensa 2026 ~ARS 160.000). ChipCard aparte. El clima manda qué está abierto.",
                "en": "Pedestrian up and down (Tour Catedral / Telecabina Amancay depending on the day’s operation). Not a guided tour: it is the lift. The skier pass is a different fare (2026 press ~ARS 160,000). ChipCard extra. Weather decides what is open.",
                "duration_es": "el día de medios (suele 9–16)",
                "duration_en": "the lift day (often 9–16)",
                "includes_es": "un ascenso y descenso peatón; ski y estacionamiento aparte",
                "includes_en": "one pedestrian up and down; ski and parking extra",
                "ars": 90000,
                "asof": "catedralaltapatagonia.com/tarifas, 2026",
                "asof_en": "catedralaltapatagonia.com/tarifas, 2026",
                "note_es": "tarifa única; infantes 0–5 sin cargo",
                "note_en": "flat fare; infants 0–5 free",
            },
            {
                "url": "https://www.cruceandino.com/",
                "es_name": "Cruce Andino (tres lagos)",
                "en_name": "Cruce Andino (three lakes)",
                "es": "Nahuel Huapi, Frías, Todos los Santos hacia Peulla/Puerto Varas. No es el micro por Samoré. Parques y almuerzo aparte. Sale casi todos los días; el lago manda.",
                "en": "Nahuel Huapi, Frías, Todos los Santos toward Peulla/Puerto Varas. It is not the Samoré bus. Parks and lunch extra. It runs most days; the lake decides.",
                "duration_es": "~12 h",
                "duration_en": "~12 h",
                "includes_es": "buses + barcos del cruce; parques, almuerzo y tasas aparte",
                "includes_en": "crossing buses + boats; parks, lunch, and taxes extra",
                "usd_only": "USD 355 no residente / 277 residente · ~ARS 550.000 / 429.000 al FX de esta guía",
                "usd_only_en": "USD 355 non-resident / 277 resident · ~ARS 550,000 / 429,000 at this guide’s FX",
                "asof": "cruceandino.com tarifa 2026–28",
                "asof_en": "cruceandino.com 2026–28 fare",
                "note_es": "publicado por el operador en USD",
                "note_en": "published by the operator in USD",
            },
            {
                "url": "https://www.turisur.com.ar/?c=inicio&lang=es&v=tarifas",
                "es_name": "Turisur — Cerro Tronador",
                "en_name": "Turisur — Cerro Tronador",
                "es": "Día largo al volcán/glaciar del lado argentino. Parque Nahuel Huapi aparte. Hoja terrestre 2026 del mismo operador que Circuito Chico.",
                "en": "A long day to the volcano/glacier on the Argentine side. Nahuel Huapi park extra. Same 2026 land sheet as Circuito Chico.",
                "duration_es": "~9 h (9:00–18:00 en la hoja)",
                "duration_en": "~9 h (9:00–18:00 on the sheet)",
                "includes_es": "bus y guía; parque aparte",
                "includes_en": "bus and guide; park extra",
                "ars": 81000,
                "asof": "turisur.com.ar tarifas terrestres 2026",
                "asof_en": "turisur.com.ar land fares 2026",
                "note_es": "adulto 4+; infante 0–3 sin cargo",
                "note_en": "adult 4+; infant 0–3 free",
            },
        ],
        "tips": {
            "es_title": "Para cuando vayas — Trevelin / Esquel",
            "en_title": "For when you go — Trevelin / Esquel",
            "es": """<p>Si el plan es seguir al oeste de los lagos: Esquel y Trevelin (Chubut andino, té galés de cordillera). ~4–5 h desde Bariloche. <strong>Yo no los marqué como visitados</strong> — Villa La Angostura tampoco (eso ya sería Neuquén). Confirmá micros en Plataforma10; no invento tarifa de esa semana.</p>""",
            "en": """<p>If the plan is to keep west of the lakes: Esquel and Trevelin (Andean Chubut, mountain Welsh tea). ~4–5 h from Bariloche. <strong>I did not mark them as visited</strong> — nor Villa La Angostura (that would already be Neuquén). Confirm buses on Plataforma10; I am not inventing that week’s fare.</p>""",
        },
    },
    {
        "slug": "santa-cruz",
        "region": "patagonia",
        "es": {
            "name": "Santa Cruz",
            "where": "Patagonia de hielo · El Calafate",
            "teaser": "Pueblo-base para el Perito Moreno. Kayak o hielo, no los dos el mismo día. El Chaltén es otro viaje (yo no lo marqué).",
            "vibe": "Pueblo-base para el Perito Moreno. El glaciar es el motivo; el pueblo es viento, souvenir y cordero. Estuve en El Calafate. El kayak frente a la pared lo armé con Patagonia Chic — agregador/operador local, ficha pública. El trekking largo es Chaltén: yo no lo marqué.",
            "season": "El Perito Moreno «funciona» casi todo el año: las pasarelas no dependen de un crampón. Ideal nov–mar para luz (y para kayak o hielo). May–ago: frío, ~7–8 h de luz, algunas salidas se cortan por viento. Enero es caro y lleno. Febrero sigue alta: hay paquetes de verano que suman traslado de aeropuerto. Mar–abr afloja un poco y todavía hay día. Pueblo y operadores en <a href=\"#ciudad\">Calafate</a>.",
            "arrive": "Vuelo a FTE (~3 h desde Buenos Aires). No hay micro directo razonable desde BA: si no volás, es odisea de combinaciones. El aeropuerto (Comandante Armando Tola) queda ~20 km al este, ~20 min. Taxi/remís o transfer de hotel. Si reservás una excursión con <a href=\"https://www.patagoniachic.com/el-calafate/excursiones/perito-moreno-kayak\" rel=\"noopener\">Patagonia Chic</a>, la ficha pública de nov. 2026 regala el tramo de <em>llegada</em> FTE→hotel — no el regreso. El glaciar está al otro lado: ~80 km al oeste.",
            "do": [
                "Pasarelas del glaciar (imprescindible) + entrada APN. Micro Caltur / Taqsa / Always Glaciers desde la terminal: ~ARS 56.000–60.000 el tramo (Plataforma10, 3 nov. 2026); parque aparte.",
                "Un segundo plan, no tres el mismo día: kayak (<a href=\"#tours\">Patagonia Chic</a>), minitrekking/safari (Hielo y Aventura) o sólo pasarelas.",
                "El Chaltén queda a ~2 h 40 / 215 km si seguís — <a href=\"#tips\">tip, no pin</a>.",
            ],
            "eat": "Cordero patagónico, calafate en dulce o helado, trucha. Porciones de refugio, no de degustación. Libertador es la calle: parrilla y menú de glaciar. No amarro un restaurante que puede cerrar mañana.",
            "hack": "Si el plan es hielo + sendero: dos noches Calafate (pasarelas o kayak) y después micro a Chaltén (Cal Tur / Chaltén Travel / TAQSA, ~ARS 70.000 / ~USD 45 el tramo, oct. 2026 + tasa). Chaltén no tiene aeropuerto. No es day trip de trekking.",
        },
        "en": {
            "name": "Santa Cruz",
            "where": "Ice Patagonia · El Calafate",
            "teaser": "Base town for Perito Moreno. Kayak or ice, not both the same day. El Chaltén is another trip (I did not mark it).",
            "vibe": "Base town for Perito Moreno. The glacier is the reason; the town is wind, souvenirs, and lamb. I was in El Calafate. The kayak in front of the wall I booked with Patagonia Chic — a local aggregator/operator, public card. The long trekking is El Chaltén: I did not mark it.",
            "season": "Perito Moreno “works” most of the year: the boardwalks do not need crampons. Ideal Nov–Mar for daylight (and for kayak or ice). May–Aug: cold, ~7–8 h of light, some outings get cut by wind. January is expensive and packed. February is still high: summer packages often add an airport transfer. Mar–Apr eases a bit and you still have daylight. Town and operators in <a href=\"#ciudad\">Calafate</a>.",
            "arrive": "Fly to FTE (~3 h from Buenos Aires). There is no reasonable direct bus from BA: if you don’t fly, it is a multi-day odyssey. The airport (Comandante Armando Tola) sits ~20 km east, ~20 min. Taxi/remis or a hotel transfer. If you book an outing with <a href=\"https://www.patagoniachic.com/el-calafate/excursiones/perito-moreno-kayak\" rel=\"noopener\">Patagonia Chic</a>, the Nov 2026 public card gives the <em>arrival</em> FTE→hotel leg — not the return. The glacier is the other way: ~80 km west.",
            "do": [
                "Glacier boardwalks (non-negotiable) plus the APN ticket. Caltur / Taqsa / Always Glaciers buses from the terminal: ~ARS 56,000–60,000 one way (Plataforma10, 3 Nov 2026); park extra.",
                "One second plan, not three the same day: kayak (<a href=\"#tours\">Patagonia Chic</a>), mini trekking/safari (Hielo y Aventura), or boardwalks only.",
                "El Chaltén is ~2 h 40 / 215 km if you continue — <a href=\"#tips\">a tip, not a pin</a>.",
            ],
            "eat": "Patagonian lamb, calafate in jam or ice cream, trout. Mountain-refuge portions, not a tasting menu. Libertador is the street: grill and glacier-menu. I am not locking a restaurant that may close tomorrow.",
            "hack": "If the plan is ice + trail: two nights in Calafate (boardwalks or kayak) and then the bus to Chaltén (Cal Tur / Chaltén Travel / TAQSA, ~ARS 70,000 / ~USD 45 one way, Oct 2026 plus tax). Chaltén has no airport. Not a trekking day trip.",
        },
        "legs_es": [("air", "Avión ~3 h"), ("warn", "Micro: no (2+ días)")],
        "legs_en": [("air", "Flight ~3 h"), ("warn", "Bus: no (2+ days)")],
        "nearby": ["tierra-del-fuego", "chubut", "rio-negro"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Los Glaciares (APN)",
                "en_name": "Los Glaciares National Park (APN)",
                "es": "Entrada al área del Perito Moreno. Las pasarelas se hacen por tu cuenta. Llevá abrigo aunque sea enero.",
                "en": "Ticket for the Perito Moreno area. The boardwalks you do on your own. Bring a jacket even in January.",
                "duration_es": "el día en las pasarelas",
                "duration_en": "your boardwalk day",
                "includes_es": "ingreso al área; lancha y hielo aparte",
                "includes_en": "area admission; boat and ice extra",
                "ars": APN["glaciares"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; nacionales ARS 25.000",
                "note_en": "general fee; Argentine residents ARS 25,000",
            },
            {
                "url": "https://hieloyaventura.com/tarifas/",
                "es_name": "Hielo y Aventura — Minitrekking",
                "en_name": "Hielo y Aventura — Mini trekking",
                "es": "Concesionaria del parque. Crampones sobre el glaciar; apto 8–65 años. Big Ice (más exigente, 15 sep–30 abr) ARS 550.000 + traslado opcional ARS 80.000. Parque y comida aparte.",
                "en": "Park concessionaire. Crampons on the ice; ages 8–65. Big Ice (harder, 15 Sep–30 Apr) ARS 550,000 + optional transfer ARS 80,000. Park and food extra.",
                "duration_es": "~4 h 30 desde el puerto; ~10 h con traslado desde Calafate + pasarelas",
                "duration_en": "~4 h 30 from the port; ~10 h with transfer from Calafate + boardwalks",
                "includes_es": "navegación, guías ES/EN, equipo técnico; parque, comida y traslado opcionales",
                "includes_en": "boat, ES/EN guides, technical kit; park, food, and transfer optional",
                "ars": 420000,
                "asof": "hieloyaventura.com desde 1 nov 2026",
                "asof_en": "hieloyaventura.com from 1 Nov 2026",
                "note_es": "adulto sin traslado (con traslado ARS 500.000)",
                "note_en": "adult without transfer (ARS 500,000 with transfer)",
            },
            {
                "url": "https://hieloyaventura.com/tarifas/",
                "es_name": "Hielo y Aventura — Safari Náutico",
                "en_name": "Hielo y Aventura — Nautical safari",
                "es": "La lancha corta frente a la pared, todo el año. Si no estás para crampones, es el plan. Parque aparte. Safari Azul es otro producto (ARS 140.000, temporada acotada).",
                "en": "The short boat along the wall, year-round. If crampons are not the day, this is the plan. Park extra. Safari Azul is a different product (ARS 140,000, limited season).",
                "duration_es": "navegación corta (el día en el parque es aparte)",
                "duration_en": "short navigation (the park day is separate)",
                "includes_es": "embarque frente al glaciar; parque aparte",
                "includes_en": "boarding in front of the glacier; park extra",
                "ars": 80000,
                "asof": "hieloyaventura.com desde 1 nov 2026",
                "asof_en": "hieloyaventura.com from 1 Nov 2026",
                "note_es": "adulto; 20% jubilados/residentes Santa Cruz/menores 4–15",
                "note_en": "adult; 20% off for Argentine seniors / Santa Cruz residents / ages 4–15",
            },
            {
                "url": "https://www.patagoniachic.com/el-calafate/excursiones/perito-moreno-kayak",
                "es_name": "Patagonia Chic — Kayak Perito Moreno",
                "en_name": "Patagonia Chic — Perito Moreno kayak",
                "rec_es": "Lo reservé — ficha pública, sin códigos",
                "rec_en": "I booked this — public card, no codes",
                "es": "Agregador/operador de Calafate. Kayak doble en el Canal de los Témpanos, la pared de frente. 14 años o más; no hace falta experiencia. Lo armé como kayak de temporada alta (paquete de verano / febrero, con opción de traslado de aeropuerto). Si el plan es crampón sobre hielo, compará con Hielo y Aventura: son días distintos. La <a href=\"https://www.patagoniachic.com/politica-de-cancelacion\" rel=\"noopener\">política pública</a> y la ficha del kayak dicen cancelación gratis hasta 24 h antes; confirmala en el checkout, no en un mail. No publico vouchers ni IDs.",
                "en": "Calafate aggregator/operator. Double kayak on the Canal de los Témpanos, the wall in front of you. Age 14+; no experience required. I booked it as a high-season kayak (a summer / February package, with an airport-transfer option). If the plan is crampons on ice, compare with Hielo y Aventura: those are different days. The <a href=\"https://www.patagoniachic.com/politica-de-cancelacion\" rel=\"noopener\">public policy</a> and the kayak card say free cancel until 24 h before; confirm it at checkout, not in an email. I am not publishing vouchers or IDs.",
                "duration_es": "~1 h 30 de kayak (9:45–13:30 desde el parque); con traslado y pasarelas el día se va a las ~17:30",
                "duration_en": "~1 h 30 of kayaking (9:45–13:30 from the park); with transfer and boardwalks the day runs to ~17:30",
                "includes_es": "kayak, traje seco, guía, snack; la ficha de nov. 2026 dice ticket APN incluido — confirmá al pagar. Traslado hotel + pasarelas ARS 90.000 extra. Llegada FTE→hotel: la ficha lo ofrece gratis al reservar una excursión (no el regreso)",
                "includes_en": "kayak, dry suit, guide, snack; the Nov 2026 card says the APN ticket is included — confirm at payment. Hotel transfer + boardwalks ARS 90,000 extra. FTE→hotel arrival: the card offers it free when you book an outing (not the return)",
                "ars": 370000,
                "ars_high": 510000,
                "asof": "patagoniachic.com ficha + política de cancelación, nov. 2026",
                "asof_en": "patagoniachic.com card + cancellation policy, Nov 2026",
                "note_es": "adulto 14+ desde el parque; 370.000 era promo en pantalla (27% off) vs lista 510.000 — no es un precio eterno",
                "note_en": "adult 14+ starting at the park; 370,000 was an on-screen promo (27% off) vs 510,000 list — not a forever fare",
            },
        ],
        "city_extra": {
            "toc_es": "Calafate",
            "toc_en": "Calafate",
            "es_title": "El Calafate: pueblo, glaciar, cómo elegir el día",
            "en_title": "El Calafate: town, glacier, how to pick the day",
            "es": """<p>Calafate es un pueblo-base, no un destino de vereda. Libertador concentra parrilla, souvenir y agencia. El motivo está a ~80 km: el Perito Moreno. Un día rinde pasarelas; un segundo día rinde <em>o</em> kayak <em>o</em> hielo, no los dos.</p>
      <h3>Cómo ir al glaciar</h3>
      <ul class="season-list">
        <li><strong>Micro</strong> — Caltur, Taqsa, Always Glaciers desde la terminal. Plataforma10 el 3 nov. 2026: ~ARS 56.000–60.000 / ~USD 36–39 el tramo, ~1 h 15–1 h 30. Ida y vuelta el mismo día; confirmá el último regreso antes de perderte en las pasarelas. Parque APN aparte (ARS 50.000 / ~USD 32 general, desde 1 jun 2026).</li>
        <li><strong>Excursión con traslado</strong> — Hielo y Aventura cobra el minitrekking sin traslado ARS 420.000 y con traslado ARS 500.000 (desde 1 nov 2026). Patagonia Chic suma hotel + pasarelas a ARS 90.000 sobre el kayak.</li>
        <li><strong>Auto</strong> — Tiene sentido si encadenás un segundo punto; para un solo día al glaciar el micro alcanza.</li>
      </ul>
      <h3>Kayak vs hielo vs sólo pasarelas</h3>
      <ul class="season-list">
        <li><strong>Pasarelas</strong> — El plan que no falla. Caminás, mirás la pared, volvés. Abrigo aunque sea enero.</li>
        <li><strong>Patagonia Chic — kayak</strong> — La que usé. Agregador/operador de Calafate, ficha en <a href=\"https://www.patagoniachic.com/el-calafate/excursiones/perito-moreno-kayak\" rel=\"noopener\">patagoniachic.com</a>. Doble, 14+, ~1 h 30 en el Canal de los Témpanos. Paquetes de verano (febrero incluido) suelen ofrecer traslado de aeropuerto; la ficha de nov. 2026 lo deja gratis en la <em>llegada</em>. Cancelación gratis ~24 h en su <a href=\"https://www.patagoniachic.com/politica-de-cancelacion\" rel=\"noopener\">política pública</a> — verificá en vivo. No pongo voucher, ID ni mail.</li>
        <li><strong>Hielo y Aventura</strong> — Concesionaria del parque. Crampones (Minitrekking / Big Ice) o lancha corta (Safari Náutico). Otro músculo, otra tarifa. Fichas en <a href=\"#tours\">tours</a>.</li>
      </ul>
      <h3>Un circuito corto que cierra</h3>
      <ul class="season-list">
        <li><strong>Día 1</strong> — FTE, pueblo, temprano a dormir. Si el vuelo llega de día, no armes kayak esa misma tarde: el viento y el jet lag no se llevan.</li>
        <li><strong>Día 2</strong> — Glaciar: pasarelas en micro, o kayak, o minitrekking. Uno.</li>
        <li><strong>Día 3</strong> — El otro producto, o vuelo, o micro a Chaltén (eso ya es otro viaje: <a href=\"#tips\">tip</a>).</li>
      </ul>
      <p>Precios de orden de magnitud, as-of nov. 2026, ~ARS 1.550/USD. El peso se mueve: confirmá la ficha el día que pagás.</p>""",
            "en": """<p>Calafate is a base town, not a sidewalk destination. Libertador holds the grills, souvenirs, and agencies. The reason sits ~80 km away: Perito Moreno. One day covers the boardwalks; a second day covers <em>either</em> kayak <em>or</em> ice, not both.</p>
      <h3>How to reach the glacier</h3>
      <ul class="season-list">
        <li><strong>Bus</strong> — Caltur, Taqsa, Always Glaciers from the terminal. Plataforma10 on 3 Nov 2026: ~ARS 56,000–60,000 / ~USD 36–39 one way, ~1 h 15–1 h 30. Out and back the same day; confirm the last return before you disappear on the boardwalks. APN park extra (ARS 50,000 / ~USD 32 general, from 1 Jun 2026).</li>
        <li><strong>Tour with transfer</strong> — Hielo y Aventura charges mini trekking without transfer at ARS 420,000 and with transfer at ARS 500,000 (from 1 Nov 2026). Patagonia Chic adds hotel + boardwalks at ARS 90,000 on top of the kayak.</li>
        <li><strong>Car</strong> — Makes sense if you chain a second stop; for a single glacier day the bus is enough.</li>
      </ul>
      <h3>Kayak vs ice vs boardwalks only</h3>
      <ul class="season-list">
        <li><strong>Boardwalks</strong> — The plan that does not fail. You walk, you look at the wall, you go back. A jacket even in January.</li>
        <li><strong>Patagonia Chic — kayak</strong> — The one I used. Calafate aggregator/operator, card on <a href=\"https://www.patagoniachic.com/el-calafate/excursiones/perito-moreno-kayak\" rel=\"noopener\">patagoniachic.com</a>. Doubles, 14+, ~1 h 30 on the Canal de los Témpanos. Summer packages (February included) often offer an airport transfer; the Nov 2026 card leaves the <em>arrival</em> free. Free cancel ~24 h on their <a href=\"https://www.patagoniachic.com/politica-de-cancelacion\" rel=\"noopener\">public policy</a> — verify live. No voucher, ID, or email here.</li>
        <li><strong>Hielo y Aventura</strong> — Park concessionaire. Crampons (Mini trekking / Big Ice) or the short boat (Nautical safari). A different muscle, a different fare. Cards under <a href=\"#tours\">tours</a>.</li>
      </ul>
      <h3>A short circuit that closes</h3>
      <ul class="season-list">
        <li><strong>Day 1</strong> — FTE, town, early to bed. If the flight lands in daylight, do not stack kayak that same afternoon: wind and jet lag do not mix.</li>
        <li><strong>Day 2</strong> — Glacier: boardwalks by bus, or kayak, or mini trekking. One.</li>
        <li><strong>Day 3</strong> — The other product, or a flight, or the bus to Chaltén (that is already another trip: <a href=\"#tips\">tip</a>).</li>
      </ul>
      <p>Order-of-magnitude prices, as-of Nov 2026, ~ARS 1,550/USD. Pesos move: confirm the card the day you pay.</p>""",
        },
        "tips": {
            "toc_es": "Chaltén",
            "toc_en": "Chaltén",
            "es_title": "Para cuando vayas — El Chaltén",
            "en_title": "For when you go — El Chaltén",
            "es": """<p>El glaciar es Calafate; el trekking largo es Chaltén. ~2 h 40 / 215 km, micros todos los días (Cal Tur, Chaltén Travel, TAQSA), ~ARS 70.000 / ~USD 45 el tramo (oct. 2026) + tasa de terminal. <strong>Yo no lo marqué como visitado.</strong> Reservá 2–3 noches <em>después</em> del Perito Moreno. No tiene aeropuerto. Mejor oct–abr para senderos; mayo–agosto es frío y poca luz. No es day trip: el micro se come la luz.</p>""",
            "en": """<p>The glacier is Calafate; the long trekking is Chaltén. ~2 h 40 / 215 km, buses every day (Cal Tur, Chaltén Travel, TAQSA), ~ARS 70,000 / ~USD 45 one way (Oct 2026) plus terminal tax. <strong>I did not mark it as visited.</strong> Book 2–3 nights <em>after</em> Perito Moreno. No airport. Better Oct–Apr for trails; May–August is cold and short on light. Not a day trip: the bus eats the daylight.</p>""",
        },
    },
    {
        "slug": "tierra-del-fuego",
        "region": "patagonia",
        "es": {
            "name": "Tierra del Fuego",
            "where": "El fin del mundo · Ushuaia",
            "teaser": "Montaña metida en el mar. Taun para glaciar de trekking; Beagle para el agua.",
            "vibe": "Montaña metida en el mar, viento que te ordena el pelo y una ciudad que vive del turismo y de ser el punto más austral que la mayoría va a pisar. Para glaciar de trekking usé Taun, operadora local de Ushuaia: Vinciguerra es el día largo; Esmeralda el clásico más fácil.",
            "season": "Trekking y Beagle: dic–mar (pingüinos oct–mar). Ski (Cerro Castor): jun–ago. Jun–jul si la idea es sendero: viento y ~7 h de luz — se puede (Vinciguerra corre todo el año) pero el día es corto. Verano ~6–14 °C; abrigo los doce meses. Agosto es invierno fueguino: nieve en el sendero, crampones o raquetas. Pueblo y Taun en <a href=\"#ciudad\">Ushuaia</a>.",
            "arrive": "Vuelo a USH (~3 h 30). Por tierra son dos días y un cruce: casi nadie lo hace de visita. El aeropuerto (Malvinas Argentinas) está a ~4 km / 10–15 min del centro. No hay colectivo urbano que entre a la península del aeropuerto (dato oct. 2026): taxi o remís en arribos, o un transfer reservado. Listados públicos de transfer compartido andan ~ARS 20.000 por persona (mín. 2, oct. 2026–abr. 2027) — confirmá esa semana, no es un taxímetro.",
            "do": [
                "Parque Nacional Tierra del Fuego (senderos costeros; el Tren del Fin del Mundo es otro boleto).",
                "Trekking con Taun: Vinciguerra (glaciar, día largo) o Laguna Esmeralda (más fácil). Fichas públicas en <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>.",
                "Canal Beagle (faro, lobos; pingüinos oct–mar en Isla Martillo, sin desembarco).",
                "Cerro Martial. En invierno, ski en Castor; en verano, trekking largo.",
            ],
            "eat": "Centolla, merluza negra, cordero fueguino. Es caro comparado con el norte: el flete se siente. No amarro un restaurante de puerto que cambia de dueño.",
            "hack": "Ushuaia ↔ Punta Arenas: Bus-Sur / Tecni Austral, dos fronteras y un ferry de ~30 min por el Estrecho (Punta Delgada). ~USD 40–70 / CLP 58–68 mil (catálogo 2026). No hay ferry directo. No vale si tenés dos días en Ushuaia.",
        },
        "en": {
            "name": "Tierra del Fuego",
            "where": "The end of the world · Ushuaia",
            "teaser": "A mountain stuck in the sea. Taun for glacier trekking; the Beagle for the water.",
            "vibe": "A mountain stuck in the sea, wind that rearranges your hair, and a town that lives off tourism and being the southernmost point most people will ever stand on. For glacier trekking I used Taun, a local Ushuaia operator: Vinciguerra is the long day; Esmeralda is the easier classic.",
            "season": "Trekking and the Beagle: Dec–Mar (penguins Oct–Mar). Ski (Cerro Castor): Jun–Aug. Jun–Jul if the idea is a trail: wind and ~7 h of light — it is possible (Vinciguerra runs year-round) but the day is short. Summer ~6–14 °C; a jacket, twelve months. August is Fuegian winter: snow on the trail, crampons or snowshoes. Town and Taun in <a href=\"#ciudad\">Ushuaia</a>.",
            "arrive": "Fly to USH (~3 h 30). Overland is two days and a border: almost nobody does it as a visit. The airport (Malvinas Argentinas) is ~4 km / 10–15 min from the centre. No city bus enters the airport peninsula (Oct 2026 note): taxi or remis at arrivals, or a booked transfer. Public shared-transfer listings sit around ARS 20,000 per person (min. 2, Oct 2026–Apr 2027) — confirm that week; it is not a meter.",
            "do": [
                "Tierra del Fuego National Park (coastal trails; the End of the World Train is a different ticket).",
                "Trekking with Taun: Vinciguerra (glacier, long day) or Laguna Esmeralda (easier). Public cards on <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>.",
                "Beagle Channel (lighthouse, sea lions; penguins Oct–Mar on Isla Martillo, no landing).",
                "Cerro Martial. In winter, ski at Castor; in summer, long treks.",
            ],
            "eat": "King crab, black hake, Fuegian lamb. It is expensive compared with the north: you feel the freight. I am not locking a harbour restaurant that changes hands.",
            "hack": "Ushuaia ↔ Punta Arenas: Bus-Sur / Tecni Austral, two borders and a ~30 min Magellan Strait ferry (Punta Delgada). ~USD 40–70 / CLP 58–68k (2026 catalogue). There is no direct ferry. Skip it if you only have two days in Ushuaia.",
        },
        "legs_es": [("air", "Avión ~3 h 30"), ("warn", "Tierra: 2 días")],
        "legs_en": [("air", "Flight ~3 h 30"), ("warn", "Overland: 2 days")],
        "nearby": ["santa-cruz"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Tierra del Fuego (APN)",
                "en_name": "Tierra del Fuego National Park (APN)",
                "es": "El parque al oeste de la ciudad. Entrada oficial. Senderos costeros; el Tren del Fin del Mundo es otro boleto, no el parque.",
                "en": "The park west of town. Official gate fee. Coastal trails; the End of the World Train is a different ticket, not the park.",
                "duration_es": "tu día en el parque",
                "duration_en": "your park day",
                "includes_es": "senderos habilitados; tren y Beagle aparte",
                "includes_en": "open trails; train and Beagle extra",
                "ars": APN["tdf"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; nacionales ARS 18.000",
                "note_en": "general fee; Argentine residents ARS 18,000",
            },
            {
                "url": "https://taunushuaia.com.ar/excursion/laguna-esmeralda/",
                "es_name": "Taun — Laguna Esmeralda",
                "en_name": "Taun — Laguna Esmeralda",
                "es": "La misma operadora local que recomiendo para Vinciguerra. El clásico fácil: 9 km, 300 m, 5 h, todo el año. Guías de montaña (EPGAMT/AAGM). Packrafting y otras fichas: mirá <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>, no un teléfono. El viento cancela.",
                "en": "The same local operator I recommend for Vinciguerra. The easy classic: 9 km, 300 m, 5 h, year-round. Mountain guides (EPGAMT/AAGM). Packrafting and other cards: look at <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>, not a phone number. Wind cancels.",
                "duration_es": "5 h · 9 km · 300 m · baja · todo el año",
                "duration_en": "5 h · 9 km · 300 m · easy · year-round",
                "includes_es": "traslados hotel, guía certificado, vianda, seguro, bastones y crampones/raquetas; ropa y calzado no",
                "includes_en": "hotel transfers, certified guide, packed lunch, insurance, poles and crampons/snowshoes; clothes and boots extra",
                "ars": 140000,
                "asof": "taunushuaia.com.ar/excursion/laguna-esmeralda/, nov. 2026",
                "asof_en": "taunushuaia.com.ar/excursion/laguna-esmeralda/, Nov 2026",
                "note_es": "publicado en ARS en la ficha; el sitio también muestra USD",
                "note_en": "listed in ARS on the card; the site also shows USD",
            },
            {
                "url": "https://taunushuaia.com.ar/excursion/glaciar-vinciguerra/",
                "es_name": "Taun — Trekking Glaciar Vinciguerra",
                "en_name": "Taun — Vinciguerra Glacier trek",
                "rec_es": "Lo hice — operadora local, ficha pública",
                "rec_en": "I did this — local operator, public card",
                "es": "Operadora local de Ushuaia (guías de montaña nacidos acá). La recomiendo para glaciar de trekking: hice el Vinciguerra un agosto (invierno fueguino). Día largo: Valle de Andorra, turbal RAMSAR, bosque, Laguna de los Témpanos y el glaciar. Nivel medio: ritmo constante, no sprint. El hielo retrocede y las cuevas cambian — confirmá qué está abierto ese día. Mini-trekking sobre el hielo: temporada de verano, según la ficha. El viento cancela. Sólo páginas públicas: no pongo teléfono, mail ni reserva.",
                "en": "A local Ushuaia operator (mountain guides born here). I recommend them for glacier trekking: I did Vinciguerra one August (Fuegian winter). A long day: Valle de Andorra, RAMSAR peat bog, forest, Laguna de los Témpanos and the glacier. Moderate grade: a steady pace, not a sprint. The ice is receding and the caves change — confirm what is open that day. Mini glacier trek: summer season, per the card. Wind cancels. Public pages only: no phone, email, or booking on this site.",
                "duration_es": "8 h · 14 km · 650 m · media · todo el año",
                "duration_en": "8 h · 14 km · 650 m · moderate · year-round",
                "includes_es": "traslados, equipo técnico (bastones, crampones/raquetas, casco), comida, guía certificado, seguro; abrigo, calzado y botella aparte",
                "includes_en": "transfers, technical kit (poles, crampons/snowshoes, helmet), food, certified guide, insurance; warm clothes, boots and bottle extra",
                "ars": 190000,
                "ars_high": 235000,
                "asof": "taunushuaia.com.ar/excursion/glaciar-vinciguerra/, nov. 2026 (listados terceros oct. 2026–abr. 2027)",
                "asof_en": "taunushuaia.com.ar/excursion/glaciar-vinciguerra/, Nov 2026 (third-party listings Oct 2026–Apr 2027)",
                "note_es": "ficha Taun ARS 190.000; agencias terceras a veces ~ARS 235.000. En 2025 este día se movía en el orden de unos pocos cientos de miles de ARS (rango, no factura)",
                "note_en": "Taun card ARS 190,000; third-party agencies sometimes ~ARS 235,000. In 2025 this day sat on the order of a few hundred thousand ARS (a range, not an invoice)",
            },
            {
                "url": "https://www.canoerocatamaranes.com.ar/product/navegacion-pinguinera/",
                "es_name": "Canoero — Beagle pingüinera (Isla Martillo)",
                "en_name": "Canoero — Beagle penguins (Isla Martillo)",
                "es": "Catamarán desde el muelle: lobos, faro Les Eclaireurs e Isla Martillo. No se baja a la isla. Oct–mar. La navegación corta a Isla de los Lobos (sin pingüinos) es ARS 123.000 / ~3 h, todo el año. Tolkeyen y otras lanchas en el puerto: compará, no persigas fauna. Viento cancela.",
                "en": "Catamaran from the pier: sea lions, Les Eclaireurs lighthouse, and Isla Martillo. No landing on the island. Oct–Mar. The short Isla de los Lobos run (no penguins) is ARS 123,000 / ~3 h, year-round. Tolkeyen and other boats at the port: compare, do not chase wildlife. Wind cancels.",
                "duration_es": "~5 h (oct–mar)",
                "duration_en": "~5 h (Oct–Mar)",
                "includes_es": "navegación + tasa de puerto ARS 6.000; no incluye traslado ni desembarco",
                "includes_en": "navigation + ARS 6,000 port tax; transfer and landing extra / not offered",
                "ars": 213000,
                "asof": "canoerocatamaranes.com.ar, vigencia hasta 31/12/2026",
                "asof_en": "canoerocatamaranes.com.ar, valid through 31 Dec 2026",
                "note_es": "por persona, tasa incluida; 4–11 años 50%",
                "note_en": "per person, tax included; ages 4–11 pay 50%",
            },
        ],
        "city_extra": {
            "toc_es": "Ushuaia",
            "toc_en": "Ushuaia",
            "es_title": "Ushuaia: pueblo, glaciar, cómo armar los días",
            "en_title": "Ushuaia: town, glacier, how to stack the days",
            "es": """<p>Ushuaia es chica y cara. El centro se camina: Maipú al puerto, las cuestas al norte. El viento manda más que el reloj. Un día de glaciar + un Beagle + el parque ya es un viaje; no apiles Vinciguerra y Martillo el mismo día.</p>
      <h3>Taun, la que usé para glaciar</h3>
      <p>Operadora local de Ushuaia — guías de montaña nacidos acá, no un mostrador de hotel. Fichas públicas en <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>. Hice el <a href=\"https://taunushuaia.com.ar/excursion/glaciar-vinciguerra/\" rel=\"noopener\">Trekking Glaciar Vinciguerra</a> un agosto (invierno fueguino): hay nieve, luz corta y el viento puede cancelar. La recomiendo para glaciar de trekking. <a href=\"https://taunushuaia.com.ar/excursion/laguna-esmeralda/\" rel=\"noopener\">Laguna Esmeralda</a> es la hermana fácil si el grupo no está para 14 km y 650 m. Ojo del Albino y packrafting existen en el mismo sitio; no los cotizo si no vi la ficha ese día. No pongo teléfono, mail, dirección ni código de reserva.</p>
      <h3>Qué sale, en rangos</h3>
      <ul class="season-list">
        <li><strong>Vinciguerra</strong> — Ficha Taun nov. 2026: ARS 190.000 / ~USD 123. Agencias terceras a veces piden ~ARS 235.000 (listados oct. 2026–abr. 2027). En 2025 este tipo de día se movía en el orden de unos pocos cientos de miles de ARS — rango, no factura. Confirmá en la ficha el día que pagás.</li>
        <li><strong>Laguna Esmeralda</strong> — ARS 140.000 / ~USD 90 en la ficha de nov. 2026.</li>
        <li><strong>Parque nacional</strong> — APN ARS 40.000 / ~USD 26 general (desde 1 jun 2026). El tren es otro boleto.</li>
        <li><strong>Beagle pingüinera</strong> — Canoero ARS 213.000 / ~USD 137 con tasa, oct–mar (vigencia hasta 31/12/2026). El corto a lobos/faro corre más meses.</li>
      </ul>
      <h3>Cómo moverse</h3>
      <ul class="season-list">
        <li><strong>Aeropuerto</strong> — ~4 km, 10–15 min. No hay colectivo urbano a la península (oct. 2026). Taxi/remís en arribos; transfer compartido listado ~ARS 20.000 por persona (mín. 2). No invento el total del taxímetro.</li>
        <li><strong>Pueblo</strong> — A pie. Taxi si llueve o si el hotel está arriba de la cuesta.</li>
        <li><strong>Parque / Martial / Castor</strong> — Transfer de la excursión, remís o auto. El parque al oeste no es una cuadra.</li>
      </ul>
      <h3>Un circuito que cierra</h3>
      <ul class="season-list">
        <li><strong>Día 1</strong> — USH, pueblo, Martial o nada. No armes Vinciguerra el mismo día del vuelo.</li>
        <li><strong>Día 2</strong> — Vinciguerra (largo) o Esmeralda (más corto). Uno.</li>
        <li><strong>Día 3</strong> — Beagle, o parque nacional, o ski si es invierno. El cruce a Punta Arenas se come un día entero: no lo metas en una visita de 48 h (ver <a href=\"#hack\">hack</a>).</li>
      </ul>
      <p>Precios de orden de magnitud, as-of nov. 2026, ~ARS 1.550/USD. El peso se mueve.</p>""",
            "en": """<p>Ushuaia is small and expensive. The centre is walkable: Maipú to the port, the hills to the north. Wind outranks the clock. One glacier day + one Beagle + the park is already a trip; do not stack Vinciguerra and Martillo on the same day.</p>
      <h3>Taun, the operator I used for glacier</h3>
      <p>A local Ushuaia operator — mountain guides born here, not a hotel desk. Public cards on <a href=\"https://taunushuaia.com.ar/\" rel=\"noopener\">taunushuaia.com.ar</a>. I did the <a href=\"https://taunushuaia.com.ar/excursion/glaciar-vinciguerra/\" rel=\"noopener\">Vinciguerra Glacier trek</a> one August (Fuegian winter): snow, short light, and wind can cancel. I recommend them for glacier trekking. <a href=\"https://taunushuaia.com.ar/excursion/laguna-esmeralda/\" rel=\"noopener\">Laguna Esmeralda</a> is the easier sibling if the group is not up for 14 km and 650 m. Ojo del Albino and packrafting live on the same site; I do not quote them if I have not seen that day’s card. No phone, email, address, or booking code here.</p>
      <h3>What it costs, in ranges</h3>
      <ul class="season-list">
        <li><strong>Vinciguerra</strong> — Taun card Nov 2026: ARS 190,000 / ~USD 123. Third-party agencies sometimes ask ~ARS 235,000 (listings Oct 2026–Apr 2027). In 2025 this kind of day sat on the order of a few hundred thousand ARS — a range, not an invoice. Confirm on the card the day you pay.</li>
        <li><strong>Laguna Esmeralda</strong> — ARS 140,000 / ~USD 90 on the Nov 2026 card.</li>
        <li><strong>National park</strong> — APN ARS 40,000 / ~USD 26 general (from 1 Jun 2026). The train is a different ticket.</li>
        <li><strong>Beagle penguins</strong> — Canoero ARS 213,000 / ~USD 137 with tax, Oct–Mar (valid through 31 Dec 2026). The short sea-lion/lighthouse run covers more months.</li>
      </ul>
      <h3>Getting around</h3>
      <ul class="season-list">
        <li><strong>Airport</strong> — ~4 km, 10–15 min. No city bus onto the peninsula (Oct 2026). Taxi/remis at arrivals; shared-transfer listings ~ARS 20,000 per person (min. 2). I am not inventing a meter total.</li>
        <li><strong>Town</strong> — On foot. A taxi if it rains or if the hotel sits up the hill.</li>
        <li><strong>Park / Martial / Castor</strong> — Tour transfer, remis, or a car. The park to the west is not a block away.</li>
      </ul>
      <h3>A circuit that closes</h3>
      <ul class="season-list">
        <li><strong>Day 1</strong> — USH, town, Martial or nothing. Do not stack Vinciguerra on the flight day.</li>
        <li><strong>Day 2</strong> — Vinciguerra (long) or Esmeralda (shorter). One.</li>
        <li><strong>Day 3</strong> — Beagle, or the national park, or ski if it is winter. The crossing to Punta Arenas eats a whole day: do not fold it into a 48 h visit (see the <a href=\"#hack\">hack</a>).</li>
      </ul>
      <p>Order-of-magnitude prices, as-of Nov 2026, ~ARS 1,550/USD. Pesos move.</p>""",
        },
    },
]

NOT_YET = [
    ("Chaco", "Impenetrable y Resistencia: aún no.", "Impenetrable forest and Resistencia: not yet."),
    ("Corrientes", "Esteros del Iberá / Colonia Carlos Pellegrini, carnaval. Aún no pisé: 4×4, mosquitos, mejor en seca (abr–oct). Tip, no pin.", "Iberá wetlands / Colonia Carlos Pellegrini, carnival. I have not been: 4×4, mosquitoes, better in the dry (Apr–Oct). A tip, not a pin."),
    ("Formosa", "Bañado La Estrella y frontera con Paraguay. Aún no. Humedal, calor, logística propia. Tip, no pin.", "Bañado La Estrella and the Paraguay border. Not yet. Wetland, heat, its own logistics. A tip, not a pin."),
    ("La Pampa", "Pampa interior. Aún no.", "Interior pampas. Not yet."),
    ("La Rioja", "Talampaya queda acá. Aún no.", "Talampaya is here. Not yet."),
    ("Neuquén", "Villa La Angostura y San Martín de los Andes: yo marqué Bariloche en Río Negro.", "Villa La Angostura and San Martín de los Andes: I marked Bariloche in Río Negro."),
    ("San Juan", "Cuyo norte, Ischigualasto. Aún no.", "Northern Cuyo, Ischigualasto. Not yet."),
    ("San Luis", "Sierras puntanas. Aún no.", "Puntano sierras. Not yet."),
]

SLUG_BY = {p["slug"]: p for p in PROVINCES}


def esc(s: str) -> str:
    return s.replace("&", "&amp;") if s else s


def legs_html(legs):
    bits = []
    for kind, text in legs:
        bits.append(f'<span class="leg {kind}">{text}</span>')
    return " ".join(bits)


def tour_html(t, lang):
    name = t["en_name"] if lang == "en" else t["es_name"]
    body = t["en"] if lang == "en" else t["es"]
    asof = t.get("asof_en") if lang == "en" else t.get("asof")
    note = t.get("note_en") if lang == "en" else t.get("note_es")
    duration = t.get("duration_en") if lang == "en" else t.get("duration_es")
    includes = t.get("includes_en") if lang == "en" else t.get("includes_es")
    override = t.get("price_en") if lang == "en" else t.get("price_es")
    if override:
        price_line = f"{override} · {note}" if note else override
    elif t.get("usd_only"):
        price = t["usd_only_en"] if lang == "en" else t["usd_only"]
        price_line = f"{price} · {note}" if note else price
    elif t.get("ars"):
        lo, hi = t["ars"], t.get("ars_high")
        ars_bit = f"ARS {ars_fmt(lo, lang)}–{ars_fmt(hi, lang)}" if hi else f"ARS {ars_fmt(lo, lang)}"
        price_line = f"{ars_bit} / {usd_span(lo, hi)}"
        if note:
            price_line = f"{price_line} · {note}"
    else:
        price_line = note or ("confirm with the operator" if lang == "en" else "confirmá en el operador")
    asof_html = f' <span class="asof">({asof})</span>' if asof else ""
    meta = []
    if duration:
        dk = "Duration" if lang == "en" else "Duración"
        meta.append(f'<p class="tour-meta"><span>{dk}</span> {duration}</p>')
    if includes:
        ik = "Includes" if lang == "en" else "Incluye"
        meta.append(f'<p class="tour-meta"><span>{ik}</span> {includes}</p>')
    meta_html = ("\n          " + "\n          ".join(meta) + "\n          ") if meta else "\n          "
    rec = t.get("rec_en") if lang == "en" else t.get("rec_es")
    rec_html = f'\n          <p class="tour-rec">{rec}</p>' if rec else ""
    url = t["url"]
    return f"""        <article class="tour">
          <h3><a href="{url}" rel="noopener">{name}</a></h3>{rec_html}
          <p>{body}</p>{meta_html}<p class="price">{price_line}{asof_html}</p>
        </article>"""


def nearby_html(slugs, lang, prefix):
    links = []
    for s in slugs:
        p = SLUG_BY[s]
        name = p[lang]["name"]
        links.append(f'<a href="{prefix}{s}/">{name}</a>')
    return "\n          ".join(links)


def header_nav(lang, es_href, en_href, depth_to_site):
    es_cur = ' aria-current="page"' if lang != "en" else ""
    en_cur = ' aria-current="page"' if lang == "en" else ""
    label = "Language" if lang == "en" else "Idioma"
    return f"""  <header class="site">
    <strong>Aldo Escobar</strong>
    <nav>
      <a href="{depth_to_site}">CV</a>
      <a href="{depth_to_site}travel/">Travel</a>
      <a href="{depth_to_site}blog/">Blog</a>
      <a href="https://github.com/aoelvp94">GitHub</a>
      <span class="lang" aria-label="{label}">
        <a href="{es_href}" hreflang="es"{es_cur}>ES</a><span class="sep" aria-hidden="true">|</span><a href="{en_href}" hreflang="en"{en_cur}>EN</a>
      </span>
    </nav>
  </header>"""


def province_page(p, lang):
    loc = p[lang]
    other = "en" if lang == "es" else "es"
    slug = p["slug"]
    if lang == "es":
        depth_site = "../../"
        css = "../guide.css"
        hub = "../"
        es_href = "./"
        en_href = f"../en/{slug}/"
        nearby_prefix = "../"
        hreflang_es = f"https://aoelvp94.github.io/argentina/{slug}/"
        hreflang_en = f"https://aoelvp94.github.io/argentina/en/{slug}/"
        title = f"{loc['name']} — guía de Aldo"
        desc = loc["teaser"]
        crumb = f'<a href="../">Guía Argentina</a> / {loc["name"]}'
        toc_hub = "Guía"
        toc_season = "Época"
        toc_arrive = "Llegar"
        toc_do = "Qué hacer"
        toc_tours = "Tours"
        toc_eat = "Comer"
        toc_hack = "Hack"
        from_k = "Desde BA"
        h_season = "Mejor época"
        h_arrive = "Cómo llegar"
        h_do = "Qué hacer"
        h_tours = "Tours y entradas (precios públicos)"
        h_eat = "Comer"
        h_hack = "Hack local"
        h_near = "Cerca en esta guía"
        h_note = "Hemisferio sur"
        season_note = "Diciembre es verano, julio es invierno."
        visited = "Visitado por Aldo"
        tours_empty = "Acá no hay un operador único que yo pueda recomendar con nombre y tarifa pública. Parque o salida: confirmá en el lugar y mirá reseñas de esta temporada."
        fx = "USD al ~ARS 1.550 (BNA, nov. 2026). El peso se mueve: usá el número para saber si es un café o un sueldo. Tarifas públicas del operador o de APN; si no hay hoja, GetYourGuide / Viator / foros locales — no un precio inventado."
        last = f'<p><a href="../">Volver a la guía</a> · transporte, micros y plata nacional están en la hub. Cabotaje a principios de nov. 2026: Aerolíneas Argentinas y JetSMART.</p>'
    else:
        depth_site = "../../../"
        css = "../../guide.css"
        hub = "../"
        es_href = f"../../{slug}/"
        en_href = "./"
        nearby_prefix = "../"
        hreflang_es = f"https://aoelvp94.github.io/argentina/{slug}/"
        hreflang_en = f"https://aoelvp94.github.io/argentina/en/{slug}/"
        title = f"{loc['name']} — Aldo’s guide"
        desc = loc["teaser"]
        crumb = f'<a href="../">Argentina guide</a> / {loc["name"]}'
        toc_hub = "Guide"
        toc_season = "When"
        toc_arrive = "Getting there"
        toc_do = "What to do"
        toc_tours = "Tours"
        toc_eat = "Food"
        toc_hack = "Hack"
        from_k = "From BA"
        h_season = "Best time"
        h_arrive = "Getting there"
        h_do = "What to do"
        h_tours = "Tours and tickets (public prices)"
        h_eat = "Eat"
        h_hack = "Local hack"
        h_near = "Nearby in this guide"
        h_note = "Southern Hemisphere"
        season_note = "December is summer, July is winter."
        visited = "Visited by Aldo"
        tours_empty = "There is no single operator here I can name with a public rate sheet. Park or outing: confirm on the ground and read this season’s reviews."
        fx = "USD at ~ARS 1,550 (BNA, Nov 2026). Pesos move: use the number to know whether you are talking about a coffee or a salary. Public operator or APN fares; if there is no sheet, GetYourGuide / Viator / local forums — not an invented price."
        last = f'<p><a href="../">Back to the guide</a> · national transport, long-distance buses, and money live on the hub. Domestic air as of early Nov 2026: Aerolíneas Argentinas and JetSMART.</p>'

    # EN province nearby links are sibling folders under /argentina/en/
    if lang == "en":
        nearby_prefix = "../"
        depth_site = "../../../"
        # wait: argentina/en/jujuy/ -> site root is ../../..  that's argentina/en/jujuy -> en -> argentina -> repo. Yes ../../../
        # CV is at repo root. argentina/en/jujuy/index.html -> ../../../ is repo root. Good.
        # hub EN is ../ (argentina/en/)
        # nearby EN provinces: ../salta/ 
    else:
        depth_site = "../../"
        # argentina/jujuy/ -> ../../ is repo root. Good.

    do_items = "\n        ".join(f"<li>{item}</li>" for item in loc["do"])
    tours = p["tours"]
    if tours:
        tours_block = "\n".join(tour_html(t, lang) for t in tours)
        tours_section = f"""    <div class="section" id="tours">
      <h2>{h_tours}</h2>
      <p class="kicker">{fx}</p>
      <div class="tour-list">
{tours_block}
      </div>
    </div>"""
    else:
        tours_section = f"""    <div class="section" id="tours">
      <h2>{h_tours}</h2>
      <p>{tours_empty}</p>
    </div>"""

    city = p.get("city_extra")
    if city:
        ctitle = city["en_title"] if lang == "en" else city["es_title"]
        cbody = city["en"] if lang == "en" else city["es"]
        toc_city = city.get("toc_en" if lang == "en" else "toc_es") or (
            "City" if lang == "en" else "Ciudad"
        )
        toc_city_link = f'\n      <a href="#ciudad">{toc_city}</a>'
        extra_section = f"""    <div class="section" id="ciudad">
      <h2>{ctitle}</h2>
      {cbody}
    </div>
"""
    else:
        toc_city_link = ""
        extra_section = ""

    tips = p.get("tips")
    if tips:
        ttitle = tips["en_title"] if lang == "en" else tips["es_title"]
        tbody = tips["en"] if lang == "en" else tips["es"]
        flag_h = tips.get("en_flag_h" if lang == "en" else "es_flag_h") or (
            "Not a visited pin" if lang == "en" else "No es un pin visitado"
        )
        flag_p = tips.get("en_flag_p" if lang == "en" else "es_flag_p") or (
            "Side-trip or curiosity for readers. I did not mark this as a place I went."
            if lang == "en"
            else "Tip o curiosidad para quien va. Yo no lo marqué como lugar que recorrí."
        )
        toc_tips_label = tips.get("toc_en" if lang == "en" else "toc_es") or "Tips"
        toc_tips_link = f'\n      <a href="#tips">{toc_tips_label}</a>'
        tips_section = f"""    <div class="section" id="tips">
      <h2>{ttitle}</h2>
      <div class="note tip-not-visited">
        <strong>{flag_h}</strong>
        {flag_p}
      </div>
      {tbody}
    </div>
"""
    else:
        toc_tips_link = ""
        tips_section = ""

    extra_anchor = f' id="{p["extra_id"]}"' if p.get("extra_id") else ""
    legs = legs_html(p["legs_en"] if lang == "en" else p["legs_es"])
    lang_attr = "en" if lang == "en" else "es-AR"

    return f"""<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="alternate" hreflang="es" href="{hreflang_es}">
  <link rel="alternate" hreflang="en" href="{hreflang_en}">
  <link rel="stylesheet" href="{css}">
</head>
<body>
{header_nav(lang, es_href, en_href, depth_site)}
  <nav class="toc" aria-label="{'On this page' if lang == 'en' else 'Índice'}">
    <div class="toc-inner">
      <a href="{hub}">{toc_hub}</a>
      <a href="#epoca">{toc_season}</a>
      <a href="#llegar">{toc_arrive}</a>
      <a href="#hacer">{toc_do}</a>{toc_city_link}{toc_tips_link}
      <a href="#tours">{toc_tours}</a>
      <a href="#comer">{toc_eat}</a>
      <a href="#hack">{toc_hack}</a>
    </div>
  </nav>
  <main>
    <p class="crumb">{crumb}</p>
    <h1{extra_anchor}>{loc['name']}</h1>
    <p class="intro">{loc['vibe']}</p>
    <p class="meta-line">
      <span class="badge">{visited}</span>
      <span>{loc['where']}</span>
    </p>
    <p class="from-ba"><span class="from-ba-k">{from_k}</span> {legs}</p>

    <div class="section" id="epoca">
      <h2>{h_season}</h2>
      <div class="note">
        <strong>{h_note}</strong>
        {season_note}
      </div>
      <p>{loc['season']}</p>
    </div>

    <div class="section" id="llegar">
      <h2>{h_arrive}</h2>
      <p>{loc['arrive']}</p>
    </div>

    <div class="section" id="hacer">
      <h2>{h_do}</h2>
      <ul>
        {do_items}
      </ul>
    </div>

{extra_section}
{tips_section}
{tours_section}

    <div class="section" id="comer">
      <h2>{h_eat}</h2>
      <p>{loc['eat']}</p>
    </div>

    <div class="section" id="hack">
      <h2>{h_hack}</h2>
      <p>{loc['hack']}</p>
    </div>

    <div class="section">
      <h2>{h_near}</h2>
      <div class="nearby">
          {nearby_html(p['nearby'], lang, nearby_prefix)}
      </div>
      {last}
    </div>
  </main>
</body>
</html>
"""


def hub_grid(lang):
    cards = []
    for p in PROVINCES:
        loc = p[lang]
        legs = legs_html(p["legs_en"] if lang == "en" else p["legs_es"])
        more = "Abrir la página →" if lang != "en" else "Open the page →"
        from_k = "Desde BA" if lang != "en" else "From BA"
        cards.append(
            f"""      <a class="prov-card" href="{p['slug']}/">
        <span class="badge">{'Visitado por Aldo' if lang != 'en' else 'Visited by Aldo'}</span>
        <h3>{loc['name']}</h3>
        <p class="where">{loc['where']}</p>
        <p class="from-ba"><span class="from-ba-k">{from_k}</span> {legs}</p>
        <p>{loc['teaser']}</p>
        <span class="more">{more}</span>
      </a>"""
        )
    notyet = []
    for name, es, en in NOT_YET:
        blurb = en if lang == "en" else es
        notyet.append(f"        <article><h3>{name}</h3><p>{blurb}</p></article>")
    if lang == "en":
        h2 = "Provinces I actually went to"
        lead = "One page each — seasons, how to get there, food, and tours with public prices. The map pins jump here. National transport, long-distance buses, money, and the hack trips that cross borders stay on this hub."
        h3 = "Not yet"
        ny_lead = "Short notes, not fake itineraries. Neuquén would be Villa La Angostura; I marked Bariloche in Río Negro."
    else:
        h2 = "Provincias que yo sí recorrí"
        lead = "Una página cada una: época, cómo llegar, comida y tours con precios públicos. Los pines del mapa saltan acá. Transporte nacional, micros, plata y los hacks que cruzan frontera se quedan en esta hub."
        h3 = "Aún no"
        ny_lead = "Notas cortas, no itinerarios inventados. Neuquén sería Villa La Angostura; Bariloche lo marqué en Río Negro."
    return f"""    <div class="section" id="provincias">
      <h2>{h2}</h2>
      <p>{lead}</p>
      <div class="prov-grid">
{chr(10).join(cards)}
      </div>
      <h3>{h3}</h3>
      <p>{ny_lead}</p>
      <div class="unvisited-grid">
{chr(10).join(notyet)}
      </div>
    </div>
"""


LINK_MAP = [
    ('href="#lugar-jujuy"', 'href="jujuy/"'),
    ('href="#lugar-salta"', 'href="salta/"'),
    ('href="#lugar-tucuman"', 'href="tucuman/"'),
    ('href="#lugar-santiago"', 'href="santiago-del-estero/"'),
    ('href="#lugar-misiones"', 'href="misiones/"'),
    ('href="#lugar-entre-rios"', 'href="entre-rios/"'),
    ('href="#lugar-rosario"', 'href="santa-fe/"'),
    ('href="#lugar-cordoba"', 'href="cordoba/"'),
    ('href="#lugar-caba"', 'href="caba/"'),
    ('href="#lugar-pba"', 'href="buenos-aires/"'),
    ('href="#lugar-mdp"', 'href="buenos-aires/#mar-del-plata"'),
    ('href="#lugar-mendoza"', 'href="mendoza/"'),
    ('href="#lugar-madryn"', 'href="chubut/"'),
    ('href="#lugar-bariloche"', 'href="rio-negro/"'),
    ('href="#lugar-calafate"', 'href="santa-cruz/"'),
    ('href="#lugar-ushuaia"', 'href="tierra-del-fuego/"'),
    ('href="#lugares"', 'href="#provincias"'),
]


def patch_hub(path: Path, lang: str):
    text = path.read_text(encoding="utf-8")
    if lang == "es":
        text = text.replace("<html lang=\"es-AR\">", "<html lang=\"es-AR\" data-guide-root=\"./\">", 1)
        text = text.replace("<a href=\"#lugares\">Lugares</a>", "<a href=\"#provincias\">Provincias</a>", 1)
        text = text.replace(
            "ahora con mapa, <a href=\"#tiempos\">tiempos reales desde Buenos Aires</a>, <a href=\"#hacks\">hack trips</a>, precios de orden de magnitud y fichas de los lugares que <strong>yo sí recorrí</strong>.",
            "ahora con mapa, <a href=\"#tiempos\">tiempos reales desde Buenos Aires</a>, <a href=\"#hacks\">hack trips</a> y <strong>una página por provincia que yo sí recorrí</strong>.",
        )
        text = text.replace(
            "<title>Argentina — guía de Aldo Escobar</title>",
            "<title>Argentina — guía de Aldo Escobar</title>",
        )
        text = text.replace(
            'content="Guía práctica y navegable de Argentina: mapa de lugares visitados, transporte, comida, plata y cultura, en primera persona."',
            'content="Guía práctica de Argentina: mapa de provincias, una página por destino visitado, transporte, comida y cultura. Primera persona."',
        )
    else:
        text = text.replace("<html lang=\"en\">", "<html lang=\"en\" data-guide-root=\"./\">", 1)
        text = text.replace("<a href=\"#lugares\">Places</a>", "<a href=\"#provincias\">Provinces</a>", 1)
        text = text.replace(
            "now with a map, <a href=\"#tiempos\">real travel times from Buenos Aires</a>, <a href=\"#hacks\">hack trips</a>, order-of-magnitude prices, and cards for the places <strong>I actually went to</strong>.",
            "now with a map, <a href=\"#tiempos\">real travel times from Buenos Aires</a>, <a href=\"#hacks\">hack trips</a>, and <strong>one page per province I actually went to</strong>.",
        )
        text = text.replace(
            'content="A practical, navigable Argentina guide: visited-places map, transport, food, money and culture, in first person."',
            'content="A practical Argentina guide: province map, one page per place visited, transport, food and culture. First person."',
        )

    start = text.find('<div class="section" id="lugares">')
    if start == -1:
        start = text.find('<div class="section" id="provincias">')
    end = text.find('<div class="section" id="transporte">')
    if start == -1 or end == -1:
        raise SystemExit(f"hub markers missing in {path}")
    text = text[:start] + hub_grid(lang) + "\n" + text[end:]

    for old, new in LINK_MAP:
        text = text.replace(old, new)

    # filters JS was in map.js and is gone; leftover filters already removed with lugares
    path.write_text(text, encoding="utf-8")


def main():
    for p in PROVINCES:
        es_dir = ROOT / p["slug"]
        en_dir = ROOT / "en" / p["slug"]
        es_dir.mkdir(parents=True, exist_ok=True)
        en_dir.mkdir(parents=True, exist_ok=True)
        (es_dir / "index.html").write_text(province_page(p, "es"), encoding="utf-8")
        (en_dir / "index.html").write_text(province_page(p, "en"), encoding="utf-8")
    patch_hub(ROOT / "index.html", "es")
    patch_hub(ROOT / "en" / "index.html", "en")
    print(f"wrote {len(PROVINCES)} provinces × 2 + patched hub grids")


if __name__ == "__main__":
    main()
