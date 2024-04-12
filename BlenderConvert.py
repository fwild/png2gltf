import bpy
import sys
import bmesh

argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "--"

obj_in = argv[0]
txt_in = argv[1]
f_out = argv[2]

#bpy.ops.import_scene.obj(filepath=obj_in, axis_forward='-Z', axis_up='Y')
bpy.ops.wm.open_mainfile(filepath=obj_in)
#bpy.ops.import_scene.gltf(filepath=obj_in)

objs = bpy.data.objects
if (objs and len(objs) > 0 and "Cube" in objs): objs.remove(objs["Cube"], do_unlink=True)
if ("Cube.003" in bpy.data.objects): print("FOUND")

mat = bpy.data.materials.new(name=txt_in+"_material")
#mat = bpy.data.objects["Cube.003"].material_slots[0].material
mat.use_nodes = True

bsdf = mat.node_tree.nodes["Principled BSDF"]

texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
texImage.image = bpy.data.images.load(txt_in, check_existing=False)
bpy.data.images[txt_in].reload()

mat.node_tree.links.new(texImage.outputs[0], bsdf.inputs["Base Color"])
bpy.data.objects["Cube.003"].material_slots[0].material = mat

material_output = mat.node_tree.nodes.get("Material Output")
mat.node_tree.links.new(bsdf.outputs["BSDF"], material_output.inputs["Surface"])

#if objs["Cube.003"].data.materials:
#objs["Cube.003"].data.materials[0] = mat
objs["Cube.003"].data.materials.append(mat)

print("Exporting to "+f_out)
#bpy.ops.export_scene.fbx(filepath=f_out, axis_forward='-Z', axis_up='Y', embed_textures=True)
bpy.ops.export_scene.gltf(filepath=f_out, export_materials="EXPORT", export_format="GLTF_EMBEDDED", export_yup=True)
