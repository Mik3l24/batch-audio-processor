import music_tag as music_tag

valid_tags = [
    "album",
    "albumartist",
    "artist",
    "artwork",
    "comment",
    "compilation",
    "composer",
    "discnumber",
    "genre",
    "lyrics",
    "totaldiscs",
    "totaltracks",
    "tracknumber",
    "tracktitle",
    "year",
    "isrc",
]


class FileTags:
    tags: dict = {}

    def updateTags(self, other_tags: "FileTags"):
        self.tags.update(other_tags.tags)

    def replaceTags(self, other_tags: "FileTags"):
        pass

    def __init__(self, tag_source: music_tag.AudioFile = None):
        for tag in valid_tags:
            if tag_source is None or tag_source[tag] is None:
                self.tags[tag] = None
            else:
                self.tags[tag] = tag_source[tag].value


