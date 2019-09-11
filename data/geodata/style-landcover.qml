<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.4.6-Madeira" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" minScale="1e+08" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <rasterrenderer type="paletted" band="1" opacity="1" alphaBand="-1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry value="-999" alpha="255" color="#404040" label="Fora do Amazonas"/>
        <paletteEntry value="1" alpha="255" color="#dcf064" label="Agricultura anual"/>
        <paletteEntry value="2" alpha="255" color="#a80ee6" label="Área não observada"/>
        <paletteEntry value="3" alpha="255" color="#006400" label="Floresta"/>
        <paletteEntry value="4" alpha="255" color="#b0cc67" label="Mosaico de ocupações"/>
        <paletteEntry value="5" alpha="255" color="#fff5d7" label="Pasto limpo"/>
        <paletteEntry value="6" alpha="255" color="#563c10" label="Pasto sujo"/>
        <paletteEntry value="7" alpha="255" color="#af2a2a" label="Área urbana"/>
        <paletteEntry value="8" alpha="255" color="#6ebaf0" label="Vegetação secundária"/>
        <paletteEntry value="9" alpha="255" color="#d0377c" label="Regeneração com pasto"/>
        <paletteEntry value="10" alpha="255" color="#ff7b00" label="Outros"/>
        <paletteEntry value="11" alpha="255" color="#0046c8" label="Hidrografia"/>
        <paletteEntry value="12" alpha="255" color="#f3fd28" label="Mineração"/>
        <paletteEntry value="15" alpha="255" color="#d23f3f" label="Não floresta"/>
      </colorPalette>
      <colorramp type="randomcolors" name="[source]"/>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation saturation="0" colorizeStrength="100" grayscaleMode="0" colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
