import os
import bpy

# Function to search for .fbx files recursively in the folder and subfolders
def search_fbx_files(folder):
    fbx_files = []
    
    # Check if the directory exists
    if not os.path.exists(folder):
        print(f"Error: The folder path '{folder}' does not exist.")
        return fbx_files  # Return empty list if folder doesn't exist
    
    # Walk through the directory and collect .fbx files
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.lower().endswith(".fbx"):  # Case insensitive check
                fbx_files.append(os.path.join(root, filename))
    
    if not fbx_files:
        print("No .fbx files found.")
    return fbx_files

# Function to globally remove actions containing a specific keyword
def remove_actions_with_keyword(keyword):
    for action in bpy.data.actions:
        if keyword in action.name:
            print(f"Removing action: {action.name}")
            bpy.data.actions.remove(action, do_unlink=True)

# Specify the folder path
folder_path = r"C:\Users\Asus\Desktop\animations\LocomotionWalk"  # Change this to your folder path

# Get all the .fbx files from the folder and subfolders
fbx_files = search_fbx_files(folder_path)

# Loop through each .fbx file and import it
for file_path in fbx_files:
    # Save the state of objects before import to identify the newly imported ones
    objects_before_import = set(bpy.context.view_layer.objects)

    # Import the .fbx file
    bpy.ops.import_scene.fbx(filepath=file_path)

    # Identify the newly imported objects
    new_objects = set(bpy.context.view_layer.objects) - objects_before_import

    # If there are new objects, rename their animation data and conditionally merge them
    if new_objects:
        # Collect objects with unique actions to merge if they don't exist already
        objects_to_merge = []

        for obj in new_objects:
            print(f"New object imported: {obj.name}")

            # Generate a unique action name based on the file path
            action_name = file_path.replace(folder_path, "").replace(os.path.sep, "_").strip("_").replace(".fbx", "").replace(".FBX", "")

            # Check if the action already exists
            if action_name in bpy.data.actions:
                # Reuse the existing action and do not merge this object
                existing_action = bpy.data.actions[action_name]
                if obj.animation_data:
                    obj.animation_data.action = existing_action
                print(f"Reusing existing action for {obj.name}: {action_name}")
            else:
                # Rename animation action if it doesn't exist
                if obj.animation_data and obj.animation_data.action:
                    new_action = obj.animation_data.action
                    new_action.name = action_name
                    print(f"Renamed action for {obj.name} to: {action_name}")
                    # Add the object to the list of objects to be merged
                    objects_to_merge.append(obj)
                else:
                    print(f"No animation data found for {obj.name}")

        # If there are objects to merge (only those with unique action names), proceed with merging
        if objects_to_merge:
            bpy.ops.object.select_all(action='DESELECT')  # Deselect everything first
            for obj in objects_to_merge:
                obj.select_set(True)
            bpy.ops.object.join()
            print("All new objects with unique action names merged into one.")

        # Remove objects starting with "root." or "SK_Mannequin."
        for obj in new_objects:
            if obj.name.startswith(("root.", "SK_Mannequin.")):
                print(f"Removing object: {obj.name}")
                bpy.data.objects.remove(obj, do_unlink=True)

        # Purge orphaned data to completely remove unused objects and actions
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

    else:
        print(f"No new objects imported for: {file_path}")

# Remove animations globally that contain "root." in their name
remove_actions_with_keyword("root.")

# Function to get the root object in the scene collection and bind all actions to it
def bind_actions_to_root():
    # Search for the root object in the scene collection
    root_object = bpy.context.scene.collection.objects.get("root")
    
    if root_object is None:
        print("No object named 'root' found in the scene.")
        return
    
    # Loop through all actions and assign them to the root object if it has animation data
    for action in bpy.data.actions:
        # If action is not already bound to the root object
        if root_object.animation_data and root_object.animation_data.action != action:
            print(f"Binding action {action.name} to 'root' object.")
            # Set the action to the root object
            root_object.animation_data.action = action
        elif not root_object.animation_data:
            # Create animation data if not already present on the root object
            print(f"Adding animation data to 'root' object for action {action.name}.")
            root_object.animation_data_create()
            root_object.animation_data.action = action

# Call the function to bind actions to the root object
bind_actions_to_root()

# Optionally, you can also add a cleanup step to remove the "root" object if no longer needed:
# bpy.data.objects.remove(root_object, do_unlink=True)
