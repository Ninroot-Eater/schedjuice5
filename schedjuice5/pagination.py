from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# customizing the PageNumberPagination class to my liking.


class CustomPagination(PageNumberPagination):

    page_size_query_param = "size"
    page_size = 10

    def get_count_per_page(self):
        return len(list(self.page))

    def get_paginated_response(self, *args, **kwargs):
        return {
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
            "count": self.page.paginator.count,
            "count_per_page": self.get_count_per_page()
        }
