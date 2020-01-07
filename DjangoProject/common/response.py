from django.http.response import JsonResponse


class JsonResponseMixin:
    response_class = JsonResponse

    def render_to_json_response(self, context, **response_kwargs):
        return self.response_class(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        return context
