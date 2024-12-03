from django.shortcuts import render
from .models import Tests

from rest_framework import generics, permissions, parsers


class Test_views(generics