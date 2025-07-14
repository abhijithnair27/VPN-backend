import time
from django.db import connection
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger('VPN_backend.middlewares')

class APITimingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()
        # Clear old queries
        connection.queries_log.clear()

    def process_response(self, request, response):
        total_time = time.time() - request._start_time
        queries = connection.queries
        db_time = sum(float(q['time']) for q in queries)
        num_queries = len(queries)

        logger.info(
            f"{request.path} | Total time: {total_time:.3f}s | DB time: {db_time:.3f}s | Queries: {num_queries}"
        )

        return response
