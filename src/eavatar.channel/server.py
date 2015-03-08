# -*- coding: utf-8 -*-
"""
The entrypoint for the channel server.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from eavatar.channel import app


def main():
    app.run()


if __name__ == '__main__':
    main()