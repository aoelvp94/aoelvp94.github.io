#!/usr/bin/env python3
"""Generate bilingual Argentina hub teasers + one page per visited province."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
FX = 1550  # ~ARS per USD, BNA early Nov 2026


def usd(ars: int) -> str:
    return f"~USD {int(round(ars / FX))}"


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
        "nearby": ["salta", "tucuman", "santiago-del-estero"],
        "tours": [
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Calilegua (APN)",
                "en_name": "Calilegua National Park (APN)",
                "es": "Selva de yungas, no puna. Entrada oficial; no hace falta un tour para caminar los senderos habilitados.",
                "en": "Yungas jungle, not puna. Official gate fee; you do not need a tour for the open trails.",
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
                "Centro y Cerro San Bernardo.",
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
                "The centre and Cerro San Bernardo.",
                "Cachi or Cafayate via Ruta 40/68; torrontés at wineries.",
                "High Mountain Archaeology Museum if Inca history pulls you in.",
                "Los Cardones National Park on the way to Cachi.",
            ],
            "eat": "Salta empanadas (juicy, often baked), locro, tamales, goat. A downtown classic is Doña Salta (queues are normal). A folklore peña at night if that’s your thing.",
            "hack": "The solid combo is Salta + Quebrada + salt flats, 4–5 days. Onward to Bolivia: bus Salta→La Quiaca (~7 h, Andesmar/Balut, from ~ARS 35,000 / ~USD 23, Oct 2026) and the bridge into Villazón. The Chile bus via Jama leaves from here before dawn.",
        },
        "legs_es": [("bus", "Micro ~18–20 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~18–20 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["jujuy", "tucuman", "santiago-del-estero"],
        "tours": [
            {
                "url": "https://movitrack.com.ar/",
                "es_name": "Movitrack (safaris 4×4 y valles)",
                "en_name": "Movitrack (4×4 safaris and valley days)",
                "es": "Operador salteño conocido para valles y 4×4. Confirmá el precio del día en su web: cambia con temporada y grupo. Tren a las Nubes es otra postal (no corre todos los días).",
                "en": "A well-known Salta operator for valleys and 4×4 days. Confirm that day’s price on their site: it moves with season and group size. Tren a las Nubes is another postcard (not daily).",
                "ars": None,
                "asof": "confirmá en el operador",
                "asof_en": "confirm with the operator",
                "note_es": "no publico un número que no esté en su tarifa",
                "note_en": "no invented fare — check their rate sheet",
            },
            {
                "url": "https://www.argentina.gob.ar/parquesnacionales/tarifas",
                "es_name": "Parque Nacional Los Cardones (APN)",
                "en_name": "Los Cardones National Park (APN)",
                "es": "Cardones y ruta a Cachi. Entrada oficial.",
                "en": "Cardón cactus and the Cachi road. Official gate fee.",
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
                "Tafí del Valle si tenés un día extra.",
                "Ruinas de Quilmes hacia el oeste.",
            ],
            "eat": "Sánguche de milanesa (el clásico tucumano, en pan sanguchero) y empanadas tucumanas. Eso, antes que cualquier restaurante «de autor». Buscá sangucherías de barrio.",
            "hack": "Fácil de encadenar con Santiago del Estero o Salta. No amarro un operador puntual para Tafí/Quilmes: auto o agencia local, vehículo en condiciones para la cuesta.",
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
                "Tafí del Valle if you have an extra day.",
                "Quilmes ruins to the west.",
            ],
            "eat": "Milanesa sandwich (the Tucumán classic, in sanguchero bread) and Tucumán empanadas. That, before any “auteur” restaurant. Look for neighbourhood sandwich shops.",
            "hack": "Easy to chain with Santiago del Estero or Salta. I am not locking a named operator for Tafí/Quilmes: car or a local agency, and a vehicle that can handle the climb.",
        },
        "legs_es": [("bus", "Micro ~14–16 h · noche"), ("air", "Avión ~2 h")],
        "legs_en": [("bus", "Bus ~14–16 h · overnight"), ("air", "Flight ~2 h")],
        "nearby": ["santiago-del-estero", "salta", "jujuy"],
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
        "nearby": ["tucuman", "cordoba", "salta"],
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
                "es": "Incluye tren ecológico y circuitos habilitados ese día. Comprá oficial; el parque no es la lancha.",
                "en": "Includes the ecological train and the circuits open that day. Buy official; the park ticket is not the boat.",
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
                "es": "Selva en vehículo abierto + lancha a los saltos. Restricciones de embarque. Entrada al parque aparte. Paseo Ecológico ~ARS 40.000 (a veces suspendido si cierran Garganta).",
                "en": "Open-vehicle jungle trail + boat to the falls. Boarding restrictions. Park ticket extra. Ecological boat ride ~ARS 40,000 (sometimes suspended if Garganta is closed).",
                "ars": 100000,
                "asof": "tickets.iguazujungle.com, nov. 2026",
                "asof_en": "tickets.iguazujungle.com, Nov 2026",
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
                "Monumento a la Bandera, costanera, islas frente a la ciudad.",
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
                "National Flag Memorial, the waterfront, islands across the river.",
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
            "where": "Sierras · universidad y fernet",
            "teaser": "Ciudad viva; el fin de semana se va a Carlos Paz o al valle.",
            "vibe": "Universidad, cuarteto, fernet con Coca y sierras a un rato. La ciudad es viva; el fin de semana se va a Carlos Paz o al valle.",
            "season": "La ciudad rinde casi todo el año; sierras mejor sep–nov y mar–may. Evitá enero en Carlos Paz (calor + muchedumbre). Invierno seco en la ciudad, frío de noche en las sierras.",
            "arrive": "Vuelo a COR (hub doméstico fuerte, ~1 h 20) o micro (~9–11 h) desde Retiro. Auto tiene sentido si vas a las sierras varios días. Desde COR conectás Mendoza y el NOA sin volver a Ezeiza.",
            "do": [
                "Centro histórico y Manzana Jesuítica (UNESCO).",
                "Sierras Chicas o Calamuchita.",
                "Camino de las Altas Cumbres si manejás con calma.",
                "Parque Nacional Quebrada del Condorito si el plan es sierras de verdad.",
            ],
            "eat": "Fernet con Coca (sí, es cultural), locro, empanadas cordobesas, asado. En las sierras, cabrito y comida de hostería.",
            "hack": "No vale Córdoba de a pie si lo que querías eran las sierras: alquilá o tomá combi. Empate clásico: cama nocturno vs vuelo corto.",
        },
        "en": {
            "name": "Córdoba",
            "where": "Sierras · university city and fernet",
            "teaser": "A living city; the weekend leaves for Carlos Paz or the valley.",
            "vibe": "University, cuarteto, fernet and Coke, and sierras a short hop away. The city is alive; the weekend leaves for Carlos Paz or the valley.",
            "season": "The city works almost year-round; the sierras are better Sep–Nov and Mar–May. Avoid January in Carlos Paz (heat + crowds). Winter is dry in town, cold at night in the hills.",
            "arrive": "Fly to COR (a real domestic hub, ~1 h 20) or bus (~9–11 h) from Retiro. A car makes sense if you are spending several days in the sierras. From COR you can connect Mendoza and the northwest without going back to Ezeiza.",
            "do": [
                "Historic centre and the Jesuit Block (UNESCO).",
                "Sierras Chicas or Calamuchita.",
                "Camino de las Altas Cumbres if you drive calmly.",
                "Quebrada del Condorito National Park if the plan is actual hills.",
            ],
            "eat": "Fernet and Coke (yes, it is cultural), locro, Córdoba empanadas, asado. In the sierras, goat and inn food.",
            "hack": "Skip a car-free Córdoba if what you wanted was the sierras: rent or take a combi. Classic tie: overnight cama bus vs a short flight.",
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
                "note_es": "tarifa general",
                "note_en": "general fee",
            }
        ],
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
                "Palermo (parques, bares), San Telmo (feria domingo), Recoleta (cementerio, museos).",
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
                "Palermo (parks, bars), San Telmo (Sunday fair), Recoleta (cemetery, museums).",
                "Puerto Madero for the photo, La Boca briefly with your things zipped.",
                "Free walking tours at Plaza de Mayo/San Telmo (tip). Tango in a real milonga if you are up for it, not only a dinner show.",
            ],
            "eat": "Parrilla (Don Julio in Palermo, book ahead), bodegón (El Preferido de Palermo), thick-crust pizza at Güerrín, historic cafés Tortoni and Los 36 Billares, choripán at fairs (La Choripanería in Mercado de San Telmo). Dulce de leche ice cream at any serious heladería.",
            "hack": "Tigre ~50 min on the Mitre train from Retiro (~ARS 790 with a registered SUBE, Oct 2026). La Plata ~1 h 16 from Constitución. San Antonio de Areco ~2 h. Tandil is not a day trip. Montevideo: there is an overnight EGA bus, not only Buquebus — see the hub hacks.",
        },
        "legs_es": [("local", "Estás acá"), ("air", "AEP 20–40 min · EZE 45–75 min")],
        "legs_en": [("local", "You are here"), ("air", "AEP 20–40 min · EZE 45–75 min")],
        "nearby": ["buenos-aires", "entre-rios", "santa-fe"],
        "tours": [],
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
                "url": "https://troutandwine.com/",
                "es_name": "Trout & Wine (wine tours chicos)",
                "en_name": "Trout & Wine (small wine tours)",
                "es": "Operador conocido, inglés/español. También podés ir directo a bodegas con reserva. En Maipú, bici + remís de vuelta es el clásico económico. No publico un precio que no esté en su tarifa del día.",
                "en": "A known operator, English/Spanish. You can also go straight to wineries with a booking. In Maipú, bike + a remise back is the cheap classic. I am not inventing a day rate that is not on their sheet.",
                "ars": None,
                "asof": "confirmá en troutandwine.com",
                "asof_en": "confirm at troutandwine.com",
                "note_es": "varía con bodegas y grupo",
                "note_en": "moves with wineries and group size",
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
                "url": "https://www.hydrosport.ar/",
                "es_name": "Hydro Sport (avistaje embarcado)",
                "en_name": "Hydro Sport (boat-based watching)",
                "es": "Avistaje de ballenas desde Pirámides y salidas de delfines desde Madryn (estacional; a veces cierran venta). Hay otras lanchas en el muelle: compará y no persigas a los animales. El embarcado se paga aparte de la entrada al área protegida. Confirmá tarifa en su web.",
                "en": "Whale watching from Pirámides and dolphin trips from Madryn (seasonal; they sometimes stop selling). Other boats at the pier: compare, and do not chase the animals. The boat is extra to the protected-area ticket. Confirm the fare on their site.",
                "ars": None,
                "asof": "confirmá en hydrosport.ar",
                "asof_en": "confirm at hydrosport.ar",
                "note_es": "estacional; el puerto cierra con viento",
                "note_en": "seasonal; the port closes in wind",
            },
            {
                "url": "https://www.argentina.gob.ar/turismo",
                "es_name": "Entrada Península Valdés (área protegida)",
                "en_name": "Península Valdés protected-area ticket",
                "es": "Entrada 2026 al área protegida, no incluye lancha.",
                "en": "2026 protected-area ticket, boat extra.",
                "ars": 50000,
                "asof": "temporada 2026",
                "asof_en": "2026 season",
                "note_es": "extranjeros; residentes ~ARS 20.000",
                "note_en": "foreign visitors; residents ~ARS 20,000",
            },
        ],
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
                "es": "El parque alrededor de Bariloche. Entrada oficial; Circuito Chico se hace en auto, bici o bus turístico.",
                "en": "The park around Bariloche. Official gate fee; Circuito Chico is car, bike, or tourist bus.",
                "ars": APN["nahuel"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; nacionales ~ARS 15.000",
                "note_en": "general fee; Argentine residents ~ARS 15,000",
            },
            {
                "url": "https://www.cruceandino.com/",
                "es_name": "Cruce Andino (tres lagos)",
                "en_name": "Cruce Andino (three lakes)",
                "es": "Nahuel Huapi, Frías, Todos los Santos. No es un micro. Parques y almuerzo aparte. Sale casi todos los días; el clima en el lago manda.",
                "en": "Nahuel Huapi, Frías, Todos los Santos. It is not a bus. Parks and lunch extra. It runs most days; lake weather decides.",
                "ars": None,
                "usd_only": "USD 355 no residente / 277 residente",
                "usd_only_en": "USD 355 non-resident / 277 resident",
                "asof": "tarifa 2026–28",
                "asof_en": "2026–28 fare",
                "note_es": "publicado por el operador",
                "note_en": "published by the operator",
            },
        ],
    },
    {
        "slug": "santa-cruz",
        "region": "patagonia",
        "es": {
            "name": "Santa Cruz",
            "where": "Patagonia de hielo · El Calafate",
            "teaser": "Pueblo-base para el Perito Moreno. El Chaltén es otro viaje (yo no lo marqué como visitado).",
            "vibe": "Pueblo-base para el Perito Moreno. El glaciar es el motivo; el pueblo es viento, souvenir y cordero. El trekking largo es Chaltén: yo no lo marqué como visitado acá.",
            "season": "El Perito Moreno «funciona» casi todo el año. Ideal nov–mar para luz (y Chaltén cerca). Evitá may–ago si querés trekking largo: frío, pocas horas de luz, algunas salidas se cortan. Enero es caro y lleno.",
            "arrive": "Vuelo a FTE (~3 h). No hay micro directo razonable desde Buenos Aires: si no volás, es un odisea de combinaciones.",
            "do": [
                "Pasarelas del glaciar (imprescindible) + entrada al parque.",
                "Navegación frente a la pared o trekking sobre hielo si estás en forma.",
                "El Chaltén queda a ~2 h 40 / 215 km si seguís (yo no lo marqué).",
            ],
            "eat": "Cordero patagónico, calafate en dulce o helado, trucha. Porciones de refugio, no de degustación.",
            "hack": "Micros Cal Tur / Chaltén Travel / TAQSA a El Chaltén, ~ARS 70.000 / ~USD 45 el tramo (oct. 2026) + tasa de terminal. Reservá 2–3 noches en Chaltén después del Perito Moreno. No es day trip de trekking.",
        },
        "en": {
            "name": "Santa Cruz",
            "where": "Ice Patagonia · El Calafate",
            "teaser": "Base town for Perito Moreno. El Chaltén is another trip (I did not mark it as visited).",
            "vibe": "Base town for Perito Moreno. The glacier is the reason; the town is wind, souvenirs, and lamb. The long trekking is El Chaltén: I did not mark it as visited here.",
            "season": "Perito Moreno “works” most of the year. Ideal Nov–Mar for daylight (and Chaltén nearby). Avoid May–Aug if you want long treks: cold, short days, some outings get cut. January is expensive and packed.",
            "arrive": "Fly to FTE (~3 h). There is no reasonable direct bus from Buenos Aires: if you don’t fly, it is a multi-day odyssey.",
            "do": [
                "Glacier boardwalks (non-negotiable) plus the park ticket.",
                "A boat along the wall, or ice trekking if you are fit.",
                "El Chaltén is ~2 h 40 / 215 km if you continue (I did not mark it).",
            ],
            "eat": "Patagonian lamb, calafate in jam or ice cream, trout. Mountain-refuge portions, not a tasting menu.",
            "hack": "Cal Tur / Chaltén Travel / TAQSA buses to El Chaltén, ~ARS 70,000 / ~USD 45 (Oct 2026) plus terminal tax. Book 2–3 nights in Chaltén after Perito Moreno. Not a trekking day trip.",
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
                "es": "Concesionaria del parque. Minitrekking todo el año; Big Ice 15 sep–30 abr (ARS 550.000 + traslado opcional). Safari Náutico ARS 80.000 todo el año. Parque aparte.",
                "en": "Park concessionaire. Mini trekking year-round; Big Ice 15 Sep–30 Apr (ARS 550,000 + optional transfer). Nautical safari ARS 80,000 year-round. Park extra.",
                "ars": 420000,
                "asof": "hieloyaventura.com desde 1 nov 2026",
                "asof_en": "hieloyaventura.com from 1 Nov 2026",
                "note_es": "adulto, sin traslado (con traslado ARS 500.000)",
                "note_en": "adult, without transfer (ARS 500,000 with transfer)",
            },
        ],
    },
    {
        "slug": "tierra-del-fuego",
        "region": "patagonia",
        "es": {
            "name": "Tierra del Fuego",
            "where": "El fin del mundo · Ushuaia",
            "teaser": "Montaña metida en el mar y viento que te ordena el pelo.",
            "vibe": "Montaña metida en el mar, viento que te ordena el pelo y una ciudad que vive del turismo y de ser el punto más austral que la mayoría va a pisar.",
            "season": "Trekking y Beagle: dic–mar. Ski: jun–ago. Evitá jun–jul si la idea es sendero: viento y ~7 h de luz. Abrigo todo el año.",
            "arrive": "Vuelo a USH (~3 h 30). Por tierra son dos días y un cruce: casi nadie lo hace de visita. El aeropuerto está pegado a la ciudad.",
            "do": [
                "Parque Nacional Tierra del Fuego.",
                "Canal Beagle (faros, lobos, cormoranes).",
                "Laguna Esmeralda, Cerro Martial. En invierno, ski; en verano, trekking largo.",
            ],
            "eat": "Centolla, merluza negra, cordero fueguino. Es caro comparado con el norte: el flete se siente.",
            "hack": "Ushuaia ↔ Punta Arenas: Bus-Sur / Tecni Austral, dos fronteras y un ferry de ~30 min por el Estrecho (Punta Delgada). ~USD 40–70 / CLP 58–68 mil (catálogo 2026). No hay ferry directo. No vale si tenés dos días en Ushuaia.",
        },
        "en": {
            "name": "Tierra del Fuego",
            "where": "The end of the world · Ushuaia",
            "teaser": "A mountain stuck in the sea, and wind that rearranges your hair.",
            "vibe": "A mountain stuck in the sea, wind that rearranges your hair, and a town that lives off tourism and being the southernmost point most people will ever stand on.",
            "season": "Trekking and the Beagle: Dec–Mar. Ski: Jun–Aug. Avoid Jun–Jul if the idea is a trail: wind and ~7 h of light. A jacket, every month.",
            "arrive": "Fly to USH (~3 h 30). Overland is two days and a border: almost nobody does it as a visit. The airport is next to town.",
            "do": [
                "Tierra del Fuego National Park.",
                "Beagle Channel (lighthouses, sea lions, cormorants).",
                "Laguna Esmeralda, Cerro Martial. In winter, skiing; in summer, long treks.",
            ],
            "eat": "King crab, black hake, Fuegian lamb. It is expensive compared with the north: you feel the freight.",
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
                "es": "El parque al oeste de la ciudad. Entrada oficial.",
                "en": "The park west of town. Official gate fee.",
                "ars": APN["tdf"],
                "asof": "APN desde 1 jun 2026",
                "asof_en": "APN from 1 Jun 2026",
                "note_es": "tarifa general; nacionales ARS 18.000",
                "note_en": "general fee; Argentine residents ARS 18,000",
            },
            {
                "url": "https://taunushuaia.com.ar/",
                "es_name": "Taun (guías de montaña locales)",
                "en_name": "Taun (local mountain guides)",
                "es": "Trekking, glaciar Vinciguerra, packrafting, Laguna Esmeralda. Para el Beagle, hay varias lanchas en el puerto: compará duración y si incluyen isla de pingüinos (estacional). Revisá el parte: el viento cancela. Confirmá tarifa con ellos.",
                "en": "Trekking, Vinciguerra glacier, packrafting, Laguna Esmeralda. For the Beagle, several boats at the port: compare length and whether penguin island is included (seasonal). Check the forecast: wind cancels. Confirm their fare with them.",
                "ars": None,
                "asof": "confirmá en taunushuaia.com.ar",
                "asof_en": "confirm at taunushuaia.com.ar",
                "note_es": "sale según clima",
                "note_en": "runs depend on weather",
            },
        ],
    },
]

NOT_YET = [
    ("Catamarca", "NOA vecino de Salta/Tucumán; yo todavía no.", "Northwest neighbour of Salta/Tucumán; not yet for me."),
    ("Chaco", "Impenetrable y resistencia chaqueña: aún no.", "Impenetrable forest and Resistencia: not yet."),
    ("Corrientes", "Esteros e Iberá; carnaval. Aún no pisé.", "Esteros and Iberá; carnival. I have not been."),
    ("Formosa", "Frontera norte. Aún no.", "Northern border. Not yet."),
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
    asof = t["asof_en"] if lang == "en" else t["asof"]
    note = t["note_en"] if lang == "en" else t["note_es"]
    if t.get("usd_only"):
        price = t["usd_only_en"] if lang == "en" else t["usd_only"]
        price_line = f"{price} · {note}"
    elif t.get("ars"):
        price_line = f"ARS {t['ars']:,} / {usd(t['ars'])} · {note}".replace(",", ".")
        if lang == "en":
            price_line = f"ARS {t['ars']:,} / {usd(t['ars'])} · {note}".replace(",", ",")
            # English uses 60,000
            price_line = f"ARS {t['ars']:,} / {usd(t['ars'])} · {note}"
    else:
        price_line = note
    url = t["url"]
    label = "Sitio" if lang != "en" else "Site"
    return f"""        <article class="tour">
          <h3><a href="{url}" rel="noopener">{name}</a></h3>
          <p>{body}</p>
          <p class="price">{price_line} <span class="asof">({asof})</span></p>
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
        fx = "USD al ~ARS 1.550 (BNA, nov. 2026). El peso se mueve: usá el número para saber si es un café o un sueldo."
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
        fx = "USD at ~ARS 1,550 (BNA, Nov 2026). Pesos move: use the number to know whether you are talking about a coffee or a salary."
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
      <a href="#hacer">{toc_do}</a>
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
    es_hub = (ROOT / "index.html").read_text(encoding="utf-8")
    if 'id="lugares"' in es_hub:
        patch_hub(ROOT / "index.html", "es")
        patch_hub(ROOT / "en" / "index.html", "en")
        print(f"wrote {len(PROVINCES)} provinces × 2 + patched hubs")
    else:
        print(f"wrote {len(PROVINCES)} provinces × 2 (hubs already split)")


if __name__ == "__main__":
    main()
