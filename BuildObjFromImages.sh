#!/bin/bash

if [ "$1" ==  "--help" ] || [ "$1" == "-h" ] 
then
  echo -e "Usage: BuildObjFromImages.sh [switches] [--help/-h] file(s) template outimage blenderfile"
  echo -e "  --help / -h	this help text\n"
  echo -e "  Takes an input image of defined size 389x389 pixels and places it\n  onto a template texture to then integrate into a 3D standard shape obj model\n\n"
  exit
fi

template="triangle_template3.png" 
outimage="Cube.png"
blenderfile="triangle.blend"

for f in $@ ; 
do { 
   export filename="${f%.*}"
   echo "Processing texture (using template $template) into $outimage for image $f" 
   python insertTextures.py $template "$f" "$outimage" # template.png Cube.png
   # zip "$filename.zip" Cube.png cube.mtl cube.obj
   echo "Processing blender file $blenderfile and generating gltf with texture $outimage"
   /Applications/Blender.app/Contents/MacOS/Blender --background --python BlenderConvert.py -- $blenderfile $outimage exp.gltf 
   #cube.blend Cube.png exp.gltf
   echo "Copying gltf export to $filename"
   cp exp.gltf $filename.gltf
}
done

