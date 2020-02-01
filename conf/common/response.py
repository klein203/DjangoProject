from django.http.response import JsonResponse
from django.core import serializers
import datetime


class CustomizedJsonResponseMixin:
    allow_attrs = ['code', 'msg', 'data', 'page']
    response_class = JsonResponse

    def render_to_json_response(self, context, **response_kwargs):
        return self.response_class(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        # print('------------context---------------------')
        # for item in context.items():
        #     print(item)
        # print('----------------------------------------')

        data = dict()
        for attr in self.allow_attrs:
            data[attr] = context[attr]

        # TODO serialize context object to dict like structure
        data['data'] = self.get_dummy_data()
        data['page'] = self.get_dummy_page()

        # print('--------------data----------------------')
        # for item in data.items():
        #     print(item)
        # print('----------------------------------------')

        return data

    def get_dummy_data(self):
        return [{
            'id': 1,
            'name': 'aaa',
            'gender': 'M',
            'date_of_birth': datetime.date(1981, 1, 1),
            'create_time': datetime.datetime.now(),
            'update_time': datetime.datetime.now()
        },
            {
            'id': 2,
            'name': 'bbb',
            'gender': 'F',
            'date_of_birth': datetime.date(1981, 2, 2),
            'create_time': datetime.datetime.now(),
            'update_time': datetime.datetime.now()
        }]

    def get_dummy_page(self):
        return {
            'per_page': 1,
            'page': 1,
            'count': 2,
            'is_paginated': True,
        }

