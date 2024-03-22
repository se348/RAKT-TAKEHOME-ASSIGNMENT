def paginate_query(page, page_size):
    """Calculate skip and limit for pagination."""
    skip = (page - 1) * page_size
    limit = page_size
    return skip, limit

def get_prev_and_next_page(page, page_size, total):
    """Calculate the previous and next page numbers."""
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if total > page * page_size else None
    return prev_page, next_page