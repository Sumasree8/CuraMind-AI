def keyword_search(query, knowledge_base):
    query = query.lower()

    for item in knowledge_base:
        if item["keyword"] in query:
            return item

    return None
