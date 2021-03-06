# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

import os

from .base import BASE_DIR, PROJECT_ROOT_DIR

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "hoomi", "static"),
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT_DIR, "dist", "images")

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE = {
    'STYLESHEETS': {
        'hoomi': {
            'source_filenames': (
              'css/application.css',
              'css/font-awesome.css',
              'css/bootstrap-social.css',
              'css/hoomi.css',
              'fonts/*',
            ),
            'output_filename': 'css/hoomi.css',
        }
    },
    'JAVASCRIPT': {
        'hoomi': {
            'source_filenames': (
                'js/jquery.bootstrap-growl.min.js',
            ),
            'out_filename': 'js/hoomi.js',
        }
    },
}
