<a href="https://github.com/lk-geimfari/wasserstoff/">
    <p align="center">
      <img src="https://raw.githubusercontent.com/lk-geimfari/wasserstoff/master/media/wasserstoff_large.png">
    </p>
</a>

**Wasserstoff** - is a library that help you store your configurations for applications in JSON files. The configuration will be easily loaded to the scope of configuration object. The library was written with the use of tools from the standard Python library, and therefore, it does not have any side dependencies.


### Installation
```
➜  ~ pip install wasserstoff
```
or (when the project has been cloned):
```
➜  make test
➜  make install
```

### Usage

Content of `dev.json`:
```json
{
  "smtp server": [
	"smtp.yandex.ru",
	"smtp.gmail.com"
  ],
  "port": 456,
  "ssl": true,
  "secret_key": "SECRET_KEY_HERE"
}

```

Content of `test.json`:
```json
{
  "ssl": false,
  "secret_key": "001110110100101100101010100010111010"
}

```

Loading configurations from the file:
```python
>>> import wasserstoff
>>> config = wasserstoff.Config()

>>> config.add(
...     scope='dev',
...     file='dev', # without extension
... ).setup()

>>> config.dev.SMTP_SERVER
['smtp.yandex.ru', 'smtp.gmail.com']

>>> config.dev.SSL
True

>>> config.dev.PORT
456

>>> config.dev.SECRET_KEY
'SECRET_KEY_HERE'

>>> config.add(
...     scope='test',
...     file='test',
... ).setup()

>>> config.test.SECRET_KEY
'001110110100101100101010100010111010'
```

### License
Wasserstoff is licensed under the MIT License. See LICENSE for more information. 
