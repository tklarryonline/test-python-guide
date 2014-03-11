# -*- coding: utf-8 -*-
from polls.features.steps.lettuce_support import *
import sure

@step(u'I click on a poll question link')
def i_click_on_a_poll_question_link(step):
    find(".question a").click()

@step(u'I should see the poll detail')
def i_should_see_the_poll_detail(step):
    find("ul li input").should_not.be.none

@step(u'When I click button "([^"]*)"')
def when_i_click_button_group1(step, button_text):
    xpath(".//button[.='%s']" % button_text).click()