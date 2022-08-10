import cv2
cv2.imwrite = lambda x,y: 1

from options import parse_args
from evaluate import evaluate


args = parse_args()
if args.dataset == '':
    args.keyname = 'evaluate'
else:
    args.keyname = args.dataset
args.test_dir = 'test/' + args.keyname
if args.testingIndex >= 0:
    args.debug = True
if args.debug:
    args.test_dir += '_debug'
    args.printInfo = True

evaluate(args)

