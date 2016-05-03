MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'bible'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# bible versions i.e. MSG, ESV, NLT
version_schema = {
    'title': {
        'type': 'string',
    }
}

versions = {
    'additional_lookup': {
        'url': 'regex("[\w+]")',
        'field': 'title'
    },
    'schema': version_schema
}

# books I.E. Judges, Genesis etc
book_schema = {
    'title': {
        'type': 'string',
    }
}

books = {
    'additional_lookup': {
        'url': 'regex("[\w+]")',
        'field': 'title'
    },
    'schema': book_schema
}

# chapters
chapter_schema = {
    'number': {
        'type': 'integer',
        'coerse': int,
    }
}

chapters = {
    'additional_lookup': {
        'url': 'regex("[\d+]")',
        'field': 'number'
    },
    'schema': chapter_schema
}

# verses
verse_schema = {
    'number': {
        'type': 'integer',
        'coerse': int
    },
    'text': {
        'type': 'string'
    }
}

verses = {
    'additional_lookup': {
        'url': 'regex("[\d+]")',
        'field': 'number'
    },
    'schema': verse_schema
}


DOMAIN = {
    'versions': versions,
    'books': books,
    'chapters': chapters,
    'verses': verses
}
