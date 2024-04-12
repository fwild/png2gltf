# png2gltf

> [!NOTE]  
> Nifty little commandline tool for converting flat png images to 3D objects (circle/triangle/rectangle signs) using bash, python, and blender

Author: Prof Dr Fridolin Wild (f.wild@open.ac.uk)

![image](https://github.com/fwild/png2gltf/assets/183296/3afbf566-2d01-4d4e-80c7-d93a8a31ed39)

This commandline script converts ISO 7010 warnings signs stored as PNG into gltf files using a blender project template for each shape type (circle, triangle, rectangle). The script first loads and places the iso sign into an according texture template to then exchange the material in the blender project file using code, before exporting it as gltf.

To convert to a 3D shape, a template Blender project is required. There are three basic shape templates provided (thin rectangular sign, thin round sign, thin rounded edge triangle sign). The Blender project uses the name "Cube.003" for these 3D shape objects, and has a material assigned to them with a texture. The shell script first uses `insertTextures.py` to mount the input image (from Wikipedia) onto the right spot on the associated UV-mapped texture, and then uses `BlenderConvert.py` to open the project, find the right 3D object, and create a new material with the according shader properties setup to link to the freshly created texture. For convenience, these temporary textures are all called `Cube.png`. Finally, `BlenderConvert.py` exports a gltf asset with the 3D object (see example outputs in `gltf/` and `zipped/`). Please note that the texture image insert is a bit fiddly: each type of warning sign expects that its associated PNGs share the same resolution, and they are resized and rotated to fit onto the front face of the sign, keeping the rest of the texture to whatever its according texture template foresees.

To run:

1. `chmod u+x BuildObjFromImage.sh`
2. set the `template`, `outimage`, and `blenderfile` in BuildObjFromImage.sh
3. the templates are: "triangle_template3.png", "cube_template.png"
4. outimage is always "Cube.png"
5. blenderfiles are: "triangle.blend", "shield.blend", "cube.blend"
2. `./BuildObjFromImage.sh pngs/*.png` 
