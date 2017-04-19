import calendar
import string
import random
import uuid
import base64
import hashlib
import datetime
import imp
from decimal import Decimal

from django.utils.timezone import localtime
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from allauth.account.adapter import get_adapter


def render_template_to_string(template_file, params, request):
    """ Render template and get the HTML response
    """
    return render_to_string(
        template_name=template_file,
        context=params,
        request=request
    )


def get_current_application(request):
    """ Get current application
    """
    try:
        appname = request.resolver_match.namespace

        if appname is None or appname == '':
            appname = "home"
    except:
        appname = "home"

    return appname


def get_current_view(request):
    """ Get current view name
    """
    try:
        viewname = request.resolver_match.url_name
    except:
        viewname = ""

    return viewname


def get_current_view_params(request):
    """  Get params
    """
    params = request.get_full_path()

    if params.startswith("/"):
        params = params[1:]

    if params.endswith("/"):
        params = params[:-1]

    params = params.split("/")

    return params[2:]


def get_client_ip(request=None):
    """ Get IP from visitor
    """

    if not request:
        return "127.0.0.1"

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def chunk_list(l, n):
    """ Chunk l in sublist of size n
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def generate_password():
    """ Generate random password
    """
    chars = string.ascii_uppercase + string.digits
    size = 6

    return ''.join(random.choice(chars) for x in range(size))


def generate_username(content):
    """
    Generate username
    """
    return base64.urlsafe_b64encode(
        hashlib.sha256(
            content.encode("utf8", "ignore")
        ).digest()
    )[:30]


def localize_date_time (dt):
    """ Fix date time
    """
    try:
        result = localtime(dt)
    except:
        result = dt

    return result


def get_system_user():
    """ Get user with username system
    """
    return User.objects.get(username="system")


def get_author_user(request=None):
    """ Get system user
    """
    if not request or not request.user.is_authenticated():
        return get_system_user()

    return request.user


def get_author_data(request):
    """ Get author data
    """
    return (
        get_author_user(request),
        get_client_ip(request),
    )


def generate_key():
    """ Generate UUID hash
    """
    return str(uuid.uuid4())


def get_absolute_url(request, url):
    """ Get absolute URL
    """
    return request.build_absolute_uri(url)


def decode_text(value, charset="iso-8859-1"):
    """ Decode text
    """
    return value.decode(charset)


def remove_extra_whitespace(value):
    """ Remove extra whitespace in string
    """
    return " ".join(value.split())


def calculate_age(d1):
    """ Calculate age
    """
    d2 = datetime.date.today()

    return d2.year - d1.year - ((d2.month, d2.day) < (d1.month, d1.day))


def users_can_register(request):
    """ Check if users can self register
    """
    return get_adapter(request).is_open_for_signup(request)


def get_user_identity(user):
    """ Get user identity
    """
    return user.get_full_name() or user.username


def get_week_dates(d):
    start = d - datetime.datetime.timedelta(days=d.weekday() % 7)
    end = start + datetime.datetime.timedelta(days=6)

    return [
        start,
        end
    ]


def fix_decimal_points(n, mask='1.00'):
    return n.quantize(Decimal(mask))


def import_path(path):
    return imp.load_source(
        'module.name',
        path
    )


def get_year_week(d):
    return d.isocalendar()[1]


def get_weeks_number(year):
    return int(
        datetime.datetime(
            year,
            12,
            31
        ).strftime("%W")
    )


def get_month_dates(year, month):
    d = datetime.datetime(year, month).date()

    first = d.replace(day=1)
    last = d.replace(day=calendar.monthrange(year, month)[1])

    return first, last


def build_dates_range(start, end):
    return [
        datetime.datetime.combine(
            start,
            datetime.time.min
        ),

        datetime.datetime.combine(
            end,
            datetime.time.max
        ),
    ]


def build_month_range(y, m):
    start, end = get_month_dates(y, m)

    return build_dates_range(start, end)


def build_year_range(y):
    start = datetime.datetime(y, 1, 1).date()
    end = datetime.datetime(y, 12, 31).date()

    return build_dates_range(start, end)
