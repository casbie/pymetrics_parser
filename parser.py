from html.parser import HTMLParser
import json
import argparse
from pprint import pprint

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.card_tag = False
        self.card_title = False
        self.msg_left = False
        self.msg_right = False
        self.data = list()
        self.item = dict()

    def get_result(self):
        return self.data

    def handle_starttag(self, tag, attrs):
        if tag == 'trait-card':
            self.card_tag = True

        score = None
        for name, value in attrs:
            if name == 'ng-style':
                score = value

            if name == 'class' and value == 'regular-font ng-binding':
                self.card_title = True

            if tag == 'div' and name == 'style' and value == 'padding-left:0;':
                self.msg_left = True
            if tag == 'div' and name == 'style' and value == 'padding-right:0;':
                self.msg_right = True

        if score:
            score = score.replace('\'', '\"')
            score = json.loads(score)['left'].rstrip("%")
            # print("Score: ", score)
            self.item['score'] = float(score)


    def handle_endtag(self, tag):
        if tag == 'trait-card':
            self.card_tag = False
        if tag == 'div' and self.msg_left:
            self.msg_left = False
        if tag == 'div' and self.msg_right:
            self.msg_right = False
        
        if tag == 'h4' and self.card_title:
                self.card_title = False

    def handle_data(self, data):
        if self.card_title:
            # print('Card title: ', data)
            self.item['title'] = data
        if self.msg_left:
            # print('Left message: ', data)
            self.item['left_msg'] = data
        if self.msg_right:
            # print('Right message: ', data)
            self.item['right_msg'] = data
            self.data.append(self.item)
            self.item = dict()


def process_result(result, threshold=75.0):
    for item in result:
        if item['score'] > threshold:
            print('[{}] {} ({}%)'.format(item['title'], item['right_msg'], round(item['score'], 2)))
        elif item['score'] < (100-threshold):
            print('[{}] {} ({}%)'.format(item['title'], item['left_msg'], round(item['score'], 2)))

if __name__ == '__main__':
    # parse your arguments
    arg_parser = argparse.ArgumentParser(description='Automatically generate Pymetrics test report')
    arg_parser.add_argument('-f', metavar='file_name', type=str, default='pymetrics.html',
                    help='the html file you want to parse')
    arg_parser.add_argument('-t', metavar='threshold', type=float, default=75.0,
                    help='the threshold to decide your identities (percentage, default 75)')
    args = arg_parser.parse_args()
    
    file_name = args.f
    threshold = args.t

    # get the input file
    f = open(file_name)
    html_code = f.read()

    # parse the html code
    parser = MyHTMLParser()
    parser.feed(html_code)

    # filter the result by threshold
    result = parser.get_result()
    process_result(result, threshold)
    