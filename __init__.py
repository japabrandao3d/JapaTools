bl_info = {
    "name": "Japa Tools",
    "author": "Gustavo (Japa) Franco and Félix (Flix) Devost",
    "version": (0, 1, 2),
    "blender": (4, 4, 0),
    "location": "3D Viewport > Sidebar > Japa Tools",
    "description": "A simple interface that groups together small python scripts that I think are great for speeding up tasks, I hope you like it",
    "category": "Development",
}

import bpy
from . import properties
from . import panel
from .operators import (
    rename_data_blocks,
    rename_with_material,
    select_sharp_edge_verts,
    select_empty_meshes,
    batch_rename_selected,
    add_data_transfer_modifier,
    gap_finder,
    join_by_material,
)

classes = (
    rename_data_blocks.OBJECT_OT_rename_data_blocks,
    rename_with_material.OBJECT_OT_rename_object_with_material,
    select_sharp_edge_verts.MESH_OT_select_sharp_edge_verts,
    select_empty_meshes.OBJECT_OT_select_empty_meshes,
    batch_rename_selected.OBJECT_OT_batch_rename_selected,
    add_data_transfer_modifier.OBJECT_OT_add_data_transfer_modifier,
    gap_finder.OBJECT_OT_gap_finder,
    join_by_material.OBJECT_OT_join_by_material,
    panel.VIEW3D_PT_my_custom_panel,
)

def register():
    properties.add_scene_properties()
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    properties.remove_scene_properties()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()