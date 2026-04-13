import sys
import time

# declaring the function
def typing_effect(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


#calling the function
typing_effect("Brainzima Innovation Institute is a trusted computer and coding training institute in Katihar, Bihar. We offer job-oriented computer courses including Basic Computer, DCA, ADCA, programming languages like C, C++, Java, Python, and web development")