from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ApiCustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        p = self.page
        stats = {'total_record_count': p.paginator.count, 'num_pages': p.paginator.num_pages,
                 'current_page_no': p.number, 'previous': self.get_previous_link(), 'next': self.get_next_link()
                 }
        return Response(
            data={'page_details': stats, 'records': data}
        )
