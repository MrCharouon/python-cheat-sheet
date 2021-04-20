#!/usr/bin/env python3

import argparse
import sys
from datetime import timedelta
from pathlib import Path

# pip3 install srt
import srt


def nearest(items, pivot):
    return min(items, key=lambda x: abs(x.start - pivot))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='merge SRT subtitles',
                                     usage="""
    Merge SRT subtitles:
    \t{0} first.srt second.srt -o merged.srt
 """.format(Path(sys.argv[0]).name))

    parser.add_argument('srt1',
                        metavar='srt1',
                        help='SRT-file-1')
    parser.add_argument('srt2',
                        metavar='srt2',
                        help='SRT-file-2')
    parser.add_argument('--output-file', '-o',
                        default=None,
                        help='Output filename')
    parser.add_argument('--encoding', '-e',
                        default=None,
                        help='Input file encoding')
    args = parser.parse_args(sys.argv[1:])

    srt1_path = Path(args.srt1)
    srt2_path = Path(args.srt2)

    with srt1_path.open(encoding=args.encoding or 'utf-8') as fi1:
        subs1 = {s.index: s for s in srt.parse(fi1)}

    with srt2_path.open(encoding=args.encoding or 'utf-8') as fi2:
        subs2 = {s.index: s for s in srt.parse(fi2)}

    # iterate all subs in srt2 and find the closest EXISTING slots in srt1
    for idx, sub in subs2.items():

        start: timedelta = sub.start
        sub_nearest_slot: srt.Subtitle = nearest(subs1.values(), start)
        sub_nearest_slot.content = f'{sub_nearest_slot.content}<br>{sub.content}'
        subs1[sub_nearest_slot.index] = sub_nearest_slot

    if not args.output_file:
        generated_srt = srt1_path.parent / (f'{srt1_path.stem}_MERGED_{srt1_path.suffix}')
    else:
        generated_srt = Path(args.output_file)

    with generated_srt.open(mode='w', encoding='utf-8') as fout:
        fout.write(srt.compose(list(subs1.values())))
