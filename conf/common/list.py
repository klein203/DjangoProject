from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import View
from conf.common.response import CustomizedJsonResponseMixin


class MultipleJsonObjectMixin(MultipleObjectMixin):
    return_code_name = 'code'
    return_message_name = 'msg'
    data_object_name = 'data'
    paginator_object_name = 'page'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        return_code_name = self.get_return_code_name()
        return_message_name = self.get_return_message_name()
        data_object_name = self.get_data_object_name()
        paginator_object_name = self.get_paginator_object_name()

        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                return_code_name: 0,
                return_message_name: 'success',
                data_object_name: page,
                paginator_object_name: {
                    'per_page': paginator.per_page,
                    'page': page.number,
                    'count': paginator.count,
                    'is_paginated': is_paginated,
                },
                'object_list': queryset
            }
        else:
            context = {
                return_code_name: 0,
                return_message_name: 'success',
                data_object_name: queryset,
                paginator_object_name: {
                    'per_page': None,
                    'page': None,
                    'count': queryset.count,
                    'is_paginated': False,
                },
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super(MultipleObjectMixin, self).get_context_data(**context)

    def get_context_object_name(self, object_list):
        """Get the name of the item to be used in the context."""
        if self.context_object_name:
            return self.context_object_name
        else:
            return None

    def get_return_code_name(self):
        if self.return_code_name == None:
            self.return_code_name = 'code'
        return self.return_code_name

    def get_return_message_name(self):
        if self.return_message_name == None:
            self.return_message_name = 'msg'
        return self.return_message_name

    def get_data_object_name(self):
        if self.data_object_name == None:
            self.data_object_name = 'data'
        return self.data_object_name

    def get_paginator_object_name(self):
        if self.paginator_object_name == None:
            self.paginator_object_name = 'page'
        return self.paginator_object_name


class BaseJsonListView(MultipleJsonObjectMixin, View):
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_json_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class JsonListView(BaseJsonListView, CustomizedJsonResponseMixin):
    http_method_names = ['post', 'get']
