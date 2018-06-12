import os
import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument('--date', help='Date in the format of: YYYY-MM--DD')
parser.add_argument('--title', help='Title in the form of: this-is-the-tile')
args=parser.parse_args()

if not args.title:
    print 'Please provide a title, use --help for help'
    sys.exit()

if not args.date:
    print 'Please provide a date, use --help for help'
    sys.exit()

directory = "_drafts/blog/{0}/".format(args.date)
if not os.path.exists(directory):
    os.makedirs(directory)

f = open("{0}{1}-{2}.md".format(directory, args.date, args.title), "w+")
lines = [
    "---",
    "title: '{0}'".format(args.title.capitalize()).replace("-", " "),
    "layout: post",
    "date: '2018-06-06 00:30:00 -0300'",
    "---",
    "Here goes the content"
]
f.writelines("\n".join(lines))
f.close()
