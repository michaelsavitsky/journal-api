from app.models.entry import EntryModel
import collections

def sortByCategory(entries: EntryModel):
    result = collections.defaultdict(list)
    for d in entries:
        result[d['category']].append(d)

    return list(result.values()) 