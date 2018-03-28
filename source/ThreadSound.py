import threading
import time
import pyttsx3

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, flag,interval=1):
        self.flag=flag
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            if(self.flag==1):
            # Do something
                print('Doing something imporant in the background')
                engine = pyttsx3.init()
                engine.say("Human Detected")
                engine.runAndWait()
                time.sleep(self.interval)



