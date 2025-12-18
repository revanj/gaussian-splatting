import pycolmap
filtered = pycolmap.Reconstruction("data/79_decimate_interp/00010c81/sparse/0_new")

print("Remaining images:")
for img_id, img in sorted(filtered.images.items()):
    print(f"  ID {img_id}: {img.name}")
