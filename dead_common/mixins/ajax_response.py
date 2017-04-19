# -*- coding: utf-8 -*-


class AjaxResponseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        request_method = request.method.lower()

        if request.is_ajax() and request_method in self.http_method_names:
            handler = getattr(
                self,
                "{0}_ajax".format(request_method),
                self.http_method_not_allowed
            )

            self.request = request
            self.args = args
            self.kwargs = kwargs
            return handler(request, *args, **kwargs)

        return super(AjaxResponseMixin, self).dispatch(
            request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def post_ajax(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def put_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

