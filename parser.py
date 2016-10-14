#!/usr/bin/env python
# coding: utf-8

import os
from os.path import exists
from jinja2 import Template

HERE = os.path.dirname(os.path.abspath(__file__))


def _save_text_to_file(context, target_file):

    target_dir = os.path.dirname(target_file)
    if not exists(target_dir):
        os.makedirs(target_dir)

    with open(target_file, 'w') as target_handle:
        target_handle.write(context)


def main():
    machines_j2_yaml_file = os.path.join(HERE, 'machines.j2.yaml')
    nodes_yaml_file = os.path.join(HERE, 'nodes.yaml')
    _save_text_to_file(Template(open(machines_j2_yaml_file).read()).render(), nodes_yaml_file)


if __name__ == '__main__':
    main()
