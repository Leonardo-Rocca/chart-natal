# chart-natal
App para crear dibujo de carta natal


- set environment
```
source venv/bin/activate
```

- execute backend
```
python carta_natal.py      
```

- execute UI

````
streamlit run app.py
````


## Architecture

The call chain is linear:

**`app.py`** → **`carta_natal.py`** → **`chart_draw.py`**

1. **`app.py`** — Streamlit UI. Password-gated. Sidebar collects birth data (name, city, country, date, time), language selector (`"Español"` / `"English"`), and background selector. Calls `generate_final_chart()`.

2. **`carta_natal.py`** — Astrology engine. Uses `pyswisseph` to compute planet longitudes and house cusps (Placidus), then calls `draw_chart_artistic()`. Entry point: `generate_final_chart()`. Imports `DEFAULT_LANGUAGE` from `chart_draw`.

3. **`chart_draw.py`** — Matplotlib rendering. Draws a polar chart on an A4 figure with a background image, then a bottom strip (`ax_bottom`) for the special points (Sol/Luna/Asc.). Key functions:
    - `draw_chart_artistic()` — main render pipeline
    - `draw_special_points()` — bottom panel with zodiac symbol + sign name + label for Sun, Moon, Ascendant
    - `get_sign_name(degrees, language)` — returns localized sign name using `SIGN_NAMES` dict
    - `zodiac_sign(degrees)` — returns unicode glyph (♈ etc.)

4. **`config.py`** — `Background` TypedDict, `FontID` enum, `BACKGROUNDS` list. Each background defines fonts and sizes for `title`, `subtitle`, `sign_name`, and `point_label`.

5. **`location.py`** — Geocoding via `geopy` + timezone lookup via `timezonefinder`/`pytz`.
