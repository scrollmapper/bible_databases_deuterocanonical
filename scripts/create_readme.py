import os

def read_template(template_path):
	with open(template_path, 'r', encoding='utf-8') as template_file:
		return template_file.read()

def generate_links(base_dir):
	links = []
	for root, _, files in os.walk(base_dir):
		folder_name = os.path.basename(root)
		required_files = {f"{folder_name}.json", "README.md"}
		if not required_files.issubset(files):
			continue
		md_file_path = os.path.join(root, f"{folder_name}.md")
		if not os.path.exists(md_file_path):
			continue
		with open(md_file_path, 'r', encoding='utf-8') as md_file:
			for line in md_file:
				text_name = line.strip().replace("#", "")
				if text_name:
					break
		link = f"- [{text_name}]({os.path.relpath(md_file_path, base_dir)})"
		links.append(link)
	return links

def assemble_readme(template, links, output_path):
	main_scrollmapper = []
	ante_nicene = []
	nicene_1 = []
	nicene_2 = []

	for link in links:
		print(link)
		if "sources" in link:
			main_scrollmapper.append(link)
		elif "ante-nicene" in link:
			ante_nicene.append(link)
		elif "nicene-1" in link:
			nicene_1.append(link)
		elif "nicene-2" in link:
			nicene_2.append(link)

	with open(output_path, 'w', encoding='utf-8') as readme_file:
		readme_file.write(template)
		readme_file.write("\n\n## Texts\n\n")

		if main_scrollmapper:
			readme_file.write(f"### Scrollmapper Main Texts ({len(main_scrollmapper)})\n")
			for link in main_scrollmapper:
				readme_file.write(f"{link}\n")
				print(link)
			readme_file.write("\n")

		if ante_nicene:
			readme_file.write(f"### Ante-Nicene ({len(ante_nicene)})\n")
			for link in ante_nicene:
				readme_file.write(f"{link}\n")
			readme_file.write("\n")

		if nicene_1:
			readme_file.write(f"### Nicene 1 ({len(nicene_1)})\n")
			for link in nicene_1:
				readme_file.write(f"{link}\n")
			readme_file.write("\n")

		if nicene_2:
			readme_file.write(f"### Nicene 2 ({len(nicene_2)})\n")
			for link in nicene_2:
				readme_file.write(f"{link}\n")
			readme_file.write("\n")


if __name__ == "__main__":
	template_path = "readme/readme.md"
	output_path = "../README.md"

	template = read_template(template_path)
	links = generate_links("../") 
	assemble_readme(template, links, output_path)

	print(f"Generated {output_path} with links to all texts.")
