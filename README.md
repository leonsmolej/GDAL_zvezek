# GDAL – zapiski in primeri ukazov

Jupyter notebook z osebnimi zapiski o delu z orodji [GDAL/OGR](https://gdal.org/en/stable/). Zapiski so v slovenščini, ukazi pa so pripravljeni tako, da jih lahko poženete neposredno v celicah (`!ukaz`).

## Vsebina

- **Osnovno procesiranje rastrov**: `gdalinfo`, virtualni rastri (`gdalbuildvrt`), pretvorba formatov, stiskanje, NoData, Cloud Optimized GeoTIFF
- **Višinski podatki**: hillshade, multidirectional hillshade, barvni relief
- **Aerofotografije**: mozaik, izrez na območje zanimanja, overviews (piramide)
- **Satelitski posnetki (Landsat 8)**: RGB kompozit, razteg histograma, pan-sharpening
- **Rasterska algebra**: `gdal_calc.py`, reklasifikacija, NDVI
- **WMS**: dostop do spletnih slojev in prenos
- **Georeferenciranje**: z robnimi koordinatami in z GCP točkami
- **OGR (vektorji)**: `ogrinfo`, `ogr2ogr`, SQL poizvedbe, združevanje datotek, prostorske poizvedbe
- **Batch procesiranje** s Pythonom (tudi z več jedri)

## Zahteve

- Python 3 in Jupyter
- GDAL (priporočeno prek conda):

```bash
conda create -n gdal -c conda-forge gdal jupyter
conda activate gdal
jupyter notebook GDAL.ipynb
```

## Podatki

Podatki niso del repozitorija. Uporabljeni podatki so iz tečaja [GDAL Tools](https://courses.spatialthoughts.com/gdal-tools.html) (Spatial Thoughts), kjer jih lahko prenesete. Primeri uporabljajo:

- SRTM višinske podatke (`.hgt`)
- NAIP aerofotografije (`.jp2`)
- Landsat 8 posnetke
- `worldcities.csv`, potresne podatke (`.geojson`) in druge vzorčne datoteke

Poti v notebooku (npr. `C:\KODA\GDAL\...`) prilagodite svojim.

## Opombe

- Nekateri ukazi (`dir`, `%CONDA_PREFIX%\Scripts\...`) so za **Windows**. Na Linuxu ali macOS jih zamenjajte z `ls` in `$CONDA_PREFIX/bin/...`.
- To so učni zapiski, ne uradna dokumentacija. Za natančne opcije glejte [gdal.org](https://gdal.org/en/stable/).
- Zapiski so nastali ob spremljanju tečaja [GDAL Tools](https://courses.spatialthoughts.com/gdal-tools.html) (Spatial Thoughts). Vsa zasluga za vsebino in učne podatke gre avtorjem tečaja.


