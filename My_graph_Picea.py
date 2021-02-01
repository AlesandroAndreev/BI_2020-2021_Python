import pandas as pd
import geoviews as gv
import geoviews.tile_sources as gvts
import holoviews as hv
from geoviews import dim, opts

gv.extension("bokeh") #Позволяет работать с точками

from bokeh.models import HoverTool

tooltips = [('Species', '@species'),
            ('Scientific name', '@scientificName'),
            ('Longitude', '$x'),
            ('Latitude', '$y')] # »нфо по наведении курсора

hover = HoverTool(tooltips=tooltips) #—ам курсор


colnames = ["scientificName","decimalLatitude","decimalLongitude","species"] #Ќазвание столбцов, которые извлечены из dataset

#Извлечение данных. [colnames] -нужные столбцы,dropna()-удаление пропусков.drop_duplicates - удаление повторов


way_to_obovata = input("Write way to picea obovata data: ")
way_to_obovata_vir = input("Write way to picea obovata vir data: ")
way_to_koriensis = input("Write way to picea koriensis data: ")
way_to_crassifolia = input("Write way to picea crassifolia data: ")
way_to_jezoensis = input("Write way to picea jezoensis data: ")
way_to_schrenkiana = input("Write way to picea schrenkiana data: ")
way_to_smithiana = input("Write way to picea smithiana vir data: ")


obovata = pd.read_csv(way_to_obovata,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
obovata_vir = pd.read_csv(way_to_obovata_vir,
                        sep=';', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
obovata = pd.merge(obovata, obovata_vir, how = 'outer')


koriensis = pd.read_csv(way_to_koriensis,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
crassifolia = pd.read_csv(way_to_crassifolia,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
jezoensis = pd.read_csv(way_to_jezoensis,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
schrenkiana = pd.read_csv(way_to_schrenkiana,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
smithiana = pd.read_csv(way_to_smithiana,
                        sep='\t', comment='#')[colnames].dropna().drop_duplicates(subset=colnames)
#Создаем цвет маркеров


obovata["color"]= '#2fd6af'
koriensis["color"]= '#000000'
crassifolia["color"]= '#c330da'
jezoensis["color"]= '#de339f'
schrenkiana["color"]= '#FFA500'
smithiana["color"]= '#d6ce2f'


obovata["marker"]= 'circle'
koriensis["marker"]= '+'
crassifolia["marker"]= '*'
jezoensis["marker"]= 'diamond'
schrenkiana["marker"]= 'triangle'
smithiana["marker"]= 'square'

#Сливаем несколько dataset в один
piceas = pd.merge(koriensis, crassifolia, how = 'outer')
piceas = pd.merge(piceas,jezoensis, how = 'outer')
piceas = pd.merge(piceas,schrenkiana, how = 'outer')
piceas = pd.merge(piceas,smithiana, how = 'outer')
piceas = pd.merge(piceas,obovata, how = 'outer')
piceas = pd.merge(piceas,abies, how = 'outer')


#создаем точечный график
piceas=hv.Dataset(piceas)
picea_gv_points = piceas.to(gv.Points, ["decimalLongitude", "decimalLatitude"],["scientificName", "species", "color", "marker"], groupby='species').overlay()


#Киргизия_площади

areas = obovata_vir = pd.read_csv(r"C:\Users\mac\Desktop\Picea_map\Kirg.csv",
                        sep=';', comment='#')

areas['colors'] = ['#DAA520','#DAA520','#ADFF2F','#00FF00','#00FF00','#00FFFF','#00FFFF','#00FFFF','#00FFFF']

areas = hv.Dataset(areas)
areas_gv_points = areas.to(gv.Points, ['Longitude', 'Latitude'],['Species', 'colors'], groupby='Species').overlay()

areas_gv_points.opts(opts.Points(size = 15,marker = "circle_x",color=dim("colors")))


#Наносим точечный график на карту (StamenTerrainRetina) + косметика

mapa = areas_gv_points*(gvts.StamenTerrainRetina*picea_gv_points).opts(
    opts.Points(width=1980, height=1080, alpha=0.6, hover_line_color="black",
                color=dim("color"), size = 10, tools=[hover],
                show_grid=False, hover_fill_alpha = 0.5,marker = dim("marker"),show_legend=True,title="Species graph of spruce in the territory of the Russian Federation and in neighboring regions"))

gv.renderer('bokeh').save(mapa, 'Picea_map')
