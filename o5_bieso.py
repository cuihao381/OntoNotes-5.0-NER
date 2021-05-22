from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse



def o5_bieso(fin, fout):
  xs = []
  ys = []
  with open(fout, 'w') as fw:
    for line in open(fin):
      line = line.strip()
      if line == '':
        zs = ['O'] * len(ys)
        i = 0
        while i < len(zs):
          if ys[i].startswith('('):
            if ys[i].endswith(')'):
              zs[i] = 'S-' + ys[i][1:-1]
            else:
              zs[i] = 'B-' + ys[i][1:-1]
              typ = zs[i][2:]
              i += 1
              while i < len(zs):
                if ys[i].endswith(')'):
                  zs[i] = 'E-' + typ
                  break
                else:
                  zs[i] = 'I-' + typ
                  i += 1
          else:
            pass
          i += 1
        ys = zs
        if len(xs) > 0:
          for x, y in zip(xs, ys):
            fw.write(x + '\t' + y + '\n')
          fw.write('\n')
          xs = []
          ys = []
      else:
        v = line.split()
        xs.append(v[3])
        ys.append(v[10])

    if len(xs) > 0:
      for x, y in zip(xs, ys):
        fw.write(x + '\t' + y + '\n')
      fw.write('\n')
      xs = []
      ys = []

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='o5 to bieso')
  parser.add_argument('--input_file', type=str,
                      help='path to input file')
  parser.add_argument('--output_file', type=str, default='',
                      help='path to output file')
  args = parser.parse_args()

  o5_bieso(args.input_file,
           args.output_file)
