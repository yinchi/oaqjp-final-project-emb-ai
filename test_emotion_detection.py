import unittest

from EmotionDetection.emotion_detection import emotion_detector

TESTS = [
    ("I am glad this happened", "joy"),
    ("I am really mad about this", "anger"),
    ("I feel disgusted just hearing about this", "disgust"),
    ("I am so sad about this", "sadness"),
    ("I am really afraid that this will happen", "fear"),
]

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        for test in TESTS:
            self.assertEqual(emotion_detector(test[0])['dominant_emotion'], test[1])

unittest.main()
