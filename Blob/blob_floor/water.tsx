<?xml version="1.0" encoding="UTF-8"?>
<tileset name="water" tilewidth="32" tileheight="32" tilecount="9" columns="3">
 <grid orientation="orthogonal" width="1" height="1"/>
 <terraintypes>
  <terrain name="Water" tile="4"/>
 </terraintypes>
 <tile id="0" terrain=",,,0">
  <image width="32" height="32" source="water_top_left.jpg"/>
 </tile>
 <tile id="1" terrain=",,0,0">
  <image width="32" height="32" source="water_top.jpg"/>
 </tile>
 <tile id="2" terrain=",,0,">
  <image width="32" height="32" source="water_top_right.jpg"/>
 </tile>
 <tile id="3" terrain=",0,,0">
  <image width="32" height="32" source="water_left.jpg"/>
 </tile>
 <tile id="4">
  <image width="32" height="32" source="water.jpg"/>
 </tile>
 <tile id="5" terrain="0,,0,">
  <image width="32" height="32" source="water_right.jpg"/>
 </tile>
 <tile id="6" terrain=",0,,">
  <image width="32" height="32" source="water_bottom_left.jpg"/>
 </tile>
 <tile id="7" terrain="0,0,,">
  <image width="32" height="32" source="water_bottom.jpg"/>
 </tile>
 <tile id="8" terrain="0,,,">
  <image width="32" height="32" source="water_bottom_right.jpg"/>
 </tile>
</tileset>
