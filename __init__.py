# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import intent_file_handler
from mycroft.util.log import LOG
from mycroft.util.parse import extract_datetime
import json
import requests


UTC_TZ = u'+0:00'
# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class GTMSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(GTMSkill, self).__init__(name="GTMSkill")
        
        # Initialize working variables used within the skill.
        self.count = 0

    


    @intent_file_handler('SetStartTime.intent')
    def get_start_time(self,msg):
        print("in start time************")
        start = extract_datetime(msg.data['utterance'])[0]
        #print("message data", msg.data['utterance'])
        #print("here is the time from msg",extract_datetime(msg.data['utterance']))
        print("here is the time", start)
        self.speak_dialog("Success")


    '''@intent_file_handler('SetEndTime.intent')
    def get_end_time(self,msg):
        end = extract_datetime(msg.data['utterance'])[0]
        #print("message data", msg.data['utterance'])
        #print("here is the time from msg",extract_datetime(msg.data['utterance']))
        #print("here is the time", st)
        self.speak_dialog("Success", data = {"end":end})'''



    

        # Sending a command to mycroft, speak Greetings Dialog


    # The "handle_xxxx_intent" function is triggered by Mycroft when the
    # skill's intent is matched.  The intent is defined by the IntentBuilder()
    # pieces, and is triggered when the user's utterance matches the pattern
    # defined by the keywords.  In this case, the match occurs when one word
    # is found from each of the files:
    #    vocab/en-us/Hello.voc
    #    vocab/en-us/World.voc
    # In this example that means it would match on utterances like:
    #   'Hello world'
    #   'Howdy you great big world'
    #   'Greetings planet earth'
  

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return GTMSkill()
