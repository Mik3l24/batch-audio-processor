class FileTags:
    tags = {}

    def updateTags(self, other_tags):
        if isinstance(other_tags, FileTags):
            self.tags.update(other_tags.tags)
        else:
            print("Invalid input. Expected object of type FileTags.")
