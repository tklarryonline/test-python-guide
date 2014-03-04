# -*- coding: utf-8 -*-
from lettuce import step
from polls.features.steps.lettuce_support import browser
import sure

@step(u'I have a list of polls')
def i_have_a_list_of_polls(step):
    from polls.models import Question, Choice
    import datetime

    #create 5 poll question
    for i in range(0, 5):
        question = Question()
        question.question_text = "Question text %s" % i
        question.pub_date = datetime.datetime.now()
        question.save()

        # create 5 choice for each question
        for j in range(0, 5):
            choice = Choice()
            choice.choice_text = "Choice text %s" % j
            choice.question = question
            choice.save()

@step(u'I visit "([^"]*)"')
def i_visit_url(step, url):
    browser().get('http://localhost:8000%s' % url) # produce right url


@step(u'I should see a list of polls question')
def i_should_see_a_list_of_polls_question(step):
    questions = browser().find_elements_by_css_selector("#questions .question")
    len(questions).should.equal(5)

@step(u'there is no question in the system')
def there_is_no_question_in_the_system(step):
    from polls.models import Question
    Question.objects.all().delete()

@step(u'I should see the text "([^"]*)"')
def i_should_see_the_text(step, text):
    body_element = browser().find_element_by_tag_name("body")
    body_element.text.should.contain(text)