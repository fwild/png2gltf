# png2gltf

Nifty little commandline tool for converting flat png images to 3D objects (circle/triangle/rectangle signs) using bash, python, and blender

Author: Prof Dr Fridolin Wild (f.wild@open.ac.uk)

This commandline script converts ISO 7010 warnings signs stored as PNG into gltf files using a blender project template for each shape type (circle, triangle, rectangle). The script first loads and places the iso sign into an according texture template to then exchange the material in the blender project file using code, before exporting it as gltf.

To run:

1. `chmod u+x BuildObjFromImage.sh`
2. set the `template`, `outimage`, and `blenderfile` in BuildObjFromImage.sh
3. the templates are: "triangle_template3.png", "cube_template.png"
4. outimage is always "Cube.png"
5. blenderfiles are: "triangle.blend", "shield.blend", "cube.blend"
2. `./BuildObjFromImage.sh pngs/*.png` 
