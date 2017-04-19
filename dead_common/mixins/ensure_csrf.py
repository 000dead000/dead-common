from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


class EnsureCSRFMixin(object):
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(EnsureCSRFMixin, self).dispatch(*args, **kwargs)
