#!/usr/bin/env python

import zipfile
import shutil
import os
import sys


def add_channel_file(apk_file, channel_file, channel_name):
    zipped = zipfile.ZipFile(apk_file, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/mchpkg_{channel}".format(channel=channel_name)
    print('adding channel file ' + empty_channel_file)
    zipped.write(channel_file, empty_channel_file)
    zipped.close()


def create_empty_file(name):
    f = open(name, 'w')
    f.close()


def ensure_output_dir(out_dir):
    exist = os.path.exists(out_dir)
    if not exist:
        os.makedirs(out_dir)


def zip_output(apks, output_file):
    zipped = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
    try:
        for apk in apks:
            zipped.write(apk)
    finally:
        zipped.close()
    for apk in apks:
        os.remove(apk)


if __name__ == '__main__':
    assert len(sys.argv[1]) > 0
    assert len(sys.argv[2]) > 0

    APK_FILE = sys.argv[1]
    config_file = open(sys.argv[2])
    cwd = os.path.split(os.path.realpath(__file__))[0]
    OUTPUT_DIR = cwd + '/output'
    EMPTY_FILE = OUTPUT_DIR + '/empty'
    output_files = []
    ensure_output_dir(OUTPUT_DIR)

    try:
        # os.chdir(OUTPUT_DIR)
        create_empty_file(EMPTY_FILE)
        for line in config_file:
            config = line.strip()
            if len(config) > 0:
                break
        channels = config.split(',')
        for channel in channels:
            channel = channel.strip()
            print('Preparing package for channel ' + channel)
            apk_name = OUTPUT_DIR + '/' + os.path.splitext(os.path.basename(APK_FILE))[0] + '_' + channel + '.apk'
            output_files.append(apk_name)
            shutil.copyfile(APK_FILE, apk_name)
            add_channel_file(apk_name, EMPTY_FILE, channel)
        os.remove(EMPTY_FILE)
    finally:
        config_file.close()
    zip_output(output_files, OUTPUT_DIR + '/output.zip')
