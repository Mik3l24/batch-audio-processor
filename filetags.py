class FileTags:
    tags: dict = {}

    def updateTags(self, other_tags: "FileTags"):
        self.tags.update(other_tags.tags)

    def replaceTags(self, other_tags: "FileTags"):
        pass
