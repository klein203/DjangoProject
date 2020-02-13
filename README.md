# Readme
## local settings
- create a file named _local_setting.py_
- make sure you include codes below in the bottom of your _setting.py_ file
```
if os.path.isfile(os.path.join('core', 'local_settings.py')):
    from .local_settings import *
else:
    print(_("No local settings file found"))
```

## migrations
- generate scripts from logical models
```
python manage.py makemigrations
```
- execute scripts to persistent layer
```
python manage.py migrate
```
- show migrations info
```
python manage.py showmigrations
```

## i18n settings
- include code below in the _setting.py_ or local setting file
```
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

LANGUAGES = (
    ('en', 'English'),
    ('zh-Hans', '简体中文'),
    ('zh-Hant', '中文繁體'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'conf', 'locale'),
)
```

- create or update _locale/LC_MESSAGE_ directories and localization file with .po extension in the directory _LOCALE_PATHS_.

**Remind the seperator of zh_Hans should be underscore '_'
```
python manage.py makemessages -l zh_Hans
```

- compile .po files to .mo files to enable quick access for message translation
```
python manage.py compilemessages
```

## template hierarchy definition
- root template `common/base.html`
