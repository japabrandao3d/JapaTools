import bpy

class VIEW3D_PT_my_custom_panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Japa Tools"
    bl_label = "Japa Tools"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Selection Tools")
        layout.operator("object.select_empty_meshes")
        layout.operator("mesh.select_sharp_edge_verts")

        layout.label(text="Renaming Tools")
        layout.operator("object.rename_with_material")
        layout.operator("object.batch_rename_selected")
        layout.operator("object.rename_data_blocks")

        layout.label(text="Data Transfer Tools")
        layout.prop(context.scene, "source_object")
        layout.prop(context.scene, "apply_first_vertex_group", text="Apply First Vertex Group")
        layout.operator("object.add_data_transfer_modifier")

        layout.label(text="(Beta) Utilities")
        layout.operator("object.join_by_material")
        layout.operator("object.gap_finder")
        layout.prop(context.scene, "gap_threshold")
