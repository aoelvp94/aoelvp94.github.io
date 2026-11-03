(function () {
  const LANG = (document.documentElement.lang || "es").toLowerCase().startsWith("en") ? "en" : "es";
  const ROOT = document.documentElement.getAttribute("data-guide-root") || "./";
  const t = LANG === "en"
    ? {
        visited: "Visited by Aldo",
        notYet: "Not yet",
        click: "Click a pin or a province",
        still: "Aldo has not been here yet"
      }
    : {
        visited: "Visitado por Aldo",
        notYet: "Aún no",
        click: "Tocá un pin o una provincia",
        still: "Aldo todavía no estuvo acá"
      };

  const PLACES = [
    { id: "jujuy", slug: "jujuy", lat: -24.1858, lon: -65.2995, labelEs: "Jujuy", labelEn: "Jujuy", dir: "right" },
    { id: "salta", slug: "salta", lat: -24.7829, lon: -65.4232, labelEs: "Salta", labelEn: "Salta", dir: "left" },
    { id: "tucuman", slug: "tucuman", lat: -26.8083, lon: -65.2176, labelEs: "Tucumán", labelEn: "Tucumán", dir: "left" },
    { id: "santiago", slug: "santiago-del-estero", lat: -27.7834, lon: -64.2642, labelEs: "Sgo. Estero", labelEn: "Sgo. Estero", dir: "right" },
    { id: "misiones", slug: "misiones", lat: -25.5972, lon: -54.5786, labelEs: "Iguazú", labelEn: "Iguazú", dir: "right" },
    { id: "entre-rios", slug: "entre-rios", lat: -31.7319, lon: -60.5238, labelEs: "E. Ríos", labelEn: "E. Ríos", dir: "top" },
    { id: "rosario", slug: "santa-fe", lat: -32.9442, lon: -60.6505, labelEs: "Rosario", labelEn: "Rosario", dir: "right" },
    { id: "cordoba", slug: "cordoba", lat: -31.4201, lon: -64.1888, labelEs: "Córdoba", labelEn: "Córdoba", dir: "left" },
    { id: "caba", slug: "caba", lat: -34.6037, lon: -58.3816, labelEs: "CABA", labelEn: "CABA", dir: "left" },
    { id: "pba", slug: "buenos-aires", lat: -34.9214, lon: -57.9544, labelEs: "PBA", labelEn: "PBA", dir: "right" },
    { id: "mdp", slug: "buenos-aires", hash: "mar-del-plata", lat: -38.0055, lon: -57.5426, labelEs: "MdP", labelEn: "MdP", dir: "right" },
    { id: "mendoza", slug: "mendoza", lat: -32.8895, lon: -68.8458, labelEs: "Mendoza", labelEn: "Mendoza", dir: "left" },
    { id: "madryn", slug: "chubut", lat: -42.7692, lon: -65.0385, labelEs: "Madryn", labelEn: "Madryn", dir: "right" },
    { id: "bariloche", slug: "rio-negro", lat: -41.1335, lon: -71.3103, labelEs: "Bariloche", labelEn: "Bariloche", dir: "left" },
    { id: "calafate", slug: "santa-cruz", lat: -50.3379, lon: -72.2648, labelEs: "Calafate", labelEn: "Calafate", dir: "right" },
    { id: "ushuaia", slug: "tierra-del-fuego", lat: -54.8019, lon: -68.3030, labelEs: "Ushuaia", labelEn: "Ushuaia", dir: "right" }
  ];

  const FIRST_PLACE = {
    "02": "caba",
    "06": "buenos-aires",
    "14": "cordoba",
    "26": "chubut",
    "30": "entre-rios",
    "38": "jujuy",
    "50": "mendoza",
    "54": "misiones",
    "62": "rio-negro",
    "66": "salta",
    "78": "santa-cruz",
    "82": "santa-fe",
    "86": "santiago-del-estero",
    "90": "tucuman",
    "94": "tierra-del-fuego"
  };

  function goProvince(slug, hash) {
    if (!slug) return;
    const url = ROOT + slug + "/" + (hash ? "#" + hash : "");
    window.location.href = url;
  }

  window.jumpToArgentinaPlace = function (id) {
    const place = PLACES.find((p) => p.id === id);
    if (place) goProvince(place.slug, place.hash);
  };

  const mapEl = document.getElementById("map");
  if (!mapEl || typeof L === "undefined") return;

  const scriptSrc = document.currentScript && document.currentScript.src
    ? document.currentScript.src
    : new URL("map.js", window.location.href).href;
  const geoUrl = new URL("provincias.geojson", scriptSrc).href;

  const map = L.map(mapEl, {
    zoomControl: true,
    minZoom: 3,
    maxZoom: 9,
    worldCopyJump: false,
    zoomSnap: 0.25,
    attributionControl: true
  });

  function baseStyle(feature) {
    if (feature.properties.visited) {
      return { color: "#1d4ed8", weight: 0.8, fillColor: "#3b82f6", fillOpacity: 0.88 };
    }
    return { color: "#243246", weight: 0.45, fillColor: "#1c2b3a", fillOpacity: 0.9 };
  }

  fetch(geoUrl)
    .then((r) => {
      if (!r.ok) throw new Error("geojson " + r.status);
      return r.json();
    })
    .then((geo) => {
      const layer = L.geoJSON(geo, {
        style: baseStyle,
        onEachFeature: (f, shape) => {
          const name = LANG === "en" ? (f.properties.nameEn || f.properties.name) : f.properties.name;
          const status = f.properties.visited ? t.visited : t.notYet;
          shape.bindTooltip(`${name} · ${status}`, { sticky: true, className: "tip", opacity: 1 });
          shape.on("mouseover", () => {
            shape.setStyle({ weight: 1.6, fillOpacity: 1, color: "#fff" });
            shape.bringToFront();
          });
          shape.on("mouseout", () => shape.setStyle(baseStyle(f)));
          shape.on("click", () => {
            if (f.properties.visited) {
              const slug = FIRST_PLACE[f.properties.id];
              if (slug) goProvince(slug);
            }
          });
        }
      }).addTo(map);

      map.fitBounds(layer.getBounds(), { padding: [20, 20], maxZoom: 4.6, animate: false });
      map.invalidateSize();

      PLACES.forEach((place) => {
        const label = LANG === "en" ? place.labelEn : place.labelEs;
        const marker = L.circleMarker([place.lat, place.lon], {
          radius: 7,
          color: "#fff",
          weight: 2,
          fillColor: "#60a5fa",
          fillOpacity: 1
        }).addTo(map);
        marker.bindTooltip(label, {
          permanent: true,
          direction: place.dir || "right",
          offset: [6, 0],
          className: "pin-label",
          opacity: 1
        });
        marker.on("click", () => goProvince(place.slug, place.hash));
      });
    })
    .catch(() => {
      mapEl.replaceChildren();
      const p = document.createElement("p");
      p.style.cssText = "margin:0;padding:24px;color:#9fb0c2;";
      p.textContent = t.click;
      mapEl.appendChild(p);
    });
})();
