from behave import  *
from selenium import webdriver

def before_all(context):
    print ("browser Initalised")

def before_feature(context, feature):
    print("before feature")

def before_scenario(context, scenario):
    print ("scenario passed")

def before_step(context, step):
    print ("step passed")

def after_all(context):
    print ("browser quit")

def after_feature(context, feature):
    print("after feature")

def after_scenario(context, scenario):
    print ("after passed")

def after_step(context, step):
    print ("after step passed")
