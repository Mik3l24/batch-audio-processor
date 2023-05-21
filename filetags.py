class FileTags:
    tags = {}

    def updateTags(self, other_tags):
        assert isinstance(other_tags, FileTags), "Invalid input. Expected object of type FileTags."
        self.tags.update(other_tags.tags)
