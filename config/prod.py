from .base import *

DEBUG = False

ALLOWED_HOSTS = ['43.202.97.115']

STATIC_ROOT = BASE_DIR / 'static/'

# 추가적인 정적 파일 경로 설정
STATICFILES_DIRS = []

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/ubuntu/projects/DA34-final-trois-blackmamba_web/logs/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
