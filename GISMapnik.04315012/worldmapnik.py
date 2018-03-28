import mapnik
m = mapnik.Map(800,400)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('white')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('green')	
line_symbolizer.stroke_width = 2.0

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('my project',s)

sumberdata = mapnik.Shapefile(file="/home/wahyushigemori/ne_110m_admin_0_countries.shp")
lapisan = mapnik.Layer('world')
lapisan.datasource = sumberdata
lapisan.styles.append('my project')
m.layers.append(lapisan)
m.zoom_all()
mapnik.render_to_file(m,'map.png', 'png')
print "rendered image to 'map.png'"
