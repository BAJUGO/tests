"""
There are lots of problems with id or _id or smth like that,
so I decided to start function names with "id" or smth for
your attention
"""
def id_list_fixed(cursor_listed: list):
    for el in cursor_listed:
        el["_id"] = str(el["_id"])
    return cursor_listed


def id_doc_fixed(doc: dict):
    doc["_id"] = str(doc["_id"])
    return doc
