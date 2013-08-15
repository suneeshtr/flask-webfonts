# -*- coding: utf-8 -*-
"""
    flask.ext.webfonts
    ~~~~~~~~~~~~~~~~~
This extension provides a simple font gallery interface as well as a api for
using the fonts as webfonts.

    :copyright: (c) 2013 by Nithin Saji.
    :license: BSD, see LICENSE for more details.
"""

from .views import WebfontsApiView
from flask import Blueprint


class Webfonts(object):
    """
    This class makes flask application serve webfonts from a specified url or
    subdomain. It also comes with an optional interface for showcasing
    webfonts. It supports multiple lamguages.
    """
    def __init__(
            self,
            fonts,
            app=None,
            font_folder="fonts",
            api_url_prefix="/webfonts",
            subdomain=None
    ):

        self.app = app
        self.fonts = fonts
        self.url_prefix = api_url_prefix
        self.subdomain = subdomain
        self.font_folder = font_folder
        self.blueprint = Blueprint('api_Blueprint', __name__, static_folder=font_folder)
        self.blueprint.add_url_rule('/', view_func=WebfontsApiView(fonts).as_view('webfonts_api', fonts))

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        #register the api blueprint
        app.register_blueprint(self.blueprint,
                               static_folder=self.font_folder,
                               template_folder='templates',
                               url_prefix=self.url_prefix,
                               subdomain=self.subdomain)

    def add_gallery(self, url_prefix):
        pass

    def list_fonts(self, *languages):
        font_list = []
        for i in self.fonts:
            if self.fonts[i]["Language"] in languages:
                font_list.append({i: self.fonts[i]})
        return font_list
