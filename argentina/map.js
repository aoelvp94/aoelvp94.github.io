(function () {
  const LANG = (document.documentElement.lang || "es").toLowerCase().startsWith("en") ? "en" : "es";
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
    { id: "jujuy", lat: -24.1858, lon: -65.2995, labelEs: "Jujuy", labelEn: "Jujuy", fullEs: "Jujuy", fullEn: "Jujuy", dir: "right" },
    { id: "salta", lat: -24.7829, lon: -65.4232, labelEs: "Salta", labelEn: "Salta", fullEs: "Salta", fullEn: "Salta", dir: "left" },
    { id: "tucuman", lat: -26.8083, lon: -65.2176, labelEs: "Tucumán", labelEn: "Tucumán", fullEs: "Tucumán", fullEn: "Tucumán", dir: "left" },
    { id: "santiago", lat: -27.7834, lon: -64.2642, labelEs: "Sgo. Estero", labelEn: "Sgo. Estero", fullEs: "Santiago del Estero", fullEn: "Santiago del Estero", dir: "right" },
    { id: "misiones", lat: -25.5972, lon: -54.5786, labelEs: "Iguazú", labelEn: "Iguazú", fullEs: "Misiones (Iguazú)", fullEn: "Misiones (Iguazú)", dir: "right" },
    { id: "entre-rios", lat: -31.7319, lon: -60.5238, labelEs: "E. Ríos", labelEn: "E. Ríos", fullEs: "Entre Ríos", fullEn: "Entre Ríos", dir: "top" },
    { id: "rosario", lat: -32.9442, lon: -60.6505, labelEs: "Rosario", labelEn: "Rosario", fullEs: "Rosario", fullEn: "Rosario", dir: "right" },
    { id: "cordoba", lat: -31.4201, lon: -64.1888, labelEs: "Córdoba", labelEn: "Córdoba", fullEs: "Córdoba", fullEn: "Córdoba", dir: "left" },
    { id: "caba", lat: -34.6037, lon: -58.3816, labelEs: "CABA", labelEn: "CABA", fullEs: "CABA", fullEn: "CABA", dir: "left" },
    { id: "pba", lat: -34.9214, lon: -57.9544, labelEs: "PBA", labelEn: "PBA", fullEs: "Buenos Aires (provincia)", fullEn: "Buenos Aires Province", dir: "right" },
    { id: "mdp", lat: -38.0055, lon: -57.5426, labelEs: "MdP", labelEn: "MdP", fullEs: "Mar del Plata", fullEn: "Mar del Plata", dir: "right" },
    { id: "mendoza", lat: -32.8895, lon: -68.8458, labelEs: "Mendoza", labelEn: "Mendoza", fullEs: "Mendoza", fullEn: "Mendoza", dir: "left" },
    { id: "madryn", lat: -42.7692, lon: -65.0385, labelEs: "Madryn", labelEn: "Madryn", fullEs: "Puerto Madryn", fullEn: "Puerto Madryn", dir: "right" },
    { id: "bariloche", lat: -41.1335, lon: -71.3103, labelEs: "Bariloche", labelEn: "Bariloche", fullEs: "Bariloche", fullEn: "Bariloche", dir: "left" },
    { id: "calafate", lat: -50.3379, lon: -72.2648, labelEs: "Calafate", labelEn: "Calafate", fullEs: "El Calafate", fullEn: "El Calafate", dir: "right" },
    { id: "ushuaia", lat: -54.8019, lon: -68.3030, labelEs: "Ushuaia", labelEn: "Ushuaia", fullEs: "Ushuaia", fullEn: "Ushuaia", dir: "right" }
  ];

  const FIRST_PLACE = {
    "02": "caba",
    "06": "pba",
    "14": "cordoba",
    "26": "madryn",
    "30": "entre-rios",
    "38": "jujuy",
    "50": "mendoza",
    "54": "misiones",
    "62": "bariloche",
    "66": "salta",
    "78": "calafate",
    "82": "rosario",
    "86": "santiago",
    "90": "tucuman",
    "94": "ushuaia"
  };

  function jumpToPlace(id) {
    const el = document.getElementById("lugar-" + id);
    if (!el) return;
    document.querySelectorAll(".place-card.is-target").forEach((n) => n.classList.remove("is-target"));
    el.classList.add("is-target");
    el.scrollIntoView({ behavior: "smooth", block: "start" });
    if (history.replaceState) history.replaceState(null, "", "#lugar-" + id);
    window.setTimeout(() => el.classList.remove("is-target"), 2200);
  }

  window.jumpToArgentinaPlace = jumpToPlace;

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
              const id = FIRST_PLACE[f.properties.id];
              if (id) jumpToPlace(id);
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
        marker.on("click", () => jumpToPlace(place.id));
      });
    })
    .catch(() => {
      mapEl.replaceChildren();
      const p = document.createElement("p");
      p.style.cssText = "margin:0;padding:24px;color:#9fb0c2;";
      p.textContent = t.click;
      mapEl.appendChild(p);
    });

  document.querySelectorAll("[data-region-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const region = btn.getAttribute("data-region-filter");
      document.querySelectorAll("[data-region-filter]").forEach((b) => b.classList.toggle("active", b === btn));
      document.querySelectorAll(".place-card").forEach((card) => {
        const show = region === "all" || card.getAttribute("data-region") === region;
        card.hidden = !show;
      });
    });
  });

  if (location.hash && location.hash.indexOf("#lugar-") === 0) {
    const id = location.hash.slice("#lugar-".length);
    window.setTimeout(() => jumpToPlace(id), 400);
  }
})();
