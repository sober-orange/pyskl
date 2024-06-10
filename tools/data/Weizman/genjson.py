import os
import decord
import json
from mmcv import load, dump

from pyskl.smp import mwlines


def writeJson(path_train, jsonpath):
    outpot_list = []
    trainfile_list = os.listdir(path_train)
    for train_name in trainfile_list:
        traindit = {}
        sp = train_name.split('_')
        traindit['vid_name'] = train_name.replace('.avi', '')
        traindit['label'] = int(sp[1].replace('.avi', ''))
        traindit['start_frame'] = 0

        video_path = os.path.join(path_train, train_name)
        vid = decord.VideoReader(video_path)
        traindit['end_frame'] = len(vid)
        outpot_list.append(traindit.copy())
    with open(jsonpath, 'w') as outfile:
        json.dump(outpot_list, outfile)


# path是数据集路径 dirpath = '../data/Weizmann'
# name为生成的list文件名称，这里为 'Weizmann'
def writeList(dirpath, name):
    path_train = os.path.join(dirpath, 'train')
    path_test = os.path.join(dirpath, 'test')
    trainfile_list = os.listdir(path_train)
    testfile_list = os.listdir(path_test)

    train = []
    for train_name in trainfile_list:
        traindit = {}
        sp = train_name.split('_')

        traindit['vid_name'] = train_name
        traindit['label'] = sp[1].replace('.avi', '')
        train.append(traindit)
    test = []
    for test_name in testfile_list:
        testdit = {}
        sp = test_name.split('_')
        testdit['vid_name'] = test_name
        testdit['label'] = sp[1].replace('.avi', '')
        test.append(testdit)

    tmpl1 = os.path.join(path_train, '{}')
    lines1 = [(tmpl1 + ' {}').format(x['vid_name'], x['label']) for x in train]

    tmpl2 = os.path.join(path_test, '{}')
    lines2 = [(tmpl2 + ' {}').format(x['vid_name'], x['label']) for x in test]
    lines = lines1 + lines2
    mwlines(lines, os.path.join(dirpath, name))


def traintest(dirpath, pklname, newpklname):
    os.chdir(dirpath)
    train = load('train.json')
    test = load('test.json')
    annotations = load(pklname)
    split = dict()
    split['xsub_train'] = [x['vid_name'] for x in train]
    split['xsub_val'] = [x['vid_name'] for x in test]
    dump(dict(split=split, annotations=annotations), newpklname)


if __name__ == '__main__':
    dirpath = './'
    pklname = 'train.pkl'
    newpklname = 'Wei_xsub_stgn++.pkl'
    # writeJson('test', 'test.json')
    # writeJson('train', 'train.json')
    traintest(dirpath, pklname, newpklname)
    # writeList('./', 'Weizmann.list')
