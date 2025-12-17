import pycolmap
filtered = pycolmap.Reconstruction("data/79_decimate/00010c81/sparse/0")

print("Remaining images:")
for img_id, img in sorted(filtered.images.items()):
    print(f"  ID {img_id}: {img.name}")
