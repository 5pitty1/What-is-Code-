<?xml version="1.0" encoding="UTF-8"?>
<tileset name="path" tilewidth="32" tileheight="32" tilecount="9" columns="3">
 <grid orientation="orthogonal" width="1" height="1"/>
 <terraintypes>
  <terrain name="Path" tile="4"/>
 </terraintypes>
 <tile id="0" terrain=",,,0">
  <image width="32" height="32" source="path_top_left.PNG"/>
 </tile>
 <tile id="1" terrain=",,0,0">
  <image width="32" height="32" source="path_top.PNG"/>
 </tile>
 <tile id="2" terrain=",,0,">
  <image width="32" height="32" source="path_top_right.PNG"/>
 </tile>
 <tile id="3" terrain=",0,,0">
  <image width="32" height="32" source="path_left.PNG"/>
 </tile>
 <tile id="4">
  <image width="32" height="32" source="path.PNG"/>
 </tile>
 <tile id="5" terrain="0,,0,">
  <image width="32" height="32" source="path_right.PNG"/>
 </tile>
 <tile id="6" terrain=",0,,">
  <image width="32" height="32" source="path_bottom_left.PNG"/>
 </tile>
 <tile id="7" terrain="0,0,,">
  <image width="32" height="32" source="path_bottom.PNG"/>
 </tile>
 <tile id="8" terrain="0,,,">
  <image width="32" height="32" source="path_bottom_right.PNG"/>
 </tile>
</tileset>
