#!/usr/bin/env python
#-*- coding:utf-8 -*-

'test wsgiref'

#__author__=

def application(environ,start_response):
	print environ['PATH_INFO']
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>Hello,%s</h1>' % (environ['PATH_INFO'][1:] or 'web')