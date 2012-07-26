confuzzle
=========

**A tiny tool for generating configuration files by combining [Jinja2](http://jinja.pocoo.org/docs/) templates with [YAML](http://www.yaml.org/) data.**

**Author:** Jamie Matthews. [Follow me on Twitter](http://twitter.com/j4mie).

When deploying an application, you often need to create configuration files for various components (databases, web servers, reverse proxies, etc). Often, the **same** value needs to appear in **multiple** places (for example, a port number that servers should bind to and clients should connect to). `confuzzle` lets you store all of your app config in one place (possibly outside of version control), and combine it with your templated config files at build time.

Example
-------

In your `gunicorn.py.tmpl`:

```jinja
bind: "bind = "127.0.0.1:{{ gunicorn.port }}"
```

In your `nginx.conf.tmpl`:

```jinja
upstream app_server {
    server 127.0.0.1:{{ gunicorn.port }} fail_timeout=0;
}
```

Here's your `config.yaml`

```yaml
gunicorn:
  port: 8080
```

By default, confuzzle reads from `stdin` and writes to `stdout`. To use:

   confuzzle config.yaml < gunicorn.py.tmpl > gunicorn.py
   confuzzle config.yaml < nginx.conf.tmpl > nginx.conf

Now, your files look like this:

```jinja
bind: "bind = "127.0.0.1:8080"
```

```jinja
upstream app_server {
    server 127.0.0.1:8080 fail_timeout=0;
}
```

You can also supply a list of YAML files. This might be useful if you'd like to combine a general config file (in version control) with a file containing secrets such as database passwords (not in version control).

    confuzzle config.yaml secrets.yaml < settings.py.tmpl > settings.py

See `confuzzle --help` for the full list of arguments.

Prints to stdout the result of combining gunicorn_template.conf with the yaml data in config.yaml

Changelog
---------

#### 0.1.0

* Initial release.

Installation
------------

**Not yet on PyPI! Clone the repo and `python setup.py develop`**

You can install confuzzle from PyPI:

    pip install confuzzle

## Development

To contribute: fork the repository, make your changes, add some tests, commit,
push to a feature branch, and open a pull request.

## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
