import os
import json
import customtkinter as ctk
from tkinter import ttk
from tkinter import filedialog, Menu

paths = [
    r"C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Data\Objects\Database\ShapeSets",
    r"C:\Program Files (x86)\Steam\steamapps\common\Scrap Mechanic\Survival\Objects\Database\ShapeSets"
]

sort_order = {}

def load_json_files():
    items = []
    for path in paths:
        for file in os.listdir(path):
            if file.endswith(".json"):
                with open(os.path.join(path, file), 'r') as f:
                    try:
                        data = json.load(f)
                        if "blockList" in data:
                            items.extend(data["blockList"])
                        if "partList" in data:
                            items.extend(data["partList"])
                    except json.JSONDecodeError:
                        continue
    return items

def search_items():
    search_term = search_entry.get().lower()
    filtered_items = []
    filtered_indices = []
    for index, item in enumerate(items):
        item_str_values = [
            str(item.get("name", "")).lower(),
            str(item.get("uuid", "")).lower(),
            str(item.get("legacyId", "")).lower(),
            str(item.get("color", "")).lower(),
            str(item.get("physicsMaterial", "")).lower(),
            str(item.get("flammable", "")).lower(),
            str(item.get("ratings", {}).get("density", "")).lower(),
            str(item.get("ratings", {}).get("durability", "")).lower(),
            str(item.get("ratings", {}).get("friction", "")).lower(),
            str(item.get("ratings", {}).get("buoyancy", "")).lower(),
            str(item.get("box", "")).lower(),
            str(item.get("scripted", "")).lower(),
            str(item.get("chest", "")).lower(),
            str(item.get("rotationSet", "")).lower(),
            str(item.get("sticky", "")).lower(),
        ]
        if any(search_term in value for value in item_str_values):
            filtered_items.append(item)
            filtered_indices.append(index)

    update_item_list(filtered_items, filtered_indices)

def update_item_list(filtered_items, filtered_indices):
    for row in tree.get_children():
        tree.delete(row)

    for index, item in enumerate(filtered_items):
        item_name = item.get("name", "Unnamed Item")
        uuid = item.get("uuid", "N/A")
        legacy_id = item.get("legacyId", "N/A")
        color = item.get("color", "N/A")
        material = item.get("physicsMaterial", "N/A")
        flammable = item.get("flammable", "N/A")
        density = item.get("ratings", {}).get("density", "N/A")
        durability = item.get("ratings", {}).get("durability", "N/A")
        friction = item.get("ratings", {}).get("friction", "N/A")
        buoyancy = item.get("ratings", {}).get("buoyancy", "N/A")
        box = f'{item.get("box", {}).get("x", "N/A")}x{item.get("box", {}).get("y", "N/A")}x{item.get("box", {}).get("z", "N/A")}'
        chest = item.get("chest", {}).get("slots", "N/A")
        rotation_set = item.get("rotationSet", "N/A")
        sticky = item.get("sticky", "N/A")
        scripted = item.get("scripted", {}).get("filename", "N/A")

        tree.insert("", ctk.END, values=(
            item_name, uuid, legacy_id, color, material, flammable, density, durability, friction, buoyancy, box, chest,
            rotation_set, sticky, scripted), tags=(str(filtered_indices[index]),))

def copy_to_clipboard(event):
    selected_item = tree.identify_row(event.y)
    selected_column = tree.identify_column(event.x)

    if selected_item:
        column_index = int(selected_column.replace("#", "")) - 1
        item_values = tree.item(selected_item, "values")
        selected_value = item_values[column_index]

        root.clipboard_clear()
        root.clipboard_append(selected_value)
        clipboard_label.configure(text=f"{selected_value} saved to clipboard")
        clipboard_label.after(2000, lambda: clipboard_label.configure(text=""))

def sort_by_column(column):
    global sort_order

    sort_order[column] = not sort_order.get(column, False)

    items = [(tree.set(child, column), child) for child in tree.get_children("")]

    try:
        items.sort(
            key=lambda item: convert_to_sortable(item[0]),
            reverse=sort_order[column]
        )
    except Exception as e:
        print(f"Error during sorting: {e}")

    for index, (_, child) in enumerate(items):
        tree.move(child, "", index)

def convert_to_sortable(value):
    if value in ["N/A", "", None]:
        return ""
    return str(value).lower()

def is_number(value):
    try:
        return float(value)
    except ValueError:
        return value

def toggle_column(column):
    if column_vars[column].get():
        tree.heading(column, text=column)
        tree.column(column, width=100, minwidth=20, stretch=True)
        current_columns.append(column)
    else:
        tree.heading(column, text="")
        tree.column(column, width=0, minwidth=0, stretch=False)
        current_columns.remove(column)

def show_column_menu(event):
    menu = Menu(root, tearoff=0)
    for col in columns:
        state = ctk.NORMAL if col in current_columns else ctk.DISABLED
        menu.add_checkbutton(label=col, onvalue=True, offvalue=False, variable=column_vars[col],
                             command=lambda c=col: toggle_column(c))
    menu.post(event.x_root, event.y_root)

def show_original_code():
    selected_items = tree.selection()
    if selected_items:
        selected_item = selected_items[0]
        original_index = int(tree.item(selected_item, "tags")[0])
        item_data = items[original_index]

        code_window = ctk.CTkToplevel(root)
        code_window.geometry('800x600')
        code_window.title("Original JSON Code")

        text_widget = ctk.CTkTextbox(code_window, wrap='word')
        text_widget.pack(fill='both', expand=True)

        json_data = json.dumps(item_data, indent=4)
        text_widget.insert('1.0', json_data)

        text_widget.configure(state='normal')

def save_items():
    save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if save_path:
        with open(save_path, 'w') as f:
            json.dump(items, f, indent=4)

def open_settings():
    settings_window = ctk.CTkToplevel(root)
    settings_window.geometry('400x300')
    settings_window.title("Settings")

    def save_paths():
        new_path1 = path_entry_1.get()
        new_path2 = path_entry_2.get()
        paths[0] = new_path1
        paths[1] = new_path2
        settings_window.destroy()

    path_label_1 = ctk.CTkLabel(settings_window, text="Path to Creative ShapeSets")
    path_label_1.pack(pady=5, padx=10, anchor="w")
    path_entry_1 = ctk.CTkEntry(settings_window, width=350)
    path_entry_1.insert(0, paths[0])
    path_entry_1.pack(pady=5, padx=10, fill="x")

    path_label_2 = ctk.CTkLabel(settings_window, text="Path to Survival ShapeSets")
    path_label_2.pack(pady=5, padx=10, anchor="w")
    path_entry_2 = ctk.CTkEntry(settings_window, width=350)
    path_entry_2.insert(0, paths[1])
    path_entry_2.pack(pady=5, padx=10, fill="x")

    save_button = ctk.CTkButton(settings_window, text="Save", command=save_paths)
    save_button.pack(pady=20)

items = load_json_files()
filtered_items = items

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Scrap Mechanic Item Database by Fabian Vinke")
root.geometry("1200x800")

search_frame = ctk.CTkFrame(root)
search_frame.pack(pady=10, padx=10, fill="x")
search_label = ctk.CTkLabel(search_frame, text="Search:")
search_label.pack(side="left", padx=5)
search_entry = ctk.CTkEntry(search_frame)
search_entry.pack(side="left", padx=5, fill="x", expand=True)
search_button = ctk.CTkButton(search_frame, text="Search", command=search_items)
search_button.pack(side="left", padx=5)

info_label = ctk.CTkLabel(root, text="Double-click to copy anything")
info_label.pack(pady=5)

columns = (
    "Name", "UUID", "Legacy ID", "Color", "Material", "Flammable", "Density", "Durability", "Friction",
    "Buoyancy", "Box", "Chest Slots", "Rotation Set", "Sticky", "Scripted"
)

current_columns = ["Name", "UUID", "Legacy ID", "Color", "Material", "Flammable", "Density", "Durability", "Friction",
    "Buoyancy", "Box", "Chest Slots", "Rotation Set", "Sticky", "Scripted"]

tree_frame = ctk.CTkFrame(root)
tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=20)
scrollbar_y = ctk.CTkScrollbar(tree_frame, command=tree.yview)
tree.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.pack(side="right", fill="y")

column_vars = {col: ctk.BooleanVar(value=(col in current_columns)) for col in columns}
for col in columns:
    if col in current_columns:
        tree.heading(col, text=col, command=lambda _col=col: sort_by_column(_col))
        tree.column(col, width=100, stretch=True)
    else:
        tree.heading(col, text="")
        tree.column(col, width=0, stretch=False)

tree.pack(padx=10, pady=10, fill="both", expand=True)

tree.bind("<Button-3>", show_column_menu)
tree.bind("<Double-1>", copy_to_clipboard)

clipboard_label = ctk.CTkLabel(root, text="", fg_color="transparent")
clipboard_label.pack()

bottom_frame = ctk.CTkFrame(root)
bottom_frame.pack(pady=10)

show_code_button = ctk.CTkButton(bottom_frame, text="Show Original Code", command=show_original_code)
show_code_button.pack(side="left", padx=5)

save_button = ctk.CTkButton(bottom_frame, text="Save Items", command=save_items)
save_button.pack(side="left", padx=5)

settings_button = ctk.CTkButton(bottom_frame, text="Settings", command=open_settings)
settings_button.pack(side="left", padx=5)

appearance_mode_label = ctk.CTkLabel(bottom_frame, text="Appearance Mode:")
appearance_mode_label.pack(side="left", padx=5)

appearance_mode_option = ctk.CTkOptionMenu(bottom_frame, values=["System", "Light", "Dark"], command=ctk.set_appearance_mode)
appearance_mode_option.pack(side="left", padx=5)

update_item_list(filtered_items, list(range(len(filtered_items))))

root.mainloop()