from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class CategoryAnonThrottling(AnonRateThrottle):
    scope = 'category_anon'

class CategoryUserThrottling(UserRateThrottle):
    scope = 'category_user'


class ProductAnonThrottling(AnonRateThrottle):
    scope = 'product_anon'

class ProductUserThrottling(UserRateThrottle):
    scope = 'product_user'


class OrderAnonThrottling(AnonRateThrottle):
    scope = 'order_anon'

class OrderUserThrottling(UserRateThrottle):
    scope = 'order_user'