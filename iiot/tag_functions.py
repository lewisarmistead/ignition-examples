def export_all_tags():
	providers = system.tag.browse('')
	tag_providers = [p["name"] for p in providers]
	for i in tag_providers:
		filePath = "/backup/{provider}_tags.json".format(**{"provider": i})
		system.tag.exportTags(filePath=filePath, tagPaths=["[{provider}]".format(**{"provider": i})], recursive=True)
